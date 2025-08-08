#!/bin/sh
# Verify documentation integrity within container

set -e

cd /docs

echo "=== Container Documentation Verification ==="
echo

# Check file integrity
echo "[INFO] Checking file integrity..."
if sha256sum -c checksums.sha256 > /dev/null 2>&1; then
    echo "[PASS] All files match expected checksums"
else
    echo "[FAIL] File integrity check failed"
    exit 1
fi

# Display file information
echo
echo "[INFO] Documentation bundle details:"
echo "  File: chainguard-complete-docs.md"
echo "  Size: $(stat -c%s chainguard-complete-docs.md 2>/dev/null || stat -f%z chainguard-complete-docs.md) bytes"
echo "  SHA256: $(sha256sum chainguard-complete-docs.md | cut -d' ' -f1)"

echo
echo "[PASS] Container verification complete"
echo "[INFO] Documentation is ready for extraction"