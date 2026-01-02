#!/bin/sh
# Start MCP server for Chainguard AI documentation

set -e

echo "=== Chainguard AI Documentation MCP Server ==="
echo
echo "Starting MCP server..."
echo "Documentation loaded from: /docs/chainguard-ai-docs.md"
echo
echo "To connect this server to Claude Desktop, add this configuration:"
echo
echo '{
  "mcpServers": {
    "chainguard-docs": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "ghcr.io/chainguard-dev/ai-docs:latest",
        "serve-mcp"
      ]
    }
  }
}'
echo
echo "Server is ready and listening..."
echo

# Run the MCP server
exec python3 /usr/local/bin/mcp-server.py
