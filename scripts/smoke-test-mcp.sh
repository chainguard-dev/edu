#!/bin/sh
# Smoke-test the AI-docs MCP server image before it is allowed to deploy.
#
# Boots the freshly built container the same way Cloud Run does
# (serve-mcp-http) and confirms the MCP server starts and serves HTTP on its
# port. This catches the failure that took the server down on 2026-07-29: an
# incompatible mcp SDK crashed the process at startup, so it never bound the
# port and every deploy failed Cloud Run's health check (DOCS-91).
#
# Usage: scripts/smoke-test-mcp.sh <image-ref>

set -eu

IMAGE="${1:?usage: smoke-test-mcp.sh <image-ref>}"
HOST_PORT="${HOST_PORT:-18080}"   # host side; the container always listens on 8080
CONTAINER_PORT=8080
TIMEOUT="${TIMEOUT:-30}"          # seconds to wait for the server to respond

# --- Check 1: the module imports and registers its tools --------------------
# `--help` forces mcp-server.py to import, which runs the tool-registration
# decorators at module load. A breaking SDK change fails here immediately,
# before any networking is involved.
echo "Check 1: module import + tool registration"
docker run --rm --entrypoint python3 "$IMAGE" /usr/local/bin/mcp-server.py --help >/dev/null
echo "  OK"

# --- Check 2: the HTTP transport starts and binds the port ------------------
echo "Check 2: HTTP transport boots and serves on :$CONTAINER_PORT"
CID=$(docker run -d -p "127.0.0.1:$HOST_PORT:$CONTAINER_PORT" "$IMAGE" /usr/local/bin/serve-mcp-http)
trap 'docker rm -f "$CID" >/dev/null 2>&1 || true' EXIT

fail() {
    echo "  FAIL: $1" >&2
    echo "  --- container logs ---" >&2
    docker logs "$CID" 2>&1 | sed 's/^/    /' >&2 || true
    exit 1
}

# Poll until the server answers on /mcp, or give up after TIMEOUT seconds.
ready=""
i=0
while [ "$i" -lt "$TIMEOUT" ]; do
    # curl exits 0 as soon as it gets any HTTP response (a redirect counts);
    # a non-zero exit means the port is not accepting connections yet.
    if curl -s -o /dev/null "http://127.0.0.1:$HOST_PORT/mcp"; then
        [ "$(docker inspect -f '{{.State.Running}}' "$CID")" = "true" ] \
            || fail "server responded but the container is no longer running"
        echo "  OK: server responded on /mcp"
        ready=1
        break
    fi
    i=$((i + 1))
    sleep 1
done

[ -n "$ready" ] || fail "server did not serve on :$CONTAINER_PORT within ${TIMEOUT}s"

# --- Check 3: the transport runs stateless (CUS-1340) -----------------------
# A stateful transport mints an Mcp-Session-Id on initialize; behind the
# affinity-free Cloud Run load balancer that fronts this service, that is what
# caused the cross-instance 404s this image fixes. The unit test guards the
# source kwarg, but only this check proves the running server is actually
# stateless: if a future SDK silently ignores stateless_http, the source stays
# green while behavior regresses here.
echo "Check 3: transport is stateless (no Mcp-Session-Id minted)"
init='{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"smoke","version":"0"}}}'
headers=$(curl -s -D - -o /dev/null -X POST \
    -H "Content-Type: application/json" \
    -H "Accept: application/json, text/event-stream" \
    -d "$init" "http://127.0.0.1:$HOST_PORT/mcp") || fail "initialize request failed"
if printf '%s' "$headers" | grep -qi '^mcp-session-id:'; then
    fail "stateless mode expected but server minted an Mcp-Session-Id (CUS-1340)"
fi
echo "  OK: no Mcp-Session-Id"
