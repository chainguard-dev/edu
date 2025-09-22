# hljs-audit

Audit fenced code blocks in Markdown against a configured list of **Highlight.js** languages.

## What it does

- Scans `*.md` under a directory (default: `content`)
- Extracts fenced code blocks (```...```)
- Checks the language label against an **allowed** list from `config.yaml`
- Reports:
  - Disallowed/unknown languages
  - Unlabeled code fences (optional)
  - Top first-words to help spot command snippets (useful triage)

## Quick start

```bash
# optional: install dependency if you plan to use YAML features beyond the fallback parser
pip install pyyaml

# run (from repo root or wherever your markdown lives)
./hljs_audit.py               # scans ./content using ./config.yaml
./hljs_audit.py docs -c config.yaml --show-files
```

## Exit codes:

0 = clean (or warnings only)
1 = issues found (disallowed languages, and optionally unlabeled if --strict)
2 = configuration error (e.g., missing config.yaml)

Pipe output to a file for human review or keep non-zero exit for CI:

```bash
./hljs_audit.py > audit.txt                # human review
./hljs_audit.py --strict || echo "Fix issues before merge"
```

## Configuration

`config.yaml` should define at least:

```yaml
allowed_languages:
  - bash
  - json
  - yaml
  # ...

# Optional alias map, canonical -> list of synonyms
aliases:
  javascript: [js, node]
  bash: [sh, zsh, shell]
```

- All matching is lowercase.
- If a block language matches a canonical or any of its aliases, it is accepted.
- Unlabeled code fences are reported by default (disable via `--no-unlabeled`).

## CLI

```
usage: hljs-audit [-h] [-c CONFIG] [--no-unlabeled] [--show-files]
                  [--warn-only] [--strict]
                  [path]

positional arguments:
  path                  Root directory to scan (default: content)

options:
  -h, --help            Show this help message and exit
  -c, --config          Path to YAML config (default: config.yaml)
  --no-unlabeled        Ignore unlabeled fenced code blocks
  --show-files          Include example file paths in the report
  --warn-only           Always exit 0 (print warnings only)
  --strict              Treat unlabeled blocks as errors (affects exit code)
```

## Notes

- Frontmatter (--- ... ---) is stripped before scanning.
- The regex handles triple+ backtick fences and matches closing fence length.
- For best results, keep allowed_languages synced to your core Highlight.js build.
- If you want, replace config.yaml with your authoritative list and commit it.
- If you don’t want to install PyYAML, the tool falls back to a minimal parser that only reads the allowed_languages list.
