---
title: "MCP Server for AI Documentation"
linktitle: "MCP: AI Docs"
lead: "Model Context Protocol server for Chainguard documentation"
description: "Access Chainguard documentation through MCP for AI assistants and automation"
type: "article"
date: 2026-01-02T21:00:00+00:00
lastmod: 2026-04-10T00:00:00+00:00
draft: false
images: []
weight: 600
aliases:
  - /chainguard/mcp-server-ai-docs/
---

## Overview

The Chainguard AI Documentation MCP (Model Context Protocol) server enables AI assistants and automation tools to interact with Chainguard's complete documentation library through a standardized protocol. This provides efficient, searchable access to container image docs, security guides, and tool references without loading entire documentation bundles into context.

## What is MCP?

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/) is an open protocol that standardizes how AI applications access external data and tools. MCP servers expose structured data and capabilities that AI assistants can query and use to provide more accurate, context-aware responses.

## Why Use the MCP Server?

**Efficient Context Usage**
- Only retrieve relevant documentation sections
- Avoid loading 2.8 MB of docs into every prompt
- Search and filter content dynamically

**Better for Agents**
- Programmatic access to documentation
- Structured queries (get specific image docs, search CVEs, etc.)
- Perfect for automated workflows and CI/CD

**IDE Integration**
- Works with Claude Desktop, Cursor, and other MCP-compatible tools
- Access Chainguard docs while coding
- No manual copy/paste needed

## Getting Started

### Prerequisites

- MCP-compatible client (Claude Desktop, Cursor, Claude Code, or other MCP-compatible tools)

### Hosted Server (Recommended)

The fastest way to get started — no Docker or local setup required. Chainguard hosts a public MCP server at `mcp.edu.chainguard.dev`.

Add this to your MCP client configuration:

```json
{
  "mcpServers": {
    "chainguard-docs": {
      "url": "https://mcp.edu.chainguard.dev/mcp/"
    }
  }
}
```

For **Claude Desktop**, the configuration file is located at:

* **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
* **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

For **Claude Code**, add the server from the command line:

```bash
claude mcp add chainguard-docs --transport http https://mcp.edu.chainguard.dev/mcp/
```

After adding this configuration, restart your MCP client. The Chainguard documentation tools will be available in your conversations.

### Local Docker Setup

If you prefer to run the MCP server locally, you can use the container image:

```bash
docker pull ghcr.io/chainguard-dev/ai-docs:latest
```

Run in stdio mode for MCP clients that support local processes:

```bash
docker run --rm -i ghcr.io/chainguard-dev/ai-docs:latest serve-mcp
```

Claude Desktop configuration for the local Docker setup:

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

## Available Tools

The MCP server provides seven tools for querying Chainguard documentation, looking up package compatibility, and checking image availability:

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

List available Chainguard container images with optional filtering and equivalent mapping info. When the image catalog is available, results include metadata such as documentation status and alternative mappings.

**Parameters:**
- `filter` (string, optional): Filter images by name or alternate mapping (for example, "python", "nginx", "apache")
- `include_upstream` (Boolean, optional): Include alternate image mappings and variants in results (default: false)

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

Find Chainguard OS or Wolfi package equivalents for other OS packages. This is useful when migrating Dockerfiles from Debian, Fedora, or Alpine to Chainguard images and you need to translate package names for `apk add` commands.

**Parameters:**
- `package` (string, required): Upstream OS package name (e.g., "build-essential", "libssl-dev", "python3-pip")
- `distro` (string, optional): Source distribution to search: `debian`, `fedora`, or `alpine`. Searches all distributions if omitted.

**Example prompts:**
- "What's the Wolfi equivalent of Debian's build-essential?"
- "Find the Chainguard package for libssl-dev"
- "I need to replace python3-pip in my Alpine Dockerfile"

### `check_image_freshness`

Check a Chainguard image's availability and list its current tags via a live registry query to `cgr.dev`. Falls back to catalog data if no network access is available.

**Parameters:**
- `image_name` (string, required): Chainguard image name (such as "python", "node", "nginx")

**Example prompts:**
- "What tags are available for the Python image?"
- "Show me the available tags for the nginx image"
- "Is the golang image available on cgr.dev?"

## Image Catalog

The MCP server includes a pre-built image catalog that powers the `list_images`, `find_package_equivalent`, and `check_image_freshness` tools. The catalog contains:

- **All Chainguard container images** with registry references, sourced from image documentation
- **Package mappings** across Debian, Fedora, and Alpine to Wolfi equivalents

The catalog is regenerated automatically as part of the weekly documentation build.

## Example Usage

Once configured with Claude Desktop:

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

## Standalone Installation (without Docker)

The MCP server script and its dependencies are available directly from the repository. The documentation files are distributed via the container image.

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

To use this with Claude Desktop, update your configuration to point to the local script:

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

## Self-Hosting with HTTP Transport

You can also self-host the MCP server using Streamable HTTP transport. This is useful for running your own instance behind a firewall or with custom configuration.

### Standalone

```bash
python3 mcp-server.py --transport http --port 8080
```

The server will start on `http://0.0.0.0:8080` with the MCP endpoint at `/mcp`.

You can also configure via environment variables:

```bash
MCP_TRANSPORT=http MCP_PORT=8080 python3 mcp-server.py
```

### Docker

```bash
docker run --rm -p 8080:8080 ghcr.io/chainguard-dev/ai-docs:latest serve-mcp-http
```

Then configure your MCP client to connect to `http://localhost:8080/mcp/`.

### CLI Flags

| Flag | Env Var | Default | Description |
|---|---|---|---|
| `--transport` | `MCP_TRANSPORT` | `stdio` | Transport mode: `stdio` or `http` |
| `--host` | `MCP_HOST` | `0.0.0.0` | HTTP server bind address |
| `--port` | `MCP_PORT` | `8080` | HTTP server port |

## Alternative: Static Documentation

If you don't need MCP server functionality, extract the documentation from the container:

```bash
docker run --rm -v $(pwd):/output \
  ghcr.io/chainguard-dev/ai-docs:latest extract /output
```

See the [Developer Resources](/developer-resources/) page for more details on static extraction.

## Security Features

Following Chainguard's security-first approach:

- **Minimal Image**: Built on `cgr.dev/chainguard/wolfi-base`
- **Zero CVEs**: Regularly updated to maintain zero known vulnerabilities
- **Non-root**: Runs as non-root user
- **Signed**: Container images are signed with Cosign
- **Transparent**: Full SBOM and provenance available

## Troubleshooting

### Server Not Appearing in Claude Desktop

1. Check that the configuration file path is correct
2. Restart Claude Desktop after configuration changes
3. Check Claude Desktop logs for error messages
4. If using Docker locally, ensure Docker is running

### Connection Issues

Test the hosted server:

```bash
curl -X POST https://mcp.edu.chainguard.dev/mcp/ \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-03-26","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}}}'
```

You should receive a JSON response with the server's capabilities.

To test a local Docker server:

```bash
docker run --rm -i ghcr.io/chainguard-dev/ai-docs:latest serve-mcp
```

The server should start and display startup messages.

### Documentation Out of Date

The hosted server at `mcp.edu.chainguard.dev` is updated automatically. If using Docker locally, pull the latest image:

```bash
docker pull ghcr.io/chainguard-dev/ai-docs:latest
```

## Resources

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [Chainguard MCP Blog Post](https://www.chainguard.dev/unchained/meet-chainguard-mcps-bringing-supply-chain-security-to-the-ai-era)
- [Developer Resources](/developer-resources/)
- [Chainguard Images Directory](https://images.chainguard.dev/)

## Need Help?

- [Chainguard Support](https://support.chainguard.dev?utm=docs)
- [Community Slack](https://go.chainguard.dev/slack?utm=docs)
- [GitHub Issues](https://github.com/chainguard-dev/edu/issues)
