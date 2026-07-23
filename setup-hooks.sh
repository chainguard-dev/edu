#!/bin/bash
# Enable local commit checks for this clone.
#
# This points git at the repo's .githooks/ directory, whose pre-commit hook
# stamps date/lastmod on content files and then runs the pre-commit framework
# (.pre-commit-config.yaml) for linting, secret scanning, tag validation, spell
# checking, and SCSS/stylelint. One hook runs everything, so there is no need to
# run `pre-commit install` -- git ignores .git/hooks once core.hooksPath is set.

echo "Setting up git hooks..."

# Point git at the version-controlled hooks directory.
git config core.hooksPath .githooks

echo "✅ Git hooks enabled!"
echo ""
echo "On each commit, the pre-commit hook will now:"
echo "  • Stamp date/lastmod on new and edited content files"
echo "  • Run the pre-commit framework (lint, secrets, tags, spell check, SCSS)"
echo ""
echo "Install the pre-commit framework so its checks run locally (they are also"
echo "a required check on pull requests):"
echo "  brew install pre-commit   # or: pipx install pre-commit"
echo ""
echo "Optional, for local prose spell checking:"
echo "  brew install aspell       # or your system's package manager"
echo ""
echo "To skip the hook for a single commit, use:"
echo "  git commit --no-verify"
echo ""
echo "To disable the hook permanently, use:"
echo "  git config --unset core.hooksPath"
