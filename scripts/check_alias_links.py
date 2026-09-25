#!/usr/bin/env python3
"""Fail when an internal link points at an alias path instead of the real page.

A page that moves keeps its old URL working through an `aliases:` entry, which
Hugo turns into a redirect. Links inside this repo should not rely on that: each
one costs the reader a 301, and it breaks outright if the alias is ever retired.

The alias map comes from `public/_aliases`, which Hugo writes during a build and
nginx serves in production, so the check measures what is actually deployed
rather than guessing from path patterns.

Run after a build:

    npm run build
    python3 scripts/check_alias_links.py

Exits non-zero and prints `file:line: stale -> canonical` for each finding.
Pass --fix to apply the replacements in place.

Scope is `content/` and `layouts/` by choice, not by omission. Those hold the
links a reader follows. Widening it to the rest of the repo would pull in
contributor docs, archived artifacts, and the generated AI docs bundle, where a
redirect costs a reader nothing. A stale link outside those two directories is
fixed by hand.

Within that scope, two things are skipped: `aliases:` frontmatter, which is
supposed to contain alias paths, and fenced code blocks, where a URL is example
text rather than a live link.
"""

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ALIAS_MAP = REPO / "public" / "_aliases"
SEARCH_DIRS = ["content", "layouts"]
SUFFIXES = {".md", ".html"}

SITE = "https://edu.chainguard.dev"

# Each rule in public/_aliases looks like:
#   "~^/old/path(/.*)?$" /new/path$1;
ALIAS_RULE = re.compile(r'^"~\^(?P<alias>[^("]+)\(/\.\*\)\?\$"\s+(?P<target>\S+?)\$1;$')

# Markdown and HTML links, in both the root-relative and absolute-URL forms.
# Each pattern captures the path in a group named "path".
LINK_PATTERNS = [
    (re.compile(r"\]\(\s*(?P<path>/[^)\s]*)"), False),
    (re.compile(r"href=(?P<q>[\"'])(?P<path>/[^\"']*)(?P=q)"), False),
    (re.compile(r"\]\(\s*" + re.escape(SITE) + r"(?P<path>/[^)\s]*)"), True),
    (
        re.compile(
            r"href=(?P<q>[\"'])" + re.escape(SITE) + r"(?P<path>/[^\"']*)(?P=q)"
        ),
        True,
    ),
]


def load_aliases(alias_map=ALIAS_MAP):
    """Map each alias path to the canonical path it finally redirects to."""
    direct = {}
    for line in alias_map.read_text(encoding="utf-8").splitlines():
        match = ALIAS_RULE.match(line.strip())
        if match:
            direct[match["alias"].rstrip("/")] = match["target"].rstrip("/")

    # An alias can point at another alias. Follow the chain to the real page,
    # guarding against a cycle.
    resolved = {}
    for alias, target in direct.items():
        seen = {alias}
        while target in direct and target not in seen:
            seen.add(target)
            target = direct[target]
        resolved[alias] = target
    return resolved


def split_suffix(link):
    """Split a link into its path and any trailing #fragment or ?query."""
    for separator in ("#", "?"):
        if separator in link:
            cut = link.index(separator)
            return link[:cut], link[cut:]
    return link, ""


def fenced_lines(text):
    """Line numbers inside a ``` fenced code block, which are not live links."""
    fenced = set()
    inside = False
    for number, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            inside = not inside
        elif inside:
            fenced.add(number)
    return fenced


def source_files(repo=REPO):
    for directory in SEARCH_DIRS:
        for path in sorted((repo / directory).rglob("*")):
            if path.suffix in SUFFIXES and path.is_file():
                yield path


def find_stale(aliases, repo=REPO):
    """Every link whose path is an alias, as a list of finding dicts."""
    findings = []
    for path in source_files(repo):
        text = path.read_text(encoding="utf-8")
        skip = fenced_lines(text)
        line_of = _line_lookup(text)

        for pattern, absolute in LINK_PATTERNS:
            for match in pattern.finditer(text):
                link_path, suffix = split_suffix(match["path"])
                alias = link_path.rstrip("/")
                if alias not in aliases:
                    continue
                line = line_of(match.start("path"))
                if line in skip:
                    continue
                trailing = "/" if link_path.endswith("/") and link_path != "/" else ""
                findings.append(
                    {
                        "file": path.relative_to(repo).as_posix(),
                        "line": line,
                        "old": match["path"],
                        "new": aliases[alias] + trailing + suffix,
                        "absolute": absolute,
                    }
                )
    return findings


def _line_lookup(text):
    """Return a function mapping a character offset to a 1-based line number."""
    starts = [0]
    for line in text.splitlines(keepends=True):
        starts.append(starts[-1] + len(line))

    def line_of(offset):
        low, high = 0, len(starts) - 1
        while low < high:
            mid = (low + high) // 2
            if starts[mid] <= offset:
                low = mid + 1
            else:
                high = mid
        return low

    return line_of


def apply_fixes(findings, repo=REPO):
    """Rewrite each stale link in place. Absolute links become root-relative."""
    by_file = defaultdict(list)
    for finding in findings:
        by_file[finding["file"]].append(finding)

    for name, group in sorted(by_file.items()):
        path = repo / name
        text = original = path.read_text(encoding="utf-8")

        replacements = {
            ((SITE if f["absolute"] else "") + f["old"], f["new"]) for f in group
        }
        # Longest first, so a short alias never rewrites part of a longer one.
        for old, new in sorted(replacements, key=lambda pair: -len(pair[0])):
            text = text.replace(f"]({old})", f"]({new})")
            text = text.replace(f'href="{old}"', f'href="{new}"')
            text = text.replace(f"href='{old}'", f"href='{new}'")

        if text != original:
            path.write_text(text, encoding="utf-8")
            print(f"fixed {name}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--fix", action="store_true", help="rewrite the stale links in place"
    )
    args = parser.parse_args()

    if not ALIAS_MAP.is_file():
        sys.exit(f"{ALIAS_MAP} not found. Run 'npm run build' first.")

    findings = find_stale(load_aliases())

    if not findings:
        print("No internal links point at alias paths.")
        return 0

    for finding in findings:
        print(
            f"{finding['file']}:{finding['line']}: {finding['old']} -> {finding['new']}"
        )

    if args.fix:
        apply_fixes(findings)
        print(f"\nFixed {len(findings)} link(s). Rebuild and re-run to confirm.")
        return 0

    print(
        f"\n{len(findings)} internal link(s) point at an alias path instead of the "
        f"page itself.\nEach costs the reader a redirect. Run "
        f"'python3 scripts/check_alias_links.py --fix' to correct them.\n"
        f"Leave the 'aliases:' frontmatter alone -- it still serves inbound links."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
