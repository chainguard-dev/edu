# Pre-commit Hook Guide for Contributors

This guide explains the automated checks that run on your content before it merges.

## How local checks run

One git hook (`.githooks/pre-commit`, enabled by `./setup-hooks.sh`) runs on
every commit and does two things:

1. **Stamps content dates.** It adds `date` and `lastmod` to new content files
   and refreshes `lastmod` on edited ones, then re-stages the file into your
   commit. This stays a native git hook because the pre-commit framework doesn't
   re-stage files, and a "now" timestamp would never pass a CI idempotency check.
2. **Runs the [pre-commit](https://pre-commit.com/) framework**
   (`.pre-commit-config.yaml`) for linting, secret scanning, tag validation,
   spell checking, and SCSS/stylelint. The same framework runs as a **required**
   check on pull requests, where it lints only the files a pull request changes.

Because `./setup-hooks.sh` sets `core.hooksPath=.githooks`, git runs this hook
and ignores anything in `.git/hooks`. You don't run `pre-commit install`: the
hook calls the framework for you, so one setup covers everything.

## What gets checked

### Content date stamping (git hook step)

- **New files**: Adds `date` and `lastmod` fields with the current timestamp
- **Modified files**: Refreshes the `lastmod` field
- **Format**: ISO 8601 with UTC timezone, for example `2025-01-16T10:30:45+00:00`
- You don't add or update these fields yourself

### Linting and security (pre-commit framework)

These fail the commit, and the required CI check, when they find a problem:

- **Code and content linting**: JavaScript (`eslint`), Markdown (`markdownlint`), SCSS (`stylelint`), and Python (`bandit`, `black`)
- **Security and hygiene**: secret scanning (`gitleaks`), private-key detection, large-file checks, and whitespace, end-of-file, and line-ending fixes
- **GitHub Actions**: workflow security (`zizmor`) and linting (`actionlint`)

Each linter reads the repository's own configuration, for example
`.stylelintrc.json` for SCSS and `.markdownlint-cli2.jsonc` for Markdown.

### Tag validation (pre-commit framework, advisory)

- Checks that tags match the approved taxonomy, stay within five per article, and use the expected capitalization
- Reports problems as warnings but never blocks a commit

### Spelling (pre-commit framework, advisory and local-only)

- Catches typos and misspellings; reports but never blocks a commit
- Runs locally only; the CI check skips it (`SKIP=content-spellcheck`)
- Ignores code blocks, Hugo shortcodes (for example `{{< youtube >}}`), inline code, and URLs
- Uses a custom dictionary for technical terms (`.aspell.en.pws`)

## Setting up

Do this once per clone:

1. **Install the pre-commit framework:**

   ```bash
   brew install pre-commit        # or: pipx install pre-commit
   ```

2. **Enable the git hook:**

   ```bash
   ./setup-hooks.sh
   ```

3. **Optional: install aspell** so the local spell check runs:

   ```bash
   # macOS
   brew install aspell

   # Ubuntu/Debian
   sudo apt install aspell

   # RHEL/CentOS/Fedora
   sudo dnf install aspell

   # Alpine Linux
   apk add aspell

   # Arch Linux
   sudo pacman -S aspell
   ```

Every commit now stamps content dates and runs the framework checks. If you
commit before installing the `pre-commit` framework, the hook still stamps dates
and prints a reminder to install it.

## Understanding the output

When you run `git commit`, the hook prints its date-stamp result first, then the
pre-commit framework's per-hook results.

### A passing commit

```text
📅 Updated lastmod on 1 file(s):
   - content/chainguard/chainguard-images/getting-started.md
trim trailing whitespace.................................................Passed
fix end of files.........................................................Passed
Detect hardcoded secrets.................................................Passed
markdownlint-cli2........................................................Passed
Validate content tags....................................................Passed
```

### A blocked commit

A blocking hook (a linter, a secret scan, or a file-hygiene check) prints the
failure and stops the commit. Fix the reported issue, stage the change, and
commit again:

```text
markdownlint-cli2........................................................Failed
- hook id: markdownlint-cli2
- exit code: 1

content/chainguard/tutorial.md:14 MD012/no-multiple-blanks Multiple consecutive blank lines
```

Some hooks fix the file for you (for example, trailing-whitespace and
end-of-file-fixer) and then fail so you can review and re-stage the change.

### Advisory warnings

Tag and spelling checks print warnings but don't stop the commit:

```text
Validate content tags....................................................Passed
   ⚠️  Tag not in approved list: 'NewTag'
```

## Common Scenarios

### Adding a New Article

When creating a new article, you no longer need to add date fields manually. Just focus on your content:

**What you write:**

```yaml
---
title: "Getting Started with Chainguard Images"
description: "Learn how to use Chainguard's secure container images"
tags: ["Chainguard Containers", "Getting Started", "Overview"]
---
```

**What gets committed (automatically):**

```yaml
---
title: "Getting Started with Chainguard Images"
date: 2025-01-16T10:30:45+00:00
lastmod: 2025-01-16T10:30:45+00:00
description: "Learn how to use Chainguard's secure container images"
tags: ["Chainguard Containers", "Getting Started", "Overview"]
---
```

### Updating an Existing Article

When you modify an article, the `lastmod` field is automatically updated:

**Before your edit:**

```yaml
---
title: "Security Best Practices"
date: 2024-12-01T09:00:00+00:00
lastmod: 2024-12-15T14:30:00+00:00
---
```

**After commit (automatic update):**

```yaml
---
title: "Security Best Practices"
date: 2024-12-01T09:00:00+00:00
lastmod: 2025-01-16T10:45:30+00:00
---
```

### Fixing tag warnings

If you see a tag warning, update your frontmatter so the tag matches the approved taxonomy:

```yaml
# ❌ Wrong
tags: ["chainguard containers", "OVERVIEW"]

# ✅ Correct
tags: ["Chainguard Containers", "Overview"]
```

### Handling Spelling "Errors"

The spell checker might flag technical terms as errors. You have three options:

1. **Fix actual typos**:
   - `recieve` → `receive`
   - `configuation` → `configuration`

2. **Add technical terms to the dictionary**:
   If you're using a legitimate technical term that's flagged:

   ```bash
   echo "MyTechnicalTerm" >> .aspell.en.pws
   ```

3. **Skip the check** (use sparingly):

   ```bash
   git commit --no-verify -m "Your commit message"
   ```

## Approved Tags Quick Reference

### Most Common Tags

**Product Tags:**

- `Chainguard Containers`
- `Chainguard Libraries`
- `chainctl`

**Content Types:**

- `Overview` - High-level introductions
- `Procedural` - Step-by-step guides
- `Conceptual` - Theory/background
- `Reference` - API/command docs
- `FAQ` - Common questions

**Action Tags:**

- `Getting Started`
- `Migration`
- `Configuration`
- `Troubleshooting`
- `Integration`

**Platform Tags:**

- `AWS`, `GCP`, `Azure`
- `Kubernetes`
- `Docker Hub`
- `GitHub`, `GitLab`

For the complete list, see [TAG_GUIDELINES.md](../TAG_GUIDELINES.md).

## Troubleshooting

### "aspell not installed" Error

Install aspell using your system's package manager:

```bash
# macOS
brew install aspell

# Ubuntu/Debian
sudo apt install aspell

# RHEL/CentOS/Fedora
sudo yum install aspell

# Alpine Linux
apk add aspell

# Arch Linux
sudo pacman -S aspell
```

### Hook Not Running

Make sure hooks are enabled:

```bash
git config core.hooksPath
# Should output: .githooks
```

If not, run:

```bash
./setup-hooks.sh
```

### Need to Temporarily Disable

For urgent commits where you need to bypass the check:

```bash
git commit --no-verify -m "Emergency fix"
```

**Note:** Use this sparingly and fix any issues in a follow-up commit.

### Permanently Disable (Not Recommended)

```bash
git config --unset core.hooksPath
```

## Best Practices

1. **Let automation handle dates**: Never manually add or update `date`/`lastmod` fields - the hook does this for you
2. **Run checks early**: Stage your files and run `git commit` even before writing a message to see if there are issues
3. **Fix issues promptly**: Don't use `--no-verify` as a habit
4. **Keep tags minimal**: Use 3-4 tags that truly describe the content
5. **Review spelling suggestions**: The spell checker helps maintain professional documentation
6. **Use code blocks properly**: Put commands and code in markdown code blocks (```) to avoid spelling false positives

## Questions?

- For tag questions: Review [TAG_GUIDELINES.md](../TAG_GUIDELINES.md)
- For hook issues: Check with the engineering team
- For adding new approved tags: Submit a PR with justification

Remember: The hook is here to help maintain quality and consistency. It catches issues early, saving time in review and ensuring a better experience for our readers!
