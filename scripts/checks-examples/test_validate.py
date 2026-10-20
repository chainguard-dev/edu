"""Tests for scripts/checks-examples/validate.py.

None of these run chainctl or need the network: the validator is a fake
that records what it was given. One test reads the real content/ and
examples.toml, to check that every manifest entry still matches a block.

Run with:
    python3 -m unittest discover -s scripts/checks-examples -v
"""

import os
import stat
import sys
import tempfile
import textwrap
import tomllib
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import validate  # noqa: E402

PAGE = "chainguard/checks/example.md"


def markdown(text):
    return textwrap.dedent(text).lstrip("\n")


def recording_validator(passes=True):
    """Return a fake validator, and the list it appends each run's files to.

    Each run is recorded as {path: text} for every file in the scratch
    repository.
    """
    runs = []

    def fake(repo_dir):
        files = {}
        for path in sorted(Path(repo_dir).rglob("*")):
            if path.is_file():
                relative = path.relative_to(repo_dir).as_posix()
                files[relative] = path.read_text(encoding="utf-8")
        runs.append(files)
        return passes, "" if passes else "fake refusal"

    return fake, runs


class ExtractBlocksTest(unittest.TestCase):
    def test_titled_and_untitled_blocks(self):
        page = markdown("""
            Intro.

            ```yaml {title=".chainguard/ci.yaml"}
            version: 1
            ```

            ```yaml
            checks: {}
            ```
            """)
        blocks = validate.extract_blocks(page, PAGE)
        self.assertEqual(len(blocks), 2)
        self.assertEqual(blocks[0].title, ".chainguard/ci.yaml")
        self.assertEqual(blocks[0].line, 3)
        self.assertEqual(blocks[0].text, "version: 1\n")
        self.assertIsNone(blocks[1].title)
        self.assertEqual(blocks[1].line, 7)

    def test_fence_in_list_keeps_yaml_nesting(self):
        # The fence is indented three spaces, under a numbered list item.
        # Only those three spaces come off each line; the YAML's own
        # indentation stays.
        page = (
            "1. Add the file:\n"
            "\n"
            '   ```yaml {title=".chainguard/ci.yaml"}\n'
            "   version: 1\n"
            "   checks:\n"
            "     test:\n"
            "       cmd: go test ./...\n"
            "   ```\n"
        )
        [block] = validate.extract_blocks(page, PAGE)
        self.assertEqual(
            block.text,
            "version: 1\nchecks:\n  test:\n    cmd: go test ./...\n",
        )

    def test_blank_and_underindented_lines_in_a_list_fence(self):
        page = "- Item\n\n  ```yaml\n  a: 1\n\n b: 2\n  ```\n"
        [block] = validate.extract_blocks(page, PAGE)
        self.assertEqual(block.text, "a: 1\n\nb: 2\n")

    def test_yaml_fence_shown_inside_a_longer_fence_is_not_a_block(self):
        page = markdown("""
            ````markdown
            ```yaml
            not: a block
            ```
            ````

            ~~~yaml
            real: block
            ~~~
            """)
        blocks = validate.extract_blocks(page, PAGE)
        self.assertEqual([block.text for block in blocks], ["real: block\n"])

    def test_other_languages_are_ignored(self):
        page = markdown("""
            ```shell
            chainctl checks validate .
            ```

            ```yamlish
            nope: 1
            ```
            """)
        self.assertEqual(validate.extract_blocks(page, PAGE), [])

    def test_only_chainguard_titles_and_untitled_blocks_are_examples(self):
        page = markdown("""
            ```yaml {title=".github/workflows/test.yaml"}
            on: push
            ```

            ```yaml {title=".chainguard/ci.yaml"}
            version: 1
            ```

            ```yaml
            checks: {}
            ```
            """)
        blocks = validate.extract_blocks(page, PAGE)
        examples = [block for block in blocks if validate.is_checks_example(block)]
        self.assertEqual(
            [block.title for block in examples], [".chainguard/ci.yaml", None]
        )


class FileTextTest(unittest.TestCase):
    def test_fragment_gets_version_and_empty_environment(self):
        block = validate.Block(PAGE, 1, None, "checks:\n  a:\n    cmd: x\n")
        self.assertEqual(
            block.file_text(),
            "version: 1\nchecks:\n  a:\n    cmd: x\nenvironment: {}\n",
        )

    def test_fragment_with_environment_keeps_it(self):
        block = validate.Block(PAGE, 1, None, "environment:\n  packages: [go]\n")
        self.assertEqual(
            block.file_text(), "version: 1\nenvironment:\n  packages: [go]\n"
        )

    def test_nested_environment_key_is_not_top_level(self):
        block = validate.Block(PAGE, 1, None, "checks:\n  a:\n    environment: go\n")
        self.assertTrue(block.file_text().endswith("environment: {}\n"))

    def test_titled_block_is_written_unchanged(self):
        block = validate.Block(PAGE, 1, ".chainguard/ci/x.yaml", "checks: {}\n")
        self.assertEqual(block.file_text(), "checks: {}\n")


def sample_examples():
    page = markdown("""
        ```yaml {title=".chainguard/ci/services/db/db.yaml"}
        name: db
        ```

        ```yaml {title=".chainguard/ci/app.yaml"}
        services: [db]
        ```

        ```yaml {title=".chainguard/ci.yaml"}
        checks:
          # ...
        ```

        ```yaml {title=".chainguard/ci.yaml"}
        checks:
          lint: {}
        ```

        ```yaml
        checks:
          test: {}
        ```
        """)
    return validate.extract_blocks(page, PAGE)


class FindBlockTest(unittest.TestCase):
    def test_unique_title_needs_no_contains(self):
        block = validate.find_block(
            {"page": PAGE, "title": ".chainguard/ci/app.yaml"}, sample_examples()
        )
        self.assertEqual(block.line, 5)

    def test_shared_title_without_contains_is_an_error(self):
        with self.assertRaisesRegex(
            validate.ManifestError, "matches the blocks at lines"
        ):
            validate.find_block(
                {"page": PAGE, "title": ".chainguard/ci.yaml"}, sample_examples()
            )

    def test_contains_picks_one_of_a_shared_title(self):
        block = validate.find_block(
            {"page": PAGE, "title": ".chainguard/ci.yaml", "contains": "lint"},
            sample_examples(),
        )
        self.assertIn("lint", block.text)

    def test_reference_without_title_means_untitled(self):
        block = validate.find_block({"page": PAGE}, sample_examples())
        self.assertIsNone(block.title)

    def test_stale_reference_is_an_error(self):
        with self.assertRaisesRegex(validate.ManifestError, "no block matches"):
            validate.find_block(
                {"page": PAGE, "title": ".chainguard/ci/gone.yaml"}, sample_examples()
            )


def sample_manifest():
    return {
        "stubs": {
            "env": {"path": ".chainguard/ci/env/default.yaml", "text": "version: 1\n"},
        },
        "group": [
            {
                "reason": "app.yaml uses the db service.",
                "stubs": ["env"],
                "blocks": [
                    {"page": PAGE, "title": ".chainguard/ci/services/db/db.yaml"},
                    {"page": PAGE, "title": ".chainguard/ci/app.yaml"},
                ],
            }
        ],
        "skip": [
            {
                "page": PAGE,
                "title": ".chainguard/ci.yaml",
                "contains": "# ...",
                "reason": "Excerpt.",
            }
        ],
    }


class ReadManifestTest(unittest.TestCase):
    def test_groups_and_skips(self):
        groups, skips = validate.read_manifest(sample_manifest(), sample_examples())
        self.assertEqual(len(groups), 1)
        paths = [path for _, path in groups[0].members]
        self.assertEqual(
            paths, [".chainguard/ci/services/db/db.yaml", ".chainguard/ci/app.yaml"]
        )
        self.assertEqual(
            groups[0].stubs, [(".chainguard/ci/env/default.yaml", "version: 1\n")]
        )
        self.assertEqual(list(skips.values()), ["Excerpt."])

    def test_path_overrides_where_a_block_goes(self):
        manifest = sample_manifest()
        manifest["group"][0]["blocks"].append(
            {"page": PAGE, "path": ".chainguard/ci/test.yaml"}
        )
        groups, _ = validate.read_manifest(manifest, sample_examples())
        self.assertEqual(groups[0].members[-1][1], ".chainguard/ci/test.yaml")

    def test_two_files_at_one_path_is_an_error(self):
        manifest = sample_manifest()
        manifest["group"][0]["blocks"].append(
            {"page": PAGE, "path": ".chainguard/ci/env/default.yaml"}
        )
        with self.assertRaisesRegex(validate.ManifestError, "more than once"):
            validate.read_manifest(manifest, sample_examples())

    def test_unknown_stub_is_an_error(self):
        manifest = sample_manifest()
        manifest["group"][0]["stubs"] = ["missing"]
        with self.assertRaisesRegex(validate.ManifestError, "unknown stub"):
            validate.read_manifest(manifest, sample_examples())

    def test_block_both_grouped_and_skipped_is_an_error(self):
        manifest = sample_manifest()
        manifest["skip"].append(
            {"page": PAGE, "title": ".chainguard/ci/app.yaml", "reason": "x"}
        )
        with self.assertRaisesRegex(
            validate.ManifestError, "both skipped and in a group"
        ):
            validate.read_manifest(manifest, sample_examples())


class ValidateExamplesTest(unittest.TestCase):
    def run_sample(self, passes=True):
        examples = sample_examples()
        groups, skips = validate.read_manifest(sample_manifest(), examples)
        fake, runs = recording_validator(passes)
        results = validate.validate_examples(examples, groups, skips, fake)
        return results, runs

    def test_group_members_and_stubs_share_one_repository(self):
        _, runs = self.run_sample()
        group_run = [run for run in runs if ".chainguard/ci/app.yaml" in run][0]
        self.assertEqual(
            sorted(group_run),
            [
                ".chainguard/ci/app.yaml",
                ".chainguard/ci/env/default.yaml",
                ".chainguard/ci/services/db/db.yaml",
            ],
        )

    def test_every_other_block_runs_alone_and_skips_never_run(self):
        results, runs = self.run_sample()
        # One group run, plus the lint ci.yaml and the untitled fragment.
        self.assertEqual(len(runs), 3)
        self.assertEqual(runs[1], {".chainguard/ci.yaml": "checks:\n  lint: {}\n"})
        self.assertEqual(
            runs[2],
            {
                ".chainguard/ci.yaml": "version: 1\nchecks:\n  test: {}\nenvironment: {}\n"
            },
        )
        statuses = [result.status for result in results]
        self.assertEqual(statuses, ["PASS", "SKIPPED", "PASS", "PASS"])

    def test_unknown_block_that_fails_alone_fails_loudly(self):
        results, _ = self.run_sample(passes=False)
        alone = [r for r in results if r.status == "FAIL" and len(r.members) == 1]
        self.assertEqual(len(alone), 2)
        for result in alone:
            self.assertEqual(result.note, validate.UNKNOWN_BLOCK_ADVICE)

        report = validate.format_report(results)
        self.assertIn("isn't in examples.toml", report)
        self.assertIn("fake refusal", report)
        self.assertIn("0 passed, 4 failed, 1 skipped, in 3 validator runs.", report)

    def test_results_are_in_page_order(self):
        results, _ = self.run_sample()
        lines = [result.members[0][0].line for result in results]
        self.assertEqual(lines, sorted(lines))


class ChainctlValidateTest(unittest.TestCase):
    """Run a fake chainctl, a shell script that prints canned output."""

    def fake_chainctl(self, output, status):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        script = Path(directory.name) / "chainctl"
        script.write_text(f"#!/bin/sh\necho '{output}'\nexit {status}\n")
        script.chmod(script.stat().st_mode | stat.S_IXUSR)
        return str(script)

    @unittest.skipIf(os.name != "posix", "the fake chainctl is a shell script")
    def test_exit_zero_with_nothing_checked_is_not_a_pass(self):
        chainctl = self.fake_chainctl("no checks configuration under scratch-repo", 0)
        passed, output = validate.chainctl_validate(chainctl)("scratch-repo")
        self.assertFalse(passed)
        self.assertIn("no checks configuration", output)

    @unittest.skipIf(os.name != "posix", "the fake chainctl is a shell script")
    def test_exit_status_decides_otherwise(self):
        self.assertTrue(
            validate.chainctl_validate(self.fake_chainctl("ok", 0))("/x")[0]
        )
        self.assertFalse(
            validate.chainctl_validate(self.fake_chainctl("bad", 1))("/x")[0]
        )


class RealManifestTest(unittest.TestCase):
    def test_every_entry_matches_exactly_one_block_in_the_docs(self):
        with open(validate.MANIFEST_FILE, "rb") as f:
            manifest = tomllib.load(f)
        examples = validate.find_examples(validate.CONTENT_DIR, manifest["directories"])
        self.assertGreater(len(examples), 0)
        validate.read_manifest(manifest, examples)  # raises ManifestError if stale


if __name__ == "__main__":
    unittest.main()
