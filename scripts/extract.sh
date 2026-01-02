#!/bin/sh
# Extract verified documentation to specified directory

set -e

if [ -z "$1" ]; then
    echo "Usage: docker run --rm -v \$(pwd):/output cgr.dev/chainguard/ai-docs:latest extract /output"
    exit 1
fi

OUTPUT_DIR="$1/chainguard-ai-docs"

# Verify first
/usr/local/bin/verify || exit 1

echo
echo "[INFO] Extracting verified documentation to $OUTPUT_DIR"

# Create subdirectory
mkdir -p "$OUTPUT_DIR"

# Copy files
cp /docs/chainguard-ai-docs.md "$OUTPUT_DIR/"
cp /docs/checksums.txt "$OUTPUT_DIR/"
cp /docs/verification.sh "$OUTPUT_DIR/"

echo "[PASS] Documentation extracted successfully"
echo
echo "Files extracted to: $OUTPUT_DIR"
echo "  - chainguard-ai-docs.md (main documentation)"
echo "  - checksums.txt (file checksums)"
echo "  - verification.sh (verification script)"