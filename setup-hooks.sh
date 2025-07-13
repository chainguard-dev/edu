#!/bin/bash
# Setup script to enable custom git hooks

echo "Setting up git hooks..."

# Check if aspell is installed
if ! command -v aspell &> /dev/null; then
    echo "⚠️  Warning: aspell is not installed. Spell checking will be skipped."
    echo "   To enable spell checking, install aspell:"
    echo "     macOS:           brew install aspell"
    echo "     Ubuntu/Debian:   sudo apt install aspell"
    echo "     RHEL/CentOS:     sudo yum install aspell"
    echo "     Alpine:          apk add aspell"
    echo "     Arch:            sudo pacman -S aspell"
    echo ""
fi

# Configure git to use the .githooks directory
git config core.hooksPath .githooks

echo "✅ Git hooks enabled!"
echo ""
echo "The pre-commit hook will now:"
echo "  • Validate tags against approved list"
echo "  • Check for spelling errors (if aspell is installed)"
echo ""
echo "To disable hooks temporarily, use:"
echo "  git commit --no-verify"
echo ""
echo "To disable hooks permanently, use:"
echo "  git config --unset core.hooksPath"
echo ""
echo "Custom dictionary for technical terms: .aspell.en.pws"