# Instructions for AI agents

These instructions apply to any AI agent working in the Chainguard Academy
docs repository. Codex, Cursor, and GitHub Copilot read this file directly.
Claude Code reads it through `CLAUDE.md`, and Gemini CLI through `GEMINI.md`.

## Writing skills

This repository includes three writing skills in `.agents/skills/`. Claude
Code finds the same skills through symlinks in `.claude/skills/`. Apply them
before you produce any text, without waiting to be asked.

### writing-clearly-and-concisely

Use the `writing-clearly-and-concisely` skill for any prose a human will
read: documentation, pull request descriptions, commit messages, README
files, error messages, and code comments.

### written-style-guide

Use the `written-style-guide` skill for any content a Chainguard audience
will read, including docs, product UI strings, blog posts, and release
notes. It layers Chainguard's voice, tone, and product names on top of
`writing-clearly-and-concisely`, so load both. When reviewing someone's
text, flag issues and suggest fixes rather than rewriting it unless asked.
Its product names and their forms, including capitalization, take
precedence over every other guide.

### google-style

Use the `google-style` skill when you create or edit technical
documentation. It adds the mechanical conventions of technical writing and
complements `writing-clearly-and-concisely`. When it conflicts with
`written-style-guide` on a docs page, follow `google-style`, except for
product names. Where the project's own
[style guide](https://github.com/chainguard-dev/edu/wiki/Style-Guide)
differs from Google's, follow the project guide.

## Contributing conventions

Follow the Contributing section of [README.md](README.md) for page weights,
images, tags, and pre-commit setup. A member of the docs team reviews every
pull request, so flag anything you're unsure of in the pull request
description rather than guessing.
