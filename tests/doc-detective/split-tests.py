#!/usr/bin/env python3
"""Write each Doc Detective test in a page or spec file to its own spec file.

Doc Detective runs every test in an input in one browser session. On Console
pages, a test that follows another can hang (see console-cookie.sh), so the
runner gives each test its own process instead.

Usage: split-tests.py INPUT OUT_DIR

INPUT is a Markdown page with inline tests or a JSON spec file.

Prints the path of each spec it writes, one per line, in page order.
"""

import json
import re
import sys
from pathlib import Path

# Same inline syntax Doc Detective reads: [comment]: # (test {...}),
# [comment]: # (step {...}), and [comment]: # (test end).
LINE = re.compile(r"^\[comment\]: # \((test|step) (.*)\)\s*$")


def read_spec(spec: Path) -> list[dict]:
    return json.loads(spec.read_text()).get("tests", [])


def read_page(page: Path) -> list[dict]:
    tests, current = [], None
    for number, line in enumerate(page.read_text().splitlines(), start=1):
        match = LINE.match(line)
        if not match:
            continue
        kind, body = match.groups()
        if kind == "test" and body.strip() == "end":
            if current is None:
                sys.exit(f"{page}:{number}: test end without a test")
            tests.append(current)
            current = None
        elif kind == "test":
            if current is not None:
                sys.exit(f"{page}:{number}: test starts before the previous one ends")
            current = json.loads(body)
            current["steps"] = []
        else:
            if current is None:
                sys.exit(f"{page}:{number}: step outside a test")
            current["steps"].append(json.loads(body))
    if current is not None:
        sys.exit(f"{page}: test {current.get('testId')} has no test end")
    return tests


def split(source: Path, out_dir: Path) -> list[Path]:
    tests = read_spec(source) if source.suffix == ".json" else read_page(source)
    out_dir.mkdir(parents=True, exist_ok=True)
    paths = []
    for index, test in enumerate(tests, start=1):
        name = test.get("testId") or f"test-{index}"
        path = out_dir / f"{index:02d}-{name}.spec.json"
        spec = {"specId": f"{source.name}#{name}", "tests": [test]}
        path.write_text(json.dumps(spec, indent=2) + "\n")
        paths.append(path)
    return paths


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    for spec_path in split(Path(sys.argv[1]), Path(sys.argv[2])):
        print(spec_path)
