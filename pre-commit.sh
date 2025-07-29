#!/bin/bash
# Run checks from pre-commit hook

echo "Changed files.."
git diff --name-only
python3 .githooks/pre-commit
