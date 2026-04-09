#!/bin/sh
# Start MCP server in HTTP mode for remote/hosted access

set -e

echo "=== Chainguard AI Documentation MCP Server (HTTP) ===" >&2
echo >&2
echo "Starting MCP server in HTTP mode on port ${MCP_PORT:-8080}..." >&2
echo >&2
echo "Clients can connect using the Streamable HTTP transport at:" >&2
echo "  http://<host>:${MCP_PORT:-8080}/mcp" >&2
echo >&2

# Run the MCP server in HTTP mode
exec python3 /usr/local/bin/mcp-server.py --transport http
