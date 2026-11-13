"""Check the hand-written chainctl references against the generated ones.

Usage: python3 scripts/chainctl-references/check_flags.py

The generated chainctl reference under content/platform/chainctl/chainctl-docs/
is chainctl's own help text, and it's the canonical list of each command's
flags. The hand-written references for `chainctl checks` and
`chainctl develop` describe the same commands in more detail, so they can
fall behind when a chainctl release adds or removes a flag.

For each command in the generated reference, the script finds the section
of the hand-written page that covers it: the section headed with the
command's name, or, for a subcommand with no section of its own, the
section of its nearest parent command. A flag counts as documented when it
appears in inline code in that section, or anywhere on the page outside
the command sections, such as a "Flags for every command" table. Flags
that appear only in fenced examples, such as a ```shell block, don't
count; a command's synopsis, a fenced block with no language, does.

The script reports three kinds of drift:
- a command directly under the page's command group, such as
  `chainctl develop exec`, that has no section on the page
- a flag in chainctl's help that the page doesn't document
- a flag that a command section documents in inline code, such as
  `--dry`, that no command's help lists

flags.toml, next to this script, lists the pages to check and the flags to
ignore, each with its reason.

The script exits 0 when the pages match the generated reference, 1 when it
finds drift, and 2 when flags.toml is out of date, such as an ignore entry
that matches nothing. Reviewers run it after an AutoDocs update; no CI job
runs it.

Standard library only. Python 3.11 or later, for tomllib.
"""

import re
import sys
import tomllib
from dataclasses import dataclass, field
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent
CONTENT_DIR = REPO_ROOT / "content"
GENERATED_DIR = CONTENT_DIR / "platform" / "chainctl" / "chainctl-docs"
CONFIG_FILE = SCRIPT_DIR / "flags.toml"

TITLE = re.compile(r'^title: "(chainctl[^"]*)"$', re.MULTILINE)
# A flag at the start of a help line, such as "  -o, --output string".
HELP_FLAG = re.compile(r"^\s*(?:-\w, )?--([a-z][a-z0-9-]*)", re.MULTILINE)
HEADING = re.compile(r"^(#{1,6}) +(.*?)\s*$")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
INLINE_CODE = re.compile(r"`([^`\n]+)`")
FLAG = re.compile(r"(?<![\w-])--([a-z][a-z0-9-]*)")
ANCHOR = re.compile(r"\s*\{#[^}]*\}$")


@dataclass
class Command:
    """One command from the generated reference."""

    name: str
    flags: set[str]
    inherited: set[str]


@dataclass
class Page:
    """A hand-written reference, split into command sections."""

    path: str
    sections: dict[str, str] = field(default_factory=dict)
    shared_text: str = ""


def options_block(markdown, heading):
    """Return the code block under a generated page's options heading."""
    match = re.search(
        r"^### " + re.escape(heading) + r"\n+```\n(.*?)\n```",
        markdown,
        re.MULTILINE | re.DOTALL,
    )
    if match is None:
        return ""
    return match.group(1)


def parse_generated(markdown):
    """Read a command's name and flags from a generated reference page."""
    title = TITLE.search(markdown)
    if title is None:
        return None
    flags = set(HELP_FLAG.findall(options_block(markdown, "Options")))
    inherited = set(
        HELP_FLAG.findall(
            options_block(markdown, "Options inherited from parent commands")
        )
    )
    # Every command takes --help, so pages needn't document it, but a page
    # that mentions it isn't wrong.
    flags.discard("help")
    inherited.add("help")
    return Command(title.group(1), flags, inherited)


def read_generated(root):
    """Return every generated command under root, such as chainctl checks."""
    prefix = "chainctl_" + root.split(" ", 1)[1].replace(" ", "_")
    commands = {}
    for path in sorted(GENERATED_DIR.glob(prefix + "*.md")):
        command = parse_generated(path.read_text(encoding="utf-8"))
        if command is None:
            continue
        if command.name == root or command.name.startswith(root + " "):
            commands[command.name] = command
    return commands


def without_examples(markdown):
    """Return the page without its fenced examples.

    A fenced block with a language, such as ```shell, is an example, and
    the script drops it. A block with no language is a command's synopsis,
    such as ``` followed by `chainctl checks migrate [PATH] [--dry]`, and
    its lines are kept, wrapped in backticks so they count as inline code.
    """
    kept = []
    fence = None
    is_synopsis = False
    for line in markdown.splitlines():
        match = FENCE.match(line)
        if fence is None and match:
            fence = match.group(1)[0] * 3
            is_synopsis = line.strip() == match.group(1)
            continue
        if fence is not None:
            if line.strip().startswith(fence):
                fence = None
            elif is_synopsis and line.strip():
                kept.append("`" + line.strip() + "`")
            continue
        kept.append(line)
    return "\n".join(kept)


def heading_name(text):
    """Return a heading's text without its anchor or backticks."""
    return ANCHOR.sub("", text).replace("`", "").strip()


def split_page(path, markdown, root, level):
    """Split a hand-written page into its command sections and the rest.

    A command section starts at a heading of the given level whose text is
    a command under root, and ends at the next heading of that level or
    higher. Everything outside the command sections is shared text.
    """
    page = Page(path)
    shared = []
    current = None
    body = []
    for line in without_examples(markdown).splitlines():
        heading = HEADING.match(line)
        if heading and len(heading.group(1)) <= level:
            if current is not None:
                page.sections[current] = "\n".join(body)
            name = heading_name(heading.group(2))
            is_command = name == root or name.startswith(root + " ")
            if len(heading.group(1)) == level and is_command:
                current = name
                body = []
                continue
            current = None
        if current is None:
            shared.append(line)
        else:
            body.append(line)
    if current is not None:
        page.sections[current] = "\n".join(body)
    page.shared_text = "\n".join(shared)
    return page


def documented_flags(text):
    """Return the flags that appear in the text's inline code."""
    flags = set()
    for span in INLINE_CODE.findall(text):
        flags.update(FLAG.findall(span))
    return flags


def section_for(command, root, page):
    """Return the section that covers a command, or None.

    The root command and each command directly under it need a section of
    their own. A deeper subcommand without one, such as
    `chainctl develop github login`, is covered by its nearest parent's
    section, such as `chainctl develop github`.
    """
    name = command
    while name != root:
        if name in page.sections:
            return name
        parent = name.rsplit(" ", 1)[0]
        if parent == root:
            return None
        name = parent
    if root in page.sections:
        return root
    return None


@dataclass
class Finding:
    """One difference between a page and the generated reference."""

    page: str
    command: str
    message: str


def check_page(page, root, commands, ignored):
    """Compare one hand-written page with the generated commands.

    Returns the findings, and the ignored flags that were used, so the
    caller can report ignore entries that no longer match anything.
    """
    findings = []
    used = set()
    shared = documented_flags(page.shared_text)
    known = set()
    for command in commands.values():
        known |= command.flags | command.inherited

    for name, command in sorted(commands.items()):
        section = section_for(name, root, page)
        if section is None and name != root:
            findings.append(Finding(page.path, name, "has no section on the page"))
            continue
        documented = shared
        if section is not None:
            documented = documented | documented_flags(page.sections[section])
        missing = set()
        for flag in command.flags - documented:
            if flag in ignored:
                used.add(flag)
            else:
                missing.add(flag)
        if missing:
            flags = ", ".join("--" + flag for flag in sorted(missing))
            findings.append(
                Finding(page.path, name, f"isn't documented on the page: {flags}")
            )

    for name, text in sorted(page.sections.items()):
        unknown = documented_flags(text) - known
        if unknown:
            flags = ", ".join("--" + flag for flag in sorted(unknown))
            findings.append(
                Finding(
                    page.path,
                    name,
                    f"documents flags that chainctl's help doesn't list: {flags}",
                )
            )
    return findings, used


def main():
    with CONFIG_FILE.open("rb") as config_file:
        config = tomllib.load(config_file)
    ignored = {entry["flag"]: entry["reason"] for entry in config.get("ignore", [])}

    findings = []
    used = set()
    for entry in config["page"]:
        commands = read_generated(entry["command"])
        if not commands:
            print(f"No generated pages for {entry['command']} in {GENERATED_DIR}.")
            return 2
        path = CONTENT_DIR / entry["path"]
        page = split_page(
            entry["path"],
            path.read_text(encoding="utf-8"),
            entry["command"],
            entry["heading_level"],
        )
        page_findings, page_used = check_page(page, entry["command"], commands, ignored)
        findings += page_findings
        used |= page_used
        print(f"Checked {len(commands)} commands against {entry['path']}.")

    for finding in findings:
        print(f"DRIFT   {finding.page}  {finding.command} {finding.message}")

    unused = sorted(set(ignored) - used)
    for flag in unused:
        print(
            f"STALE   flags.toml ignores --{flag}, but every page documents it or no command has it."
        )
    if unused:
        return 2
    if findings:
        print(
            f"\n{len(findings)} difference(s). Update the page, or add an ignore entry with its reason to flags.toml."
        )
        return 1
    print("\nThe pages match the generated reference.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
