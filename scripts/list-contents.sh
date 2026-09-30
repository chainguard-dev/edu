#!/bin/sh
# List contents and usage information

echo "=== Chainguard AI Documentation Container ==="
echo
echo "This container provides Chainguard documentation for AI assistants"
echo "with two distribution modes: static export and MCP server."
echo
echo "Contents:"
echo "  - chainguard-ai-docs.md (Main documentation bundle)"
echo "  - package-mappings.json (dfc package and image mappings)"
echo "  - image-catalog.json (the same file under its earlier name)"
echo "  - MCP server (Model Context Protocol support)"
echo "  - checksums.txt (File checksums)"
echo "  - verification.sh (Verification script)"
echo
echo "Usage Modes:"
echo
echo "  1. Extract documentation (simple use case):"
echo "     docker run --rm -v \$(pwd):/output \\"
echo "       ghcr.io/chainguard-dev/ai-docs:latest extract /output"
echo
echo "  2. Run as MCP server (agent/IDE integration):"
echo "     docker run --rm -i \\"
echo "       ghcr.io/chainguard-dev/ai-docs:latest serve-mcp"
echo
echo "  3. Verify contents:"
echo "     docker run --rm ghcr.io/chainguard-dev/ai-docs:latest verify"
echo
echo "  4. View this help:"
echo "     docker run --rm ghcr.io/chainguard-dev/ai-docs:latest"
echo
echo "MCP Tools Available:"
echo "  - search_docs: Search across all documentation"
echo "  - get_security_docs: Get security and CVE information"
echo "  - get_tool_docs: Get wolfi/apko/melange/chainctl docs"
echo "  - find_package_equivalent: Find Wolfi equivalents for Debian and Fedora packages"
echo "  - find_image_equivalent: Find the Chainguard image that replaces an upstream image"
echo
echo "For live container image data, use the cg-oci MCP server at https://cgr.dev/mcp."
echo
echo "Security:"
echo "  - Container is signed with cosign"
echo "  - Documentation is individually signed"
echo "  - All files have SHA-256 checksums"
echo "  - Built on Chainguard wolfi-base image"
echo "  - Runs as non-root user"
echo
echo "Documentation: https://edu.chainguard.dev/platform/mcp-servers/ai-docs/"
