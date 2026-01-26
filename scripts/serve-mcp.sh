#!/bin/sh
# Start MCP server for Chainguard AI documentation

set -e

# All output must go to stderr - MCP uses stdout for JSON-RPC communication
echo "=== Chainguard AI Documentation MCP Server ===" >&2
echo >&2
echo "Starting MCP server..." >&2
echo "Documentation loaded from: /docs/chainguard-ai-docs.md" >&2
echo >&2
echo "To connect this server to Claude Desktop, add this configuration:" >&2
echo >&2
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
}' >&2
echo >&2
echo "Server is ready and listening..." >&2
echo >&2

# Run the MCP server
exec python3 /usr/local/bin/mcp-server.py
