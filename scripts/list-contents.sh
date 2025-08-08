#!/bin/sh
# List contents and usage information

echo "=== Chainguard AI Documentation Container ==="
echo
echo "This container provides cryptographically signed Chainguard documentation"
echo "optimized for AI coding assistants."
echo
echo "Contents:"
echo "  - chainguard-complete-docs.md (Main documentation bundle)"
echo "  - checksums.sha256 (File checksums)"
echo "  - verification.sh (Verification script)"
echo "  - Cosign signatures and certificates"
echo
echo "Usage:"
echo
echo "  1. Verify contents:"
echo "     docker run --rm cgr.dev/chainguard/ai-docs:latest verify"
echo
echo "  2. Extract to current directory:"
echo "     docker run --rm -v \$(pwd):/output cgr.dev/chainguard/ai-docs:latest extract /output"
echo
echo "  3. View this help:"
echo "     docker run --rm cgr.dev/chainguard/ai-docs:latest"
echo
echo "Security:"
echo "  - Container is signed with cosign"
echo "  - Documentation is individually signed"
echo "  - All files have SHA-256 checksums"
echo "  - Built on Chainguard static base image"