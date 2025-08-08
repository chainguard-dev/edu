#!/bin/sh
# Verify documentation integrity within container

set -e

cd /docs

echo "=== Container Documentation Verification ==="
echo

# Check file integrity
echo "[INFO] Checking file integrity..."
if sha256sum -c checksums.txt > /dev/null 2>&1; then
    echo "[PASS] All files match expected checksums"
else
    echo "[FAIL] File integrity check failed"
    exit 1
fi

# Display file information
echo
echo "[INFO] Documentation bundle details:"
echo "  File: chainguard-ai-docs.md"
echo "  Size: $(stat -c %s chainguard-ai-docs.md 2>/dev/null || wc -c < chainguard-ai-docs.md | tr -d ' ') bytes"
echo "  SHA256: $(sha256sum chainguard-ai-docs.md | cut -d' ' -f1)"

echo
echo "[PASS] Container verification complete"
echo "[INFO] Documentation is ready for extraction"