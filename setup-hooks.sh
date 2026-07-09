#!/bin/bash
# Enable the native git hook that stamps date/lastmod on content files.
#
# Tag validation and spell checking now run via the pre-commit framework
# (see .pre-commit-config.yaml and the README "Pre-commit" section), not here.

echo "Setting up git hooks..."

# Configure git to use the .githooks directory
git config core.hooksPath .githooks

echo "✅ Git hooks enabled!"
echo ""
echo "The pre-commit git hook will now:"
echo "  • Add date/lastmod to new content files and refresh lastmod on edits"
echo ""
echo "Tag validation and spell checking are handled by the pre-commit framework."
echo "Install it and enable its hooks with:"
echo "  brew install pre-commit   # or: pipx install pre-commit"
echo "  pre-commit install"
echo ""
echo "To disable git hooks temporarily, use:"
echo "  git commit --no-verify"
echo ""
echo "To disable git hooks permanently, use:"
echo "  git config --unset core.hooksPath"
