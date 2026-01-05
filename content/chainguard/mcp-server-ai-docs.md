---
title: "MCP Server for AI Documentation"
linktitle: "MCP: AI Docs"
lead: "Model Context Protocol server for Chainguard documentation"
description: "Access Chainguard documentation through MCP for AI assistants and automation"
type: "article"
date: 2026-01-02T21:00:00+00:00
lastmod: 2026-01-02T21:00:00+00:00
draft: false
images: []
weight: 600
menu:
  main:
    identifier: "mcp-server-ai-docs"
    parent: ""
    weight: 9999
    hidden: true
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

The MCP server provides these tools for querying Chainguard documentation:

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

List all available Chainguard container images.

**Example prompts:**
- "List all Chainguard images"
- "What images are available?"
- "Show me the image catalog"

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

## Alternative: Static Documentation

If you don't need MCP server functionality, you can extract the documentation as a single markdown file:

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
