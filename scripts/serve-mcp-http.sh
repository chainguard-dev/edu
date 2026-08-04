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

# Trust the Cloud Run front end's forwarded headers so uvicorn honors
# X-Forwarded-Proto and keeps redirects (for example, the /mcp/ -> /mcp
# trailing-slash redirect) on https instead of downgrading to http. Safe here:
# the container is only reachable through Cloud Run's front end. See DOCS-99.
export FORWARDED_ALLOW_IPS="${FORWARDED_ALLOW_IPS:-*}"

# Run the MCP server in HTTP mode
exec python3 /usr/local/bin/mcp-server.py --transport http
