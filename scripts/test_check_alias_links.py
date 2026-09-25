#!/usr/bin/env python3
"""Tests for check_alias_links.py.

Run directly, no dependencies beyond the standard library:

    python3 scripts/test_check_alias_links.py
"""

import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

import check_alias_links as checker


def fix_quietly(findings, root):
    """apply_fixes, with its progress output kept out of the test report."""
    with redirect_stdout(io.StringIO()):
        checker.apply_fixes(findings, root)


def write_repo(files, aliases=()):
    """Build a throwaway repo containing `files` and an alias map.

    `files` maps a repo-relative path to its text. `aliases` is a sequence of
    (alias, target) pairs written in the nginx form Hugo emits.
    """
    root = Path(tempfile.mkdtemp())
    for name, text in files.items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    alias_map = root / "public" / "_aliases"
    alias_map.parent.mkdir(parents=True, exist_ok=True)
    alias_map.write_text(
        "".join(f'"~^{a}(/.*)?$" {t}$1;\n' for a, t in aliases), encoding="utf-8"
    )
    return root, alias_map


class LoadAliases(unittest.TestCase):
    def test_parses_a_rule(self):
        _, alias_map = write_repo({}, [("/old/page", "/new/page")])
        self.assertEqual(checker.load_aliases(alias_map), {"/old/page": "/new/page"})

    def test_follows_a_chain_to_the_real_page(self):
        _, alias_map = write_repo({}, [("/a", "/b"), ("/b", "/c")])
        self.assertEqual(checker.load_aliases(alias_map)["/a"], "/c")

    def test_a_cycle_terminates(self):
        _, alias_map = write_repo({}, [("/a", "/b"), ("/b", "/a")])
        self.assertIn("/a", checker.load_aliases(alias_map))

    def test_ignores_lines_that_are_not_rules(self):
        _, alias_map = write_repo({}, [("/old", "/new")])
        alias_map.write_text("# a comment\n" + alias_map.read_text(), encoding="utf-8")
        self.assertEqual(checker.load_aliases(alias_map), {"/old": "/new"})


class FindStale(unittest.TestCase):
    def check(self, body, aliases=(("/old/page", "/new/page"),), name="content/a.md"):
        root, alias_map = write_repo({name: body}, aliases)
        return checker.find_stale(checker.load_aliases(alias_map), root)

    def test_flags_a_markdown_link(self):
        found = self.check("See [the page](/old/page/).\n")
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0]["old"], "/old/page/")
        self.assertEqual(found[0]["new"], "/new/page/")

    def test_flags_an_href(self):
        found = self.check('<a href="/old/page/">x</a>\n', name="layouts/index.html")
        self.assertEqual([f["new"] for f in found], ["/new/page/"])

    def test_flags_an_absolute_link_and_makes_it_relative(self):
        found = self.check("[x](https://edu.chainguard.dev/old/page/)\n")
        self.assertEqual(len(found), 1)
        self.assertTrue(found[0]["absolute"])
        self.assertEqual(found[0]["new"], "/new/page/")

    def test_preserves_a_fragment(self):
        found = self.check("[x](/old/page/#a-heading)\n")
        self.assertEqual(found[0]["new"], "/new/page/#a-heading")

    def test_preserves_the_absence_of_a_trailing_slash(self):
        found = self.check("[x](/old/page)\n")
        self.assertEqual(found[0]["new"], "/new/page")

    def test_reports_the_right_line(self):
        found = self.check("one\ntwo\n[x](/old/page/)\n")
        self.assertEqual(found[0]["line"], 3)

    def test_ignores_a_canonical_link(self):
        self.assertEqual(self.check("[x](/new/page/)\n"), [])

    def test_ignores_aliases_frontmatter(self):
        body = "---\ntitle: x\naliases:\n- /old/page/\n---\n\nbody\n"
        self.assertEqual(self.check(body), [])

    def test_ignores_a_fenced_code_block(self):
        body = 'before\n\n```html\n<a href="/old/page/">x</a>\n```\n\nafter\n'
        self.assertEqual(self.check(body), [])

    def test_does_not_match_a_longer_path_that_merely_starts_with_an_alias(self):
        self.assertEqual(self.check("[x](/old/page-two/)\n"), [])


class ApplyFixes(unittest.TestCase):
    def test_rewrites_a_markdown_link(self):
        root, alias_map = write_repo(
            {"content/a.md": "[x](/old/page/)\n"}, [("/old/page", "/new/page")]
        )
        aliases = checker.load_aliases(alias_map)
        fix_quietly(checker.find_stale(aliases, root), root)

        self.assertEqual((root / "content/a.md").read_text(), "[x](/new/page/)\n")
        self.assertEqual(checker.find_stale(aliases, root), [])

    def test_absolute_links_become_root_relative(self):
        root, alias_map = write_repo(
            {"content/a.md": "[x](https://edu.chainguard.dev/old/page/)\n"},
            [("/old/page", "/new/page")],
        )
        fix_quietly(checker.find_stale(checker.load_aliases(alias_map), root), root)
        self.assertEqual((root / "content/a.md").read_text(), "[x](/new/page/)\n")

    def test_a_short_alias_does_not_corrupt_a_longer_one_on_the_same_line(self):
        root, alias_map = write_repo(
            {"content/a.md": "[a](/old/) and [b](/old/page/)\n"},
            [("/old", "/new"), ("/old/page", "/elsewhere/page")],
        )
        aliases = checker.load_aliases(alias_map)
        fix_quietly(checker.find_stale(aliases, root), root)

        self.assertEqual(
            (root / "content/a.md").read_text(),
            "[a](/new/) and [b](/elsewhere/page/)\n",
        )
        self.assertEqual(checker.find_stale(aliases, root), [])


class AgainstTheRealBuild(unittest.TestCase):
    """Ground-truth check against this repo, when a build is present."""

    def setUp(self):
        if not checker.ALIAS_MAP.is_file():
            self.skipTest("no public/_aliases; run 'npm run build' first")

    def test_the_alias_map_parses(self):
        self.assertGreater(len(checker.load_aliases()), 100)

    def test_the_repo_is_clean(self):
        findings = checker.find_stale(checker.load_aliases())
        self.assertEqual(
            findings,
            [],
            "stale links found:\n"
            + "\n".join(f"{f['file']}:{f['line']}: {f['old']}" for f in findings),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
