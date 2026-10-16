#!/usr/bin/env python3
"""Print one fenced code block from a section of a Markdown page.

Shell tests pipe the block into a shell, so they run the commands exactly as
the page shows them. If someone edits a command, the test runs the edit; if
someone renames the section or removes the block, the test fails instead of
running stale commands.

Usage: code-blocks.py PAGE HEADING INDEX

HEADING is the section's heading text without the leading #s or backticks,
such as "Install with curl", or "" for the text before the first heading.
The section ends at the next heading of the same or a higher level. INDEX
counts the section's code blocks from 1, including output blocks, in the
order the page shows them.
"""

import re
import sys
from pathlib import Path

HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
FENCE = re.compile(r"^```")


def blocks_in_section(page: Path, heading: str) -> list[str]:
    # An empty heading selects the introduction, which any heading ends.
    level, blocks, block = (7 if heading == "" else None), [], None
    for line in page.read_text().splitlines():
        if block is not None:
            if FENCE.match(line):
                blocks.append("\n".join(block) + "\n")
                block = None
            else:
                block.append(line)
            continue
        match = HEADING.match(line)
        if match:
            depth, text = len(match.group(1)), match.group(2).replace("`", "")
            if level is not None and depth <= level:
                break
            if level is None and text == heading:
                level = depth
            continue
        if level is not None and FENCE.match(line):
            block = []
    if level is None:
        sys.exit(f"{page}: no heading named {heading!r}")
    return blocks


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    page, heading, index = Path(sys.argv[1]), sys.argv[2], int(sys.argv[3])
    blocks = blocks_in_section(page, heading)
    if not 1 <= index <= len(blocks):
        sys.exit(f"{page}: {heading!r} has {len(blocks)} code blocks, not {index}")
    sys.stdout.write(blocks[index - 1])
