---
title: "MCP Server for AI Documentation"
linktitle: "MCP: AI Docs"
lead: "Model Context Protocol server for Chainguard documentation"
description: "Access Chainguard documentation through MCP for AI assistants and automation"
type: "article"
date: 2026-01-02T21:00:00+00:00
lastmod: 2026-05-20T00:00:00+00:00
draft: false
images: []
weight: 600
aliases:
  - /chainguard/mcp-server-ai-docs/
---

## Overview

The Chainguard AI Documentation MCP server gives AI assistants and automation tools searchable access to Chainguard's container image docs, security guides, and tool references. The server returns only the sections that match each query, so clients avoid loading the full documentation bundle into context.

## What is MCP?

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/) is an open protocol that standardizes how AI applications access external data and tools. An MCP server exposes structured data and tools that AI clients can call to ground their responses in real information.

## Why use the MCP server?

- **Lower context cost.** Clients fetch only the sections they need instead of loading 2.8 MB of documentation into every prompt.
- **Structured queries.** Look up a specific image, search for a CVE, or find a package equivalent without writing custom scrapers.
- **IDE integration.** Works with Claude Code, Claude Desktop, Cursor, and other MCP-compatible clients, so developers can reference Chainguard docs while they write code.

## Getting started

### Prerequisites

- An MCP-compatible client such as Claude Code, Claude Desktop, or Cursor

### Hosted server (recommended)

Chainguard hosts a public MCP server at `https://mcp.edu.chainguard.dev/mcp/`. This is the fastest way to get started — no Docker or local setup required.

How you register the server depends on your MCP client. Clients that support HTTP transport natively can connect to the URL directly. Clients that only spawn local processes (including Claude Desktop) need a small bridge such as [`mcp-remote`](https://github.com/geelen/mcp-remote).

#### Claude Code

Run this command:

```bash
claude mcp add --transport http chainguard-docs https://mcp.edu.chainguard.dev/mcp/
```

The server is available immediately. Verify it with `claude mcp list`.

> **Note:** This sets up the docs MCP for use in the current directory. To scope use of the MCP server to any directory in which your user account uses, adjust the command by adding `--scope user` to the end.

#### Claude Desktop

Claude Desktop reads MCP servers from a JSON file but does not yet support HTTP transport directly. Use `mcp-remote` to bridge to the hosted server:

```json
{
  "mcpServers": {
    "chainguard-docs": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://mcp.edu.chainguard.dev/mcp/"
      ]
    }
  }
}
```

The configuration file lives at:

* **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
* **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

`npx` downloads and runs `mcp-remote` on demand, so Node.js must be installed on the host. Restart Claude Desktop after saving the file.

#### Cursor and other clients with native HTTP transport

Add the server URL to your client's MCP configuration:

```json
{
  "mcpServers": {
    "chainguard-docs": {
      "url": "https://mcp.edu.chainguard.dev/mcp/"
    }
  }
}
```

Consult your client's documentation for the configuration file location, then restart the client. The Chainguard documentation tools appear in the next conversation.

### Local Docker setup

To run the MCP server locally, pull the container image:

```bash
docker pull ghcr.io/chainguard-dev/ai-docs:latest
```

The image's `serve-mcp` entrypoint speaks stdio, which works with any MCP client that launches local processes. For Claude Desktop, add this block to `claude_desktop_config.json`:

```json
{
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
}
```

Restart the client after saving the file.

## Available tools

The server exposes seven tools for querying documentation, mapping packages, and checking image availability.

### `search_docs`

Search across all Chainguard documentation for relevant content.

**Parameters:**
- `query` (string, required): Search query
- `max_results` (integer, optional): Maximum results to return (default: 5)

**Example prompts:**
- "Search Chainguard docs for python CVE management"
- "Find information about FIPS compliance"
- "Search for nginx configuration examples"

### `get_image_docs`

Get documentation for a specific Chainguard container image.

**Parameters:**
- `image_name` (string, required): Image name (e.g., "python", "node", "nginx")

**Example prompts:**
- "Show me the Python image documentation"
- "Get docs for the nginx image"
- "What's in the node image?"

### `list_images`

List Chainguard container images with optional filtering. When the image catalog is available, results include metadata such as documentation status and alternative mappings.

**Parameters:**
- `filter` (string, optional): Filter images by name or alternate mapping (for example, "python", "nginx", "apache")
- `include_upstream` (boolean, optional): Include alternate image mappings and variants in results (default: `false`)

**Example prompts:**
- "List all Chainguard images"
- "Show me images related to Python"
- "List images with equivalent mappings included"

### `get_security_docs`

Get security-related documentation including CVE management, SBOMs, and signing.

**Example prompts:**
- "How does Chainguard handle CVEs?"
- "Show me security documentation"
- "Explain SBOM generation"

### `get_tool_docs`

Get documentation for Chainguard tools and ecosystem components.

**Parameters:**
- `tool_name` (string, required): Tool name: `wolfi`, `apko`, `melange`, or `chainctl`

**Example prompts:**
- "Show me wolfi documentation"
- "How do I use apko?"
- "Explain melange"

### `find_package_equivalent`

Find the Wolfi package that replaces a Debian, Fedora, or Alpine package. Use this when migrating a Dockerfile to a Chainguard image and translating package names for `apk add`.

**Parameters:**
- `package` (string, required): Upstream OS package name (e.g., "build-essential", "libssl-dev", "python3-pip")
- `distro` (string, optional): Source distribution to search: `debian`, `fedora`, or `alpine`. Searches all distributions if omitted.

**Example prompts:**
- "What's the Wolfi equivalent of Debian's build-essential?"
- "Find the Chainguard package for libssl-dev"
- "I need to replace python3-pip in my Alpine Dockerfile"

### `check_image_freshness`

Query `cgr.dev` for an image's availability and current tags. Falls back to catalog data if the registry is unreachable.

**Parameters:**
- `image_name` (string, required): Chainguard image name (such as "python", "node", "nginx")

**Example prompts:**
- "What tags are available for the Python image?"
- "Show me the available tags for the nginx image"
- "Is the golang image available on cgr.dev?"

## Image catalog

The `list_images`, `find_package_equivalent`, and `check_image_freshness` tools draw from a pre-built catalog that ships with the server. The catalog includes:

- Every Chainguard container image with its registry reference, sourced from the image documentation
- Package mappings from Debian, Fedora, and Alpine to their Wolfi equivalents

The weekly documentation build regenerates the catalog.

## Example usage

Sample exchanges from a Claude Desktop session with the server connected:

```
You: Search for python image security best practices

Claude: [Uses search_docs tool]
Based on the Chainguard documentation, here are Python image security best practices:
...
```

```
You: Show me the nginx image documentation

Claude: [Uses get_image_docs tool]
Here's the complete documentation for the Chainguard nginx image:
...
```

```
You: What's the Wolfi equivalent of Debian's build-essential?

Claude: [Uses find_package_equivalent tool]
The Wolfi equivalent of Debian's build-essential is build-base. You can install it with:
apk add build-base
...
```

```
You: What tags are available for the python image?

Claude: [Uses check_image_freshness tool]
The Chainguard Python image (cgr.dev/chainguard/python) is available with these tags:
latest, latest-dev, 3.13, 3.13-dev, ...
```

## Standalone installation (without Docker)

The server script and its dependencies live in the [edu repository](https://github.com/chainguard-dev/edu). The documentation files ship inside the container image, which you can extract once and reuse.

```bash
# Download the MCP server script and requirements
curl -LO https://raw.githubusercontent.com/chainguard-dev/edu/main/scripts/mcp-server.py
curl -LO https://raw.githubusercontent.com/chainguard-dev/edu/main/scripts/mcp-requirements.txt

# Extract the documentation bundle from the container image
docker run --rm -v $(pwd):/output ghcr.io/chainguard-dev/ai-docs:latest extract /output
# Writes chainguard-ai-docs.md and image-catalog.json to the current directory

# Install dependencies
pip install -r mcp-requirements.txt

# Run the server
DOCS_PATH=chainguard-ai-docs.md CATALOG_PATH=image-catalog.json python3 mcp-server.py
```

To run this script under Claude Desktop, point the configuration at the local files:

```json
{
  "mcpServers": {
    "chainguard-docs": {
      "command": "python3",
      "args": ["/path/to/mcp-server.py"],
      "env": {
        "DOCS_PATH": "/path/to/chainguard-ai-docs.md",
        "CATALOG_PATH": "/path/to/image-catalog.json"
      }
    }
  }
}
```

## Self-hosting with HTTP transport

Run your own HTTP instance when you need to expose the server inside a firewall or with custom configuration.

### From the standalone script

```bash
python3 mcp-server.py --transport http --port 8080
```

The server binds to `http://0.0.0.0:8080` with the MCP endpoint at `/mcp`.

Environment variables work too:

```bash
MCP_TRANSPORT=http MCP_PORT=8080 python3 mcp-server.py
```

### From Docker

```bash
docker run --rm -p 8080:8080 ghcr.io/chainguard-dev/ai-docs:latest serve-mcp-http
```

Point your MCP client at `http://localhost:8080/mcp/`.

### CLI flags

| Flag | Env var | Default | Description |
|---|---|---|---|
| `--transport` | `MCP_TRANSPORT` | `stdio` | Transport mode: `stdio` or `http` |
| `--host` | `MCP_HOST` | `0.0.0.0` | HTTP server bind address |
| `--port` | `MCP_PORT` | `8080` | HTTP server port |

## Alternative: static documentation

If you don't need the server at all, extract the documentation file from the container:

```bash
docker run --rm -v $(pwd):/output \
  ghcr.io/chainguard-dev/ai-docs:latest extract /output
```

See the [Developer Resources](/developer-resources/) page for more on static extraction.

## Security features

The container image follows the standard Chainguard pattern:

- Built on `cgr.dev/chainguard/wolfi-base`
- Runs as a non-root user
- Signed with Cosign, with SBOM and provenance attached
- Rebuilt regularly so known CVEs do not accumulate

## Troubleshooting

### Server does not appear in Claude Desktop

1. Confirm that the configuration file path is correct for your platform.
2. Restart Claude Desktop after editing the file.
3. Check Claude Desktop's logs for parse or connection errors.
4. For the local Docker block, confirm Docker is running.

### Connection issues

Test the hosted server with `curl`:

```bash
curl -X POST https://mcp.edu.chainguard.dev/mcp/ \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-03-26","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}}}'
```

A JSON response listing the server's capabilities confirms the connection.

To test a local Docker server:

```bash
docker run --rm -i ghcr.io/chainguard-dev/ai-docs:latest serve-mcp
```

The container prints startup messages and then waits for stdio input.

### Documentation out of date

The hosted server updates automatically. For the local Docker setup, pull a fresh image:

```bash
docker pull ghcr.io/chainguard-dev/ai-docs:latest
```

## Resources

- [Model Context Protocol documentation](https://modelcontextprotocol.io/)
- [Chainguard MCP blog post](https://www.chainguard.dev/unchained/meet-chainguard-mcps-bringing-supply-chain-security-to-the-ai-era)
- [Developer Resources](/developer-resources/)
- [Chainguard Images Directory](https://images.chainguard.dev/)

## Need help?

- [Chainguard Support](https://support.chainguard.dev?utm=docs)
- [Community Slack](https://go.chainguard.dev/slack?utm=docs)
- [GitHub Issues](https://github.com/chainguard-dev/edu/issues)
