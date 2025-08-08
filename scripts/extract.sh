#!/bin/sh
# Extract verified documentation to specified directory

set -e

if [ -z "$1" ]; then
    echo "Usage: docker run --rm -v \$(pwd):/output cgr.dev/chainguard/ai-docs:latest extract /output"
    exit 1
fi

OUTPUT_DIR="$1"

# Verify first
/usr/local/bin/verify || exit 1

echo
echo "[INFO] Extracting verified documentation to $OUTPUT_DIR"

# Copy files
cp /docs/chainguard-ai-docs.md "$OUTPUT_DIR/"
cp /docs/checksums.txt "$OUTPUT_DIR/"
cp /docs/verification.sh "$OUTPUT_DIR/"

echo "[PASS] Documentation extracted successfully to $OUTPUT_DIR"
echo "[INFO] Run ./verification.sh to verify the extracted files"