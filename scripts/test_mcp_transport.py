#!/usr/bin/env python3
"""Regression coverage for the docs MCP server's HTTP transport (CUS-1340).

The hosted server runs several Cloud Run instances behind a global load
balancer with no session affinity. A stateful streamable-HTTP transport keys
each session to the instance that handled `initialize`, so a follow-up request
(for example `notifications/initialized`) landing on another instance was
rejected with 404 "Session not found". Running the transport with
`stateless_http=True` makes every request self-contained, which is safe here
because the docs tools are read-only and the server sends no server-initiated
notifications.

This asserts the production invocation keeps that flag. It reads the source
rather than importing, because the `server.run(...)` call lives under
`if __name__ == "__main__"` and would block on uvicorn if executed.

Run with:
    pytest scripts/test_mcp_transport.py -v
"""

import ast
from pathlib import Path

SERVER = Path(__file__).parent / "mcp-server.py"


def streamable_http_run_calls(tree):
    """Every `.run(transport="streamable-http", ...)` call in the module."""
    calls = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        transport = next(
            (kw.value for kw in node.keywords if kw.arg == "transport"), None
        )
        if isinstance(transport, ast.Constant) and transport.value == "streamable-http":
            calls.append(node)
    return calls


def test_http_transport_runs_stateless():
    """The streamable-HTTP server must run stateless, or CUS-1340 regresses."""
    tree = ast.parse(SERVER.read_text(encoding="utf-8"))
    calls = streamable_http_run_calls(tree)
    assert calls, "expected a streamable-http server.run() call"
    for call in calls:
        flag = next(
            (kw.value for kw in call.keywords if kw.arg == "stateless_http"), None
        )
        assert flag is not None, (
            "stateless_http kwarg missing from the streamable-http run() call "
            "(CUS-1340): stateful sessions break across unaffinitized Cloud "
            "Run instances"
        )
        assert isinstance(flag, ast.Constant) and flag.value is True, (
            "stateless_http must be the literal True, not a falsy or non-True "
            "value (CUS-1340)"
        )
