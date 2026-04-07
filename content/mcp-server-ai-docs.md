---
title: "MCP Server for AI Documentation"
linktitle: "MCP: AI Docs"
lead: "Model Context Protocol server for Chainguard documentation"
description: "Access Chainguard documentation through MCP for AI assistants and automation"
type: "article"
date: 2026-01-02T21:00:00+00:00
lastmod: 2026-03-30T00:00:00+00:00
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

- Docker installed
- MCP-compatible client (Claude Desktop, Cursor, etc.)

### Pull the Container

```bash
docker pull ghcr.io/chainguard-dev/ai-docs:latest
```

### Run the MCP Server

```bash
docker run --rm -i ghcr.io/chainguard-dev/ai-docs:latest serve-mcp
```

The server runs in stdio mode and communicates via standard input/output, making it compatible with MCP clients.

## Claude Desktop Configuration

To use this MCP server with Claude Desktop, add it to your configuration file:

* **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
* **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

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

After adding this configuration, restart Claude Desktop. The Chainguard documentation tools will be available in your conversations.

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

The MCP server is also available as a standalone Python script from the [GitHub release](https://github.com/chainguard-dev/edu/releases/tag/ai-docs-bundle):

```bash
# Download the MCP server, requirements, docs, and catalog
curl -LO https://github.com/chainguard-dev/edu/releases/download/ai-docs-bundle/mcp-server.py
curl -LO https://github.com/chainguard-dev/edu/releases/download/ai-docs-bundle/mcp-requirements.txt
curl -LO https://github.com/chainguard-dev/edu/releases/download/ai-docs-bundle/chainguard-ai-docs.md
curl -LO https://github.com/chainguard-dev/edu/releases/download/ai-docs-bundle/image-catalog.json

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

## Alternative: Static Documentation

If you don't need MCP server functionality, you can download the documentation as a single markdown file from the [GitHub release](https://github.com/chainguard-dev/edu/releases/tag/ai-docs-bundle), or extract it from the container:

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
2. Ensure Docker is running
3. Restart Claude Desktop after configuration changes
4. Check Claude Desktop logs for error messages

### Connection Issues

```bash
# Test the server manually
docker run --rm -i ghcr.io/chainguard-dev/ai-docs:latest serve-mcp
```

The server should start and display startup messages.

### Documentation Out of Date

Pull the latest container image:

```bash
docker pull ghcr.io/chainguard-dev/ai-docs:latest
```

The documentation is automatically updated weekly.

## Resources

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [Chainguard MCP Blog Post](https://www.chainguard.dev/unchained/meet-chainguard-mcps-bringing-supply-chain-security-to-the-ai-era)
- [Developer Resources](/developer-resources/)
- [Chainguard Images Directory](https://images.chainguard.dev/)

## Need Help?

- [Chainguard Support](https://support.chainguard.dev?utm=docs)
- [Community Slack](https://go.chainguard.dev/slack?utm=docs)
- [GitHub Issues](https://github.com/chainguard-dev/edu/issues)
