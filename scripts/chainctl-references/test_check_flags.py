"""Tests for scripts/chainctl-references/check_flags.py.

Most tests use small made-up pages. One reads the real flags.toml and
content/, to check that every page it names still exists and has command
sections.

Run with:
    python3 -m unittest discover -s scripts/chainctl-references -v
"""

import sys
import textwrap
import tomllib
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_flags  # noqa: E402

GENERATED_PAGE = textwrap.dedent("""\
    ---
    title: "chainctl demo run"
    ---
    ## chainctl demo run

    ### Options

    ```
          --dry            Print the plan.
      -i, --stdin          Read standard input.
      -h, --help           help for run
    ```

    ### Options inherited from parent commands

    ```
      -o, --output string  Output format.
    ```
    """)

HAND_WRITTEN_PAGE = textwrap.dedent("""\
    Intro text mentions `--output`.

    ## Flags for every command

    | Flag | Description |
    | ---- | ----------- |
    | `--parent` | The organization. |

    ## chainctl demo run {#chainctl-demo-run}

    ```
    chainctl demo run [--dry]
    ```

    ```shell
    chainctl demo run --stdin
    ```

    ## chainctl demo github

    Use `--port` with `login`.

    ## Exit codes

    Mentions `--keep`, which belongs to no command section.
    """)


def command(name, flags=(), inherited=()):
    return check_flags.Command(name, set(flags), set(inherited))


class ParseGeneratedTest(unittest.TestCase):
    def test_reads_title_and_both_option_blocks(self):
        parsed = check_flags.parse_generated(GENERATED_PAGE)
        self.assertEqual(parsed.name, "chainctl demo run")
        self.assertEqual(parsed.flags, {"dry", "stdin"})
        self.assertEqual(parsed.inherited, {"output", "help"})

    def test_page_without_a_title_is_skipped(self):
        self.assertIsNone(check_flags.parse_generated("no front matter here"))


class WithoutExamplesTest(unittest.TestCase):
    def test_drops_examples_and_keeps_synopsis_as_inline_code(self):
        text = check_flags.without_examples(HAND_WRITTEN_PAGE)
        self.assertIn("`chainctl demo run [--dry]`", text)
        self.assertNotIn("--stdin", text)


class SplitPageTest(unittest.TestCase):
    def setUp(self):
        self.page = check_flags.split_page(
            "demo.md", HAND_WRITTEN_PAGE, "chainctl demo", 2
        )

    def test_finds_command_sections_by_heading(self):
        self.assertEqual(
            set(self.page.sections), {"chainctl demo run", "chainctl demo github"}
        )

    def test_section_ends_at_the_next_heading_of_its_level(self):
        self.assertIn("--port", self.page.sections["chainctl demo github"])
        self.assertNotIn("--keep", self.page.sections["chainctl demo github"])

    def test_other_text_is_shared(self):
        self.assertIn("--parent", self.page.shared_text)
        self.assertIn("--keep", self.page.shared_text)


class SectionForTest(unittest.TestCase):
    def setUp(self):
        self.page = check_flags.split_page(
            "demo.md", HAND_WRITTEN_PAGE, "chainctl demo", 2
        )

    def test_command_with_its_own_section(self):
        self.assertEqual(
            check_flags.section_for("chainctl demo run", "chainctl demo", self.page),
            "chainctl demo run",
        )

    def test_deeper_subcommand_uses_its_parents_section(self):
        self.assertEqual(
            check_flags.section_for(
                "chainctl demo github login", "chainctl demo", self.page
            ),
            "chainctl demo github",
        )

    def test_direct_subcommand_without_a_section_has_none(self):
        self.assertIsNone(
            check_flags.section_for("chainctl demo exec", "chainctl demo", self.page)
        )


class CheckPageTest(unittest.TestCase):
    def setUp(self):
        self.page = check_flags.split_page(
            "demo.md", HAND_WRITTEN_PAGE, "chainctl demo", 2
        )

    def check(self, commands, ignored=None):
        # The page documents --port for github login, so include that
        # command unless a test leaves it out on purpose.
        by_name = {
            "chainctl demo github login": command(
                "chainctl demo github login", ["port"]
            )
        }
        by_name.update({c.name: c for c in commands})
        return check_flags.check_page(
            self.page, "chainctl demo", by_name, ignored or {}
        )

    def messages(self, findings):
        return [f"{f.command} {f.message}" for f in findings]

    def test_matching_page_has_no_findings(self):
        findings, _ = self.check(
            [
                command("chainctl demo run", ["dry", "parent"], ["output"]),
                command("chainctl demo github login", ["port"]),
                command("chainctl demo github", [], ["keep"]),
            ]
        )
        self.assertEqual(findings, [])

    def test_flag_only_in_an_example_is_missing(self):
        findings, _ = self.check([command("chainctl demo run", ["dry", "stdin"])])
        self.assertEqual(
            self.messages(findings),
            ["chainctl demo run isn't documented on the page: --stdin"],
        )

    def test_ignored_flag_is_not_reported_and_is_marked_used(self):
        findings, used = self.check(
            [command("chainctl demo run", ["dry", "stdin"])],
            ignored={"stdin": "reason"},
        )
        self.assertEqual(findings, [])
        self.assertEqual(used, {"stdin"})

    def test_direct_subcommand_without_a_section_is_reported(self):
        findings, _ = self.check(
            [command("chainctl demo run", ["dry"]), command("chainctl demo exec")]
        )
        self.assertIn(
            "chainctl demo exec has no section on the page", self.messages(findings)
        )

    def test_documented_flag_that_no_command_has_is_reported(self):
        findings, _ = self.check(
            [
                command("chainctl demo run", ["dry"]),
                command("chainctl demo github login"),
            ]
        )
        self.assertIn(
            "chainctl demo github documents flags that chainctl's help doesn't list: --port",
            self.messages(findings),
        )


class RealConfigTest(unittest.TestCase):
    def test_every_configured_page_exists_and_has_sections(self):
        with check_flags.CONFIG_FILE.open("rb") as config_file:
            config = tomllib.load(config_file)
        for entry in config["page"]:
            path = check_flags.CONTENT_DIR / entry["path"]
            self.assertTrue(path.exists(), entry["path"])
            page = check_flags.split_page(
                entry["path"],
                path.read_text(encoding="utf-8"),
                entry["command"],
                entry["heading_level"],
            )
            self.assertTrue(page.sections, entry["path"])


if __name__ == "__main__":
    unittest.main()
