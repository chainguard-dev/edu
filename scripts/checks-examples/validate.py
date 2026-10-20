"""Validate the Chainguard Checks and Workspaces YAML examples in the docs.

Usage: python3 scripts/checks-examples/validate.py [--chainctl PATH]

The script finds every YAML code block on the pages under the directories
that examples.toml lists, and checks each one with `chainctl checks
validate`, which runs offline and needs no Chainguard account.

Two kinds of block are checked:
- A titled block whose title is a path under .chainguard/, such as
  ```yaml {title=".chainguard/ci.yaml"}. It's written to that path.
- An untitled ```yaml block. These are fragments of a .chainguard/ci.yaml
  file, so the script writes them to that path, adding `version: 1` and
  `environment: {}` when the fragment lacks them.
Titled blocks for other files, such as a GitHub workflow, are ignored.

By default each block is validated alone, in a scratch repository of its
own. examples.toml, next to this script, lists the exceptions:
- groups of blocks that only make sense together, plus any companion
  ("stub") files they need. A group can write an untitled block somewhere
  other than .chainguard/ci.yaml.
- blocks to skip, such as an excerpt that elides lines with "# ...", or a
  file that the validator doesn't read

The validator exits 0 when a repository holds nothing it reads as checks
configuration, such as a lone .chainguard/ci/resources.yaml. The script
counts that as a failure, because nothing was checked.

A block that examples.toml doesn't mention must pass alone. If it fails,
the report says so and suggests a manifest entry, so a new example can't
slip by unchecked. An entry that matches no block, or more than one, stops
the script before it validates anything.

The script prints a PASS, FAIL, or SKIPPED line per block and exits 1 if
any block fails, or 2 if examples.toml is out of date with the docs.
Reviewers run it by hand; no CI job runs it, because the configuration
schema changes with each chainctl release.

Standard library only. Python 3.11 or later, for tomllib.
"""

import argparse
import re
import subprocess
import sys
import tempfile
import tomllib
from dataclasses import dataclass, field
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent
CONTENT_DIR = REPO_ROOT / "content"
MANIFEST_FILE = SCRIPT_DIR / "examples.toml"

# An opening fence: indentation, then three or more backticks or tildes,
# then the info string, such as `yaml {title=".chainguard/ci.yaml"}`.
FENCE_OPEN = re.compile(r"^( *)(`{3,}|~{3,})(.*)$")
TITLE = re.compile(r'title="([^"]*)"')

FRAGMENT_PATH = ".chainguard/ci.yaml"


@dataclass
class Block:
    page: str  # path relative to content/
    line: int  # line number of the opening fence
    title: str | None  # None for an untitled block
    text: str

    def default_path(self):
        """Return where the block goes in a scratch repository by default."""
        if self.title is None:
            return FRAGMENT_PATH
        return self.title

    def file_text(self):
        """Return the file contents to validate.

        An untitled block is a fragment of a v1 .chainguard/ci.yaml, which
        must declare both `version` and `environment`.
        """
        if self.title is not None:
            return self.text
        text = self.text
        if not re.search(r"^version:", text, re.MULTILINE):
            text = "version: 1\n" + text
        if not re.search(r"^environment:", text, re.MULTILINE):
            text = text + "environment: {}\n"
        return text

    def label(self, path=None):
        """Return a one-line description, such as page.md:42  .chainguard/ci.yaml.

        `path` is where the block was written, when that isn't its default.
        """
        if path is None:
            path = self.default_path()
        if self.title is None:
            name = f"(untitled, as {path})"
        elif path != self.title:
            name = f"{self.title}, as {path}"
        else:
            name = self.title
        return f"{self.page}:{self.line}  {name}"


@dataclass
class Group:
    reason: str
    members: list  # list of (Block, path in repo)
    stubs: list  # list of (path in repo, file text)


@dataclass
class Result:
    status: str  # "PASS", "FAIL", or "SKIPPED"
    members: list  # list of (Block, path in repo)
    note: str = ""  # a group's or skip's reason, or advice for an unknown block
    stubs: list = field(default_factory=list)  # paths of a group's stub files
    output: str = ""  # the validator's output


# --- Extracting blocks ------------------------------------------------------


def strip_indent(line, width):
    """Remove up to `width` leading spaces, as Markdown does inside a fence.

    Removing exactly the fence's indentation, rather than all leading
    spaces, keeps the YAML nesting intact for a fence inside a list item.
    """
    removed = 0
    while removed < width and line.startswith(" "):
        line = line[1:]
        removed += 1
    return line


def extract_blocks(markdown, page):
    """Return every YAML code block in a page's Markdown, in page order.

    Fences of any language are tracked, so a YAML fence shown inside a
    longer Markdown fence isn't mistaken for a real block.
    """
    lines = markdown.splitlines()
    blocks = []
    i = 0
    while i < len(lines):
        opening = FENCE_OPEN.match(lines[i])
        if opening is None:
            i += 1
            continue

        indent = len(opening.group(1))
        fence = opening.group(2)
        info = opening.group(3).strip()
        # A closing fence repeats the opening character at least as many
        # times, with nothing else on the line.
        closing = re.compile(
            r"^ *" + re.escape(fence[0]) + "{" + str(len(fence)) + r",}\s*$"
        )

        body = []
        j = i + 1
        while j < len(lines) and not closing.match(lines[j]):
            body.append(strip_indent(lines[j], indent))
            j += 1

        language = info.split("{")[0].strip()
        if language == "yaml":
            title_match = TITLE.search(info)
            title = title_match.group(1) if title_match else None
            text = "\n".join(body) + "\n"
            blocks.append(Block(page=page, line=i + 1, title=title, text=text))

        i = j + 1
    return blocks


def is_checks_example(block):
    """Return True for a block this script validates."""
    return block.title is None or block.title.startswith(".chainguard/")


def find_examples(content_dir, directories):
    """Return the Checks and Workspaces examples under the given directories."""
    examples = []
    for directory in directories:
        for path in sorted((content_dir / directory).rglob("*.md")):
            page = path.relative_to(content_dir).as_posix()
            for block in extract_blocks(path.read_text(encoding="utf-8"), page):
                if is_checks_example(block):
                    examples.append(block)
    return examples


# --- Reading the manifest ---------------------------------------------------


class ManifestError(Exception):
    """examples.toml doesn't match the docs."""


def describe_reference(reference):
    """Return a manifest block reference as text, for error messages."""
    parts = [f'page = "{reference["page"]}"']
    if "title" in reference:
        parts.append(f'title = "{reference["title"]}"')
    else:
        parts.append("untitled")
    if "contains" in reference:
        parts.append(f'contains = "{reference["contains"]}"')
    return "{ " + ", ".join(parts) + " }"


def find_block(reference, examples):
    """Return the one example a manifest reference names.

    A reference names a page, a title (or no title, for an untitled block),
    and, when the page has more than one such block, a `contains` string
    that only the intended block holds.
    """
    title = reference.get("title")
    contains = reference.get("contains")
    matches = []
    for block in examples:
        if block.page != reference["page"] or block.title != title:
            continue
        if contains is not None and contains not in block.text:
            continue
        matches.append(block)

    if len(matches) == 0:
        raise ManifestError(
            f"no block matches {describe_reference(reference)}. "
            "Was the page or the example changed?"
        )
    if len(matches) > 1:
        lines = ", ".join(str(block.line) for block in matches)
        raise ManifestError(
            f"{describe_reference(reference)} matches the blocks at lines "
            f"{lines}. Add or lengthen `contains` so it matches one."
        )
    return matches[0]


def read_manifest(manifest, examples):
    """Return (groups, skips) from a parsed examples.toml.

    skips maps each skipped block's (page, line) to the reason it's skipped.
    """
    stubs = manifest.get("stubs", {})

    groups = []
    for entry in manifest.get("group", []):
        members = []
        for reference in entry["blocks"]:
            block = find_block(reference, examples)
            path = reference.get("path", block.default_path())
            members.append((block, path))

        group_stubs = []
        for name in entry.get("stubs", []):
            if name not in stubs:
                raise ManifestError(
                    f'group "{entry["reason"]}" names unknown stub {name!r}'
                )
            group_stubs.append((stubs[name]["path"], stubs[name]["text"]))

        paths = [path for _, path in members] + [path for path, _ in group_stubs]
        for path in paths:
            if paths.count(path) > 1:
                raise ManifestError(
                    f'group "{entry["reason"]}" writes {path} more than once'
                )
        groups.append(Group(reason=entry["reason"], members=members, stubs=group_stubs))

    skips = {}
    for entry in manifest.get("skip", []):
        block = find_block(entry, examples)
        skips[(block.page, block.line)] = entry["reason"]

    for group in groups:
        for block, _ in group.members:
            if (block.page, block.line) in skips:
                raise ManifestError(
                    f"{block.label()} is both skipped and in a group; pick one"
                )
    return groups, skips


# --- Validating -------------------------------------------------------------

# What `chainctl checks validate` prints, with exit status 0, when the
# repository holds no file it reads as checks configuration, such as a lone
# .chainguard/ci/resources.yaml. Nothing was checked, so it isn't a pass.
NOTHING_CHECKED = "no checks configuration under"


def chainctl_validate(chainctl):
    """Return a function that runs `chainctl checks validate` on a directory.

    The function returns (passed, output), where output is the validator's
    combined stdout and stderr.
    """

    def validate(repo_dir):
        completed = subprocess.run(
            [chainctl, "checks", "validate", str(repo_dir)],
            capture_output=True,
            text=True,
            check=False,
        )
        output = completed.stdout + completed.stderr
        passed = completed.returncode == 0 and NOTHING_CHECKED not in output
        return passed, output

    return validate


def validate_files(files, validate):
    """Write {path: text} into a fresh scratch repository and validate it."""
    with tempfile.TemporaryDirectory(prefix="checks-example-") as repo_dir:
        for path, text in files.items():
            target = Path(repo_dir) / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text, encoding="utf-8")
        return validate(repo_dir)


UNKNOWN_BLOCK_ADVICE = (
    "This block isn't in examples.toml, so it must pass alone. Fix the "
    "example, or, if it needs another file beside it, add a [[group]]; if "
    "it's an excerpt, add a [[skip]]."
)


def validate_examples(examples, groups, skips, validate):
    """Validate every example and return a list of Results, in page order.

    Each group runs once, and every block that's neither grouped nor skipped
    runs alone. A block can belong to more than one group.
    """
    results = []
    grouped = set()

    for group in groups:
        files = {path: block.file_text() for block, path in group.members}
        for path, text in group.stubs:
            files[path] = text
        passed, output = validate_files(files, validate)
        results.append(
            Result(
                status="PASS" if passed else "FAIL",
                members=group.members,
                note=group.reason,
                stubs=[path for path, _ in group.stubs],
                output=output,
            )
        )
        for block, _ in group.members:
            grouped.add((block.page, block.line))

    for block in examples:
        key = (block.page, block.line)
        if key in grouped:
            continue
        members = [(block, block.default_path())]
        if key in skips:
            results.append(Result(status="SKIPPED", members=members, note=skips[key]))
            continue
        passed, output = validate_files(
            {block.default_path(): block.file_text()}, validate
        )
        results.append(
            Result(
                status="PASS" if passed else "FAIL",
                members=members,
                note="" if passed else UNKNOWN_BLOCK_ADVICE,
                output=output,
            )
        )

    def first_block_position(result):
        block, _ = result.members[0]
        return block.page, block.line

    results.sort(key=first_block_position)
    return results


# --- Reporting --------------------------------------------------------------


def indent(text):
    return "\n".join("        " + line for line in text.strip().splitlines())


def warnings_in(output):
    """Return the validator's warning lines, which it prints even on a pass."""
    lines = [line for line in output.splitlines() if line.startswith("warning:")]
    return "\n".join(lines)


def format_report(results):
    """Return the report text, ending with a summary line."""
    lines = []
    for result in results:
        for block, path in result.members:
            lines.append(f"{result.status:<8}{block.label(path)}")
        for path in result.stubs:
            lines.append(f"        + stub {path}")
        if len(result.members) > 1 or result.stubs:
            lines.append(indent("Group: " + result.note))
        elif result.note:
            lines.append(indent(result.note))
        if result.status == "FAIL":
            lines.append(indent(result.output))
        elif result.status == "PASS" and warnings_in(result.output):
            lines.append(indent(warnings_in(result.output)))

    counts = {"PASS": 0, "FAIL": 0, "SKIPPED": 0}
    runs = 0
    for result in results:
        counts[result.status] += len(result.members)
        if result.status != "SKIPPED":
            runs += 1
    run_word = "run" if runs == 1 else "runs"
    lines.append("")
    lines.append(
        f"{counts['PASS']} passed, {counts['FAIL']} failed, "
        f"{counts['SKIPPED']} skipped, in {runs} validator {run_word}. "
        "A block in more than one group is counted once per group."
    )
    return "\n".join(lines)


def chainctl_version(chainctl):
    """Return chainctl's version number, such as 0.2.388."""
    completed = subprocess.run(
        [chainctl, "version"], capture_output=True, text=True, check=True
    )
    match = re.search(r"^GitVersion:\s*(\S+)", completed.stdout, re.MULTILINE)
    if match is None:
        return "unknown"
    return match.group(1)


def main():
    parser = argparse.ArgumentParser(
        description="Validate the Checks and Workspaces YAML examples in the docs."
    )
    parser.add_argument(
        "--chainctl", default="chainctl", help="the chainctl binary to run"
    )
    args = parser.parse_args()

    with open(MANIFEST_FILE, "rb") as f:
        manifest = tomllib.load(f)
    examples = find_examples(CONTENT_DIR, manifest["directories"])

    try:
        groups, skips = read_manifest(manifest, examples)
    except ManifestError as error:
        print(f"error: {MANIFEST_FILE.name}: {error}", file=sys.stderr)
        return 2

    print(f"chainctl {chainctl_version(args.chainctl)}")
    print(f"{len(examples)} examples found under {', '.join(manifest['directories'])}")
    print()

    results = validate_examples(
        examples, groups, skips, chainctl_validate(args.chainctl)
    )
    print(format_report(results))

    if any(result.status == "FAIL" for result in results):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
