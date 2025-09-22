#!/usr/bin/env python3
import argparse
import re
import sys
from pathlib import Path
from collections import Counter, defaultdict

try:
    import yaml  # type: ignore
except Exception as e:
    yaml = None

FENCED_BLOCK_RE = re.compile(
    r"(?P<open>^```+)[ \t]*"
    r"(?P<lang>[A-Za-z0-9_.+-]*)[^\n]*\n"
    r"(?P<code>.*?)(?<=\n)"
    r"^(?P=open)[ \t]*$",
    re.MULTILINE | re.DOTALL,
)

FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)


def read_config(config_path: Path):
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")
    text = config_path.read_text(encoding="utf-8")
    if yaml is None:
        allowed = []
        aliases = {}
        current_key = None
        for line in text.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if ":" in line and not line.startswith("-"):
                current_key = line.split(":", 1)[0].strip()
                continue
            if line.startswith("-") and current_key == "allowed_languages":
                allowed.append(line[1:].strip())
        return {"allowed_languages": [s.lower() for s in allowed], "aliases": aliases}
    data = yaml.safe_load(text) or {}
    allowed = [s.lower() for s in data.get("allowed_languages", [])]
    aliases = data.get("aliases", {}) or {}
    aliases = {k.lower(): [a.lower() for a in v] for k, v in aliases.items()}
    return {"allowed_languages": allowed, "aliases": aliases}


def extract_code_blocks(md: str):
    blocks = []
    for m in FENCED_BLOCK_RE.finditer(md):
        lang = (m.group("lang") or "").strip() or None
        code = m.group("code")
        blocks.append({"language": lang, "code": code})
    return blocks


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1)


def first_nonempty_word(code: str):
    for line in code.splitlines():
        s = line.strip()
        if s:
            return s.split()[0]
    return None


def canonicalize_language(lang, allowed, alias_map):
    if lang is None:
        return None, False
    l = lang.lower()
    if l in allowed:
        return l, True
    for canonical, aliases in alias_map.items():
        if l == canonical or l in aliases:
            return canonical, canonical in allowed
    return l, False


def audit_directory(root: Path, config: dict, include_unlabeled: bool = True):
    allowed = set(config.get("allowed_languages", []))
    alias_map = config.get("aliases", {}) or {}

    disallowed_blocks = []
    unlabeled_blocks = []
    first_word_to_files = defaultdict(set)

    for f in root.glob("**/*.md"):
        try:
            text = f.read_text(encoding="utf-8")
        except Exception:
            continue
        text = strip_frontmatter(text)
        blocks = extract_code_blocks(text)
        for block in blocks:
            lang = block["language"]
            canon, ok = canonicalize_language(lang, allowed, alias_map)
            if lang is None and include_unlabeled:
                fw = first_nonempty_word(block["code"]) or ""
                unlabeled_blocks.append((f, fw))
                if fw:
                    first_word_to_files[fw].add(str(f))
                continue
            if not ok:
                fw = first_nonempty_word(block["code"]) or ""
                disallowed_blocks.append((f, lang, fw))
                if fw:
                    first_word_to_files[fw].add(str(f))

    disallowed_counter = Counter([(lang or "None") for _, lang, _ in disallowed_blocks])
    unlabeled_counter = Counter([fw or "" for _, fw in unlabeled_blocks if fw])

    return {
        "disallowed_blocks": disallowed_blocks,
        "unlabeled_blocks": unlabeled_blocks,
        "disallowed_counter": disallowed_counter,
        "unlabeled_counter": unlabeled_counter,
        "first_word_to_files": first_word_to_files,
    }


def format_report(results, show_files: bool = False) -> str:
    lines = []
    disallowed = results["disallowed_counter"]
    unlabeled = results["unlabeled_counter"]

    lines.append("hljs-audit report")
    lines.append("================")
    lines.append("")

    total_disallowed = sum(disallowed.values())
    total_unlabeled = sum(unlabeled.values())

    lines.append(f"Disallowed language blocks: {total_disallowed}")
    if disallowed:
        for lang, count in disallowed.most_common():
            lines.append(f"  - {lang}: {count}")
    else:
        lines.append("  - none")
    lines.append("")

    lines.append(f"Unlabeled fenced code blocks: {total_unlabeled}")
    if unlabeled:
        for word, count in unlabeled.most_common(20):
            lines.append(f"  - starts with '{word}': {count}")
    else:
        lines.append("  - none")
    lines.append("")

    if show_files and (results["disallowed_blocks"] or results["unlabeled_blocks"]):
        lines.append("Examples and file references:")
        fw_files = results["first_word_to_files"]
        for fw, files in list(fw_files.items())[:20]:
            file_list = ", ".join(sorted(files)[:5])
            lines.append(f"  - '{fw}' -> {file_list}")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        prog="hljs-audit",
        description="Audit Markdown fenced code blocks against allowed Highlight.js languages.",
    )
    parser.add_argument(
        "path",
        nargs="?",
        default="content",
        help="Root directory to scan (default: content)",
    )
    parser.add_argument(
        "-c",
        "--config",
        default="config.yaml",
        help="Path to YAML config (default: config.yaml)",
    )
    parser.add_argument(
        "--no-unlabeled",
        action="store_true",
        help="Ignore unlabeled fenced code blocks",
    )
    parser.add_argument(
        "--show-files", action="store_true", help="Include example file paths in report"
    )
    parser.add_argument(
        "--warn-only", action="store_true", help="Always exit 0 (print warnings only)"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat unlabeled blocks as errors (affects exit code)",
    )
    args = parser.parse_args()

    root = Path(args.path)
    config_path = Path(args.config)

    try:
        config = read_config(config_path)
    except Exception as e:
        print(f"[hljs-audit] ERROR: {e}", file=sys.stderr)
        sys.exit(2)

    results = audit_directory(root, config, include_unlabeled=not args.no_unlabeled)
    report = format_report(results, show_files=args.show_files)
    print(report)

    exit_code = 0
    has_disallowed = sum(results["disallowed_counter"].values()) > 0
    has_unlabeled = sum(results["unlabeled_counter"].values()) > 0
    if not args.warn_only:
        if has_disallowed or (args.strict and has_unlabeled):
            exit_code = 1
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
