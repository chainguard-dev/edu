# Pre-commit Hook Guide for Technical Writers

This guide explains how to use the pre-commit hook that automatically checks your content before committing changes to the repository.

## What is a Pre-commit Hook?

A pre-commit hook is an automated script that runs every time you try to commit changes. It helps maintain consistency and quality by catching common issues before they enter the codebase.

## What Does Our Hook Check?

### 1. Tag Validation
- Ensures all tags match our approved taxonomy
- Checks that you haven't exceeded 5 tags per article
- Verifies proper capitalization (Title Case vs. acronyms)

### 2. Spelling
- Catches typos and misspellings
- Ignores code blocks and URLs
- Uses a custom dictionary for technical terms

## Setting Up the Hook

### One-time Setup

1. **Install aspell** (for spell checking):
   ```bash
   # macOS
   brew install aspell
   
   # Ubuntu/Debian
   sudo apt install aspell
   
   # RHEL/CentOS/Fedora
   sudo yum install aspell
   # or
   sudo dnf install aspell
   
   # Alpine Linux
   apk add aspell
   
   # Arch Linux
   sudo pacman -S aspell
   ```

2. **Enable the git hooks**:
   ```bash
   ./setup-hooks.sh
   ```

That's it! The hook will now run automatically when you commit.

## Understanding the Output

When you run `git commit`, you'll see output like this:

### ✅ Success Case
```
🔍 Running pre-commit checks...

✅ All checks passed!
```

### ⚠️ With Warnings
```
🔍 Running pre-commit checks...

📄 content/chainguard/getting-started.md
   Tags: ["Chainguard Containers", "Overview", "NewTag"]
   ⚠️  Tag not in approved list: 'NewTag'
   📝 Potential spelling errors: recieve, configuation

============================================================
Pre-commit Check Summary:
  Tag Warnings: 1
  Tag Errors: 0
  Files with spelling issues: 1

💡 Consider reviewing TAG_GUIDELINES.md for approved tags

📝 Spelling issues found. Consider:
   - Fixing typos
   - Adding technical terms to your personal dictionary
   - Using 'git commit --no-verify' to skip this check
```

### ❌ With Errors (Blocks Commit)
```
🔍 Running pre-commit checks...

📄 content/chainguard/tutorial.md
   Tags: ["CHAINGUARD", "TUTORIAL"]
   ❌  Tag should use Title Case: 'CHAINGUARD'
   ❌  Tag should use Title Case: 'TUTORIAL'

============================================================
Pre-commit Check Summary:
  Tag Warnings: 0
  Tag Errors: 2
  Files with spelling issues: 0

❌ Commit blocked due to tag errors. Please fix and try again.
```

## Common Scenarios

### Adding a New Article

When creating a new article, make sure your tags follow the guidelines:

```yaml
---
title: "Getting Started with Chainguard Images"
tags: ["Chainguard Containers", "Getting Started", "Overview"]
---
```

### Fixing Tag Errors

If you see a tag error, update your frontmatter:

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

1. **Run checks early**: Stage your files and run `git commit` even before writing a message to see if there are issues
2. **Fix issues promptly**: Don't use `--no-verify` as a habit
3. **Keep tags minimal**: Use 3-4 tags that truly describe the content
4. **Review spelling suggestions**: The spell checker helps maintain professional documentation

## Questions?

- For tag questions: Review [TAG_GUIDELINES.md](../TAG_GUIDELINES.md)
- For hook issues: Check with the engineering team
- For adding new approved tags: Submit a PR with justification

Remember: The hook is here to help maintain quality and consistency. It catches issues early, saving time in review and ensuring a better experience for our readers!