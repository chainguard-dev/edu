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
TIMEOUT="${TIMEOUT:-30}"          # max readiness-poll attempts (each failed
                                  # attempt costs up to ~6s: --max-time 5 + 1s sleep)

# --- Check 1: the module imports and registers its tools --------------------
# `--help` forces mcp-server.py to import, which runs the tool-registration
# decorators at module load. A breaking SDK change fails here immediately,
# before any networking is involved.
echo "Check 1: module import + tool registration"
docker run --rm --entrypoint python3 "$IMAGE" /usr/local/bin/mcp-server.py --help >/dev/null
echo "  OK"

# --- Check 2: the HTTP transport starts and binds the port ------------------
echo "Check 2: HTTP transport boots and answers MCP initialize on :$CONTAINER_PORT"
CID=$(docker run -d -p "127.0.0.1:$HOST_PORT:$CONTAINER_PORT" "$IMAGE" /usr/local/bin/serve-mcp-http)
trap 'docker rm -f "$CID" >/dev/null 2>&1 || true' EXIT

fail() {
    echo "  FAIL: $1" >&2
    echo "  --- container logs ---" >&2
    docker logs "$CID" 2>&1 | sed 's/^/    /' >&2 || true
    exit 1
}

# The MCP initialize request, reused as both the liveness probe and the
# stateless assertion below. It is a POST because POST /mcp is a
# request-response cycle in every transport mode. GET /mcp returns 405 (Check 5),
# but before that fix it opened an SSE stream that never closed. --max-time
# bounds any unexpected stall; callers pass -f so a non-2xx response is a
# failure, not a vacuous pass.
INIT_BODY='{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"smoke","version":"0"}}}'

post_init() {  # extra curl args in "$@"
    curl -s --max-time 5 \
        -H "Content-Type: application/json" \
        -H "Accept: application/json, text/event-stream" \
        -X POST -d "$INIT_BODY" "$@" "http://127.0.0.1:$HOST_PORT/mcp"
}

# Poll until initialize returns 2xx, or give up after TIMEOUT attempts. Each
# failed attempt costs up to ~6s (curl --max-time 5 + the 1s sleep below), so
# the default 30 attempts is ~180s worst case, not 30s. A connection error (the
# server has not bound the port yet) keeps the loop waiting; -f treats an HTTP
# error as not-ready-yet too.
ready=""
i=0
while [ "$i" -lt "$TIMEOUT" ]; do
    if post_init -f -o /dev/null; then
        [ "$(docker inspect -f '{{.State.Running}}' "$CID")" = "true" ] \
            || fail "server responded but the container is no longer running"
        echo "  OK: initialize returned 2xx"
        ready=1
        break
    fi
    i=$((i + 1))
    sleep 1
done

[ -n "$ready" ] || fail "server did not serve a 2xx initialize on :$CONTAINER_PORT within ${TIMEOUT} attempts"

# --- Check 3: the transport runs stateless (CUS-1340) -----------------------
# A stateful transport mints an Mcp-Session-Id on initialize; behind the
# affinity-free Cloud Run load balancer that fronts this service, that is what
# caused the cross-instance 404s this image fixes. The unit test guards the
# source kwarg, but only this check proves the running server is actually
# stateless.
#
# -f rejects an HTTP-level error (4xx/5xx), but a JSON-RPC error (e.g. a
# rejected protocolVersion) comes back as HTTP 200 with an {"error":...} body
# and no Mcp-Session-Id — which would pass the header check vacuously. So assert
# the response actually carries a "result" before trusting the absent session
# id. -D - dumps the response headers ahead of the body, so one capture covers
# both assertions.
echo "Check 3: transport is stateless (no Mcp-Session-Id minted)"
response=$(post_init -f -D -) \
    || fail "initialize did not return 2xx (check protocol version and container logs)"
printf '%s' "$response" | grep -q '"result"' \
    || fail "initialize returned 200 but no JSON-RPC result (check protocol version and container logs)"
if printf '%s' "$response" | grep -qi '^mcp-session-id:'; then
    fail "stateless mode expected but server minted an Mcp-Session-Id (CUS-1340)"
fi
echo "  OK: initialize succeeded, no Mcp-Session-Id"

# --- Check 4: POST replies are single JSON, not SSE (json_response) ----------
# json_response=True returns each POST reply as one application/json body rather
# than a one-shot text/event-stream. Reuse the captured initialize response (its
# headers are in $response via -D -) so a regression of that kwarg is caught
# alongside the stateless one.
echo "Check 4: POST transport returns application/json (json_response)"
if printf '%s' "$response" | grep -qi '^content-type:[[:space:]]*application/json'; then
    echo "  OK: Content-Type is application/json"
else
    fail "expected an application/json POST reply but the Content-Type differs (json_response regressed?)"
fi

# --- Check 5: GET /mcp is refused, not held open as a stream (EXP-577) -------
# In stateless mode the SDK accepted GET /mcp and held an empty SSE stream open
# until Cloud Run's request timeout, holding a request slot the whole time.
# Enough of those filled every slot and Cloud Run returned 429 to all callers.
# The server must answer 405. A 200 here means the stream is back; curl's
# --max-time ends it, and -w still reports the status. `|| true` keeps set -e
# from exiting on that timeout before fail() can report it.
echo "Check 5: GET /mcp returns 405 (no SSE stream)"
status=$(curl -s --max-time 5 -o /dev/null -w '%{http_code}' \
    -H "Accept: text/event-stream" \
    -H "MCP-Protocol-Version: 2025-06-18" \
    "http://127.0.0.1:$HOST_PORT/mcp") || true
[ "$status" = "405" ] \
    || fail "GET /mcp returned $status, expected 405 (a 200 means the server opened an SSE stream: EXP-577)"
echo "  OK: GET /mcp returned 405"
