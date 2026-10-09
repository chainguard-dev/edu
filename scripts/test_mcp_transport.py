#!/usr/bin/env python3
"""Regression coverage for the docs MCP server's HTTP transport.

These tests send real HTTP requests to the app that production serves, built
by build_http_app() in mcp-server.py, and guard three settings:

- Stateless (CUS-1340). The hosted server runs several Cloud Run instances
  behind a global load balancer with no session affinity. A stateful transport
  keys each session to the instance that handled `initialize`, so a follow-up
  request landing on another instance was rejected with 404 "Session not
  found". A stateless server mints no Mcp-Session-Id.
- JSON responses. Each POST reply is a single application/json body, not a
  one-shot text/event-stream.
- No SSE stream (EXP-577). In stateless mode the SDK accepts GET /mcp and
  holds an empty stream open until Cloud Run's 300-second request timeout,
  holding one of the service's request slots the whole time. Enough of those
  filled every slot, and Cloud Run returned 429 to all callers. The server
  must answer GET with 405 instead.

TestClient is used as a context manager so it runs the app's lifespan, which
starts the SDK's session manager; without it every POST fails with 500.

Run with:
    pytest scripts/test_mcp_transport.py -v
"""

import importlib.util
import os
from pathlib import Path

import pytest
from starlette.testclient import TestClient


def load_server_module():
    """Import scripts/mcp-server.py, whose filename is not a valid module name.

    The module indexes DOCS_PATH at import time. Point it at paths that do not
    exist so the import stays cheap; these tests need no documentation content.
    """
    os.environ["DOCS_PATH"] = "/nonexistent/docs.md"
    os.environ["CATALOG_PATH"] = "/nonexistent/catalog.json"

    spec = importlib.util.spec_from_file_location(
        "mcp_server_transport_under_test", Path(__file__).parent / "mcp-server.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


mcp_server = load_server_module()

# The Envoy AI Gateway sends this protocol version, and clients on any 2025
# version reach the SDK path that opened the stream.
PROTOCOL_VERSION = "2025-06-18"

POST_HEADERS = {
    "Accept": "application/json, text/event-stream",
    "Content-Type": "application/json",
}

INITIALIZE = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": PROTOCOL_VERSION,
        "capabilities": {},
        "clientInfo": {"name": "transport-test", "version": "0"},
    },
}


@pytest.fixture(scope="module")
def client():
    # Nothing binds here. The test passes production's host so the SDK picks
    # the same transport-security settings; a localhost host would turn on DNS
    # rebinding protection, which production doesn't run with.
    with TestClient(mcp_server.build_http_app("0.0.0.0")) as test_client:  # nosec B104
        yield test_client


@pytest.mark.parametrize(
    "headers",
    [
        {"Accept": "text/event-stream", "MCP-Protocol-Version": PROTOCOL_VERSION},
        {"Accept": "text/event-stream"},
    ],
    ids=["with-protocol-version", "without-protocol-version"],
)
# If the 405 route regresses, the GET opens a stream that never ends and
# TestClient waits forever for its body. The timeout (pytest-timeout) turns
# that hang into a failure.
@pytest.mark.timeout(10)
def test_get_is_refused_with_405(client, headers):
    """GET /mcp must not open an SSE stream (EXP-577)."""
    response = client.get("/mcp", headers=headers)
    assert response.status_code == 405
    assert response.headers["allow"] == "POST"


def test_initialize_is_stateless_and_json(client):
    """POST initialize still works, mints no session, and replies in JSON."""
    response = client.post("/mcp", headers=POST_HEADERS, json=INITIALIZE)
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")
    # A JSON-RPC error also comes back as HTTP 200, so check for a result
    # before trusting the absent session id.
    assert "result" in response.json()
    assert "mcp-session-id" not in response.headers, (
        "stateless mode expected but the server minted an Mcp-Session-Id "
        "(CUS-1340): stateful sessions break across unaffinitized Cloud Run "
        "instances"
    )


def test_tools_list_works_without_a_session(client):
    """A follow-up request needs no session, so any instance can serve it."""
    response = client.post(
        "/mcp",
        headers={**POST_HEADERS, "MCP-Protocol-Version": PROTOCOL_VERSION},
        json={"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
    )
    assert response.status_code == 200
    assert response.json()["result"]["tools"]
