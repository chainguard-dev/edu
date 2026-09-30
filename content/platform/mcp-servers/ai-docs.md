---
title: "AI Docs: Chainguard documentation for AI tools"
linktitle: "AI Docs"
lead: "Chainguard documentation for AI tools, through an MCP server or a downloadable bundle"
description: "Search Chainguard documentation from an AI tool or other MCP client, or download the compiled documentation bundle"
type: "article"
date: 2026-01-02T21:00:00+00:00
lastmod: 2026-09-30T14:05:59+00:00
draft: false
images: []
menu:
  docs:
    parent: "mcp-servers"
    identifier: "ai-docs"
weight: 60
aliases:
  - /mcp-server-ai-docs/
  - /chainguard/mcp-server-ai-docs/
  - /developer-resources/
---

AI Docs gives AI tools access to Chainguard's documentation: the guides, security references, and tool references published on this site, plus the package and image mappings that the Dockerfile Converter (dfc) uses. You can connect to it as an MCP server, which returns only the sections that match each query, or download the whole documentation bundle and give it to an AI tool directly.

AI Docs has no live container image data. It can tell you which Chainguard image replaces an upstream image, but for an image's tags, SBOM, or build date, use the `cg-oci` MCP server. Refer to [Container image data](#container-image-data).

For background on MCP and the other Chainguard MCP servers, refer to the [MCP servers overview](/platform/mcp-servers/overview/).

## Why use the MCP server?

- **Lower context cost.** Clients fetch only the sections they need instead of loading the entire multi-megabyte bundle into every prompt.
- **Structured queries.** Search for a guide, read the security documentation, or find a package or image equivalent without writing custom scrapers.
- **IDE integration.** Works with Claude Code, Claude Desktop, Cursor, and other MCP-compatible clients, so engineers can reference Chainguard docs while they write code.

## Connect to the server

### Prerequisites

- An MCP-compatible client such as Claude Code, Claude Desktop, or Cursor

### Hosted server (recommended)

Chainguard hosts a public MCP server at `https://mcp.edu.chainguard.dev/mcp`. This is the fastest way to get started — no Docker or local setup required, and no sign-in.

How you register the server depends on your MCP client. Clients that support HTTP transport natively can connect to the URL directly. Clients that only spawn local processes (including Claude Desktop) need a small bridge such as [`mcp-remote`](https://github.com/geelen/mcp-remote).

#### Claude Code

Run this command:

```bash
claude mcp add --transport http chainguard-docs https://mcp.edu.chainguard.dev/mcp
```

The server is available immediately. Verify it with `claude mcp list`.

By default, the command registers the server for the current directory only. To make it available in every directory, add `--scope user`.

#### Claude Desktop

Claude Desktop reads MCP servers from a JSON file but does not yet support HTTP transport directly. Use `mcp-remote` to bridge to the hosted server:

```json
{
  "mcpServers": {
    "chainguard-docs": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://mcp.edu.chainguard.dev/mcp"
      ]
    }
  }
}
```

The configuration file lives at:

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

`npx` downloads and runs `mcp-remote` on demand, so you need Node.js installed on the host. Restart Claude Desktop after saving the file.

#### Cursor and other clients with native HTTP transport

Add the server URL to your client's MCP configuration:

```json
{
  "mcpServers": {
    "chainguard-docs": {
      "url": "https://mcp.edu.chainguard.dev/mcp"
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

The image's `serve-mcp` entrypoint uses the stdio transport, which works with any MCP client that launches local processes. For Claude Desktop, add this block to `claude_desktop_config.json`:

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

The server exposes five tools for searching documentation and mapping packages and images.

### `search_docs`

Search across all Chainguard documentation for relevant content.

*Parameters:*

- `query` (string, required): Search query
- `max_results` (integer, optional): Maximum results to return (default: 5)

*Example prompts:*

- "Search Chainguard docs for python CVE management"
- "Find information about FIPS compliance"
- "Search for nginx configuration examples"

### `get_security_docs`

Get security-related documentation including CVE management, SBOMs, and signing.

*Example prompts:*

- "How does Chainguard handle CVEs?"
- "Show me security documentation"
- "Explain SBOM generation"

### `get_tool_docs`

Get documentation for Chainguard tools and ecosystem components.

*Parameters:*

- `tool_name` (string, required): Tool name: `wolfi`, `apko`, `melange`, or `chainctl`

*Example prompts:*

- "Show me wolfi documentation"
- "How do I use apko?"
- "Explain melange"

### `find_package_equivalent`

Find the Wolfi package that replaces a Debian, Fedora, or Alpine package. Use this when migrating a Dockerfile to a Chainguard image and translating package names for `apk add`.

*Parameters:*

- `package` (string, required): Upstream OS package name (for example, "build-essential", "libssl-dev", "python3-pip")
- `distro` (string, optional): Source distribution to search: `debian`, `fedora`, or `alpine`. Searches all distributions if omitted. The catalog has no Alpine mappings yet, so an Alpine lookup returns no match.

*Example prompts:*

- "What's the Wolfi equivalent of Debian's build-essential?"
- "Find the Chainguard package for libssl-dev"
- "I need to replace python3-pip in my Dockerfile"

### `find_image_equivalent`

Find the Chainguard image that replaces an upstream container image, using the Dockerfile Converter mappings. Use this when migrating a Dockerfile's `FROM` line. The tool matches names the way the Dockerfile Converter does: it ignores tags and digests, accepts Docker Hub names with or without a `docker.io/` host, and falls back to the last part of the name. It returns the Chainguard image name and a pull reference.

*Parameters:*

- `image` (string, required): Upstream image reference as it appears in a `FROM` line (for example, "bitnami/pgpool", "docker.io/library/node:20", "gcr.io/kaniko-project/executor")

*Example prompts:*

- "What Chainguard image replaces bitnami/pgpool?"
- "I'm migrating a Dockerfile that starts with FROM quay.io/prometheus/snmp-exporter. What's the Chainguard equivalent?"

## Container image data

AI Docs doesn't carry live container image data. Chainguard's product MCP servers read it from the registry and package index at the moment you ask, so their answers describe the images as they are now. These servers require a Chainguard account. For connection and authentication steps, refer to the [MCP servers overview](/platform/mcp-servers/overview/).

This table shows where to go for each image task, and which AI Docs tool used to cover it:

| Task | Former AI Docs tool | Use now |
| --- | --- | --- |
| Read an image's documentation | `get_image_docs` | The image's page in the [Chainguard Containers Directory](https://images.chainguard.dev/). For how the image was built, the `get_config` and `get_apko_config` tools on [`cg-oci`](/platform/mcp-servers/cg-oci/). |
| List images | `list_images` | The `list_repos` tool on [`cg-oci`](/platform/mcp-servers/cg-oci/), which lists the repositories your account can pull. To browse the public catalog, use the Chainguard Containers Directory. |
| Check an image's tags and build date | `check_image_freshness` | The `list_tags` tool on [`cg-oci`](/platform/mcp-servers/cg-oci/) for tags, and `get_manifest` for the build date. The `registry_tags_list` tool on [`cg-api`](/platform/mcp-servers/cg-api/) also filters tags by update time. |
| Map a Debian or Fedora package to Wolfi | `find_package_equivalent` | AI Docs, unchanged. For the Wolfi package's versions, SBOM, and build configuration, use the `search_packages` tool on [`cg-apk`](/platform/mcp-servers/cg-apk/). |
| Find the Chainguard image that replaces an upstream image | None | The `find_image_equivalent` tool in AI Docs. |

{{< note >}}
AI Docs removed its three image tools at the end of September 2026. Their data came from a snapshot of image documentation that had stopped updating.
{{< /note >}}

The AI Docs server also sends these pointers to each client when it connects, so an AI tool asked about an image can direct you to the right server.

### Image references

Write a Chainguard image reference as `cgr.dev/<your-organization>/<image>`, replacing `<your-organization>` with your Chainguard organization's name. Most Chainguard images are available only to organizations entitled to them, in the organization's own namespace. The public `cgr.dev/chainguard` namespace serves a free subset with `latest`-style tags only, so an image reference that works for one organization may not work in `cgr.dev/chainguard`. To check which images your organization can pull, use the `list_repos` tool on [`cg-oci`](/platform/mcp-servers/cg-oci/).

## Package catalog

The `find_package_equivalent` and `find_image_equivalent` tools draw from a package catalog that ships with the server. The catalog holds the Dockerfile Converter's mappings: Debian and Fedora packages to their Wolfi equivalents, with no Alpine mappings, and upstream images to the Chainguard images that replace them. Each documentation build regenerates it.

The catalog file is `package-mappings.json`. The container image and the extracted files also include an identical copy named `image-catalog.json`, the file's earlier name, so configurations that point at that name continue to work.

## Example usage

Sample exchanges from a Claude Code session with `chainguard-docs` connected. The documentation changes often, so your answers will differ.

```Prompt
How do I use a multi-stage build with the Chainguard Python image?
```

```output
  Called chainguard-docs (ctrl+o to expand)

● Use the -dev variant as the build stage and the minimal image as the
  runtime stage. The -dev image includes pip and a shell, so install your
  dependencies there, then copy them into the minimal image, which has
  only Python and its standard library. The Getting started with the
  Python Chainguard Container guide walks through a full example.
```

```Prompt
What's the Wolfi equivalent of Debian's build-essential?
```

```output
  Called chainguard-docs (ctrl+o to expand)

● Debian's build-essential maps to build-base in Wolfi. Install it with:

  apk add build-base
```

```Prompt
Which Chainguard image replaces bitnami/pgpool?
```

```output
  Called chainguard-docs (ctrl+o to expand)

● bitnami/pgpool maps to Chainguard's pgpool2 image. Pull it as
  cgr.dev/<your-organization>/pgpool2, replacing <your-organization>
  with your Chainguard organization's name.
```

## Standalone installation (without Docker)

The server script and its dependencies live in the [edu repository](https://github.com/chainguard-dev/edu). The documentation files ship inside the container image, which you can extract once and reuse.

```bash
# Download the MCP server script and requirements
curl -LO https://raw.githubusercontent.com/chainguard-dev/edu/main/scripts/mcp-server.py
curl -LO https://raw.githubusercontent.com/chainguard-dev/edu/main/scripts/mcp-requirements.txt

# Extract the documentation bundle from the container image
docker run --rm --user "$(id -u):$(id -g)" \
  -v $(pwd):/output ghcr.io/chainguard-dev/ai-docs:latest extract /output
# Writes chainguard-ai-docs.md, package-mappings.json, image-catalog.json,
# checksums.txt, and verification.sh into a chainguard-ai-docs/ subdirectory

# Install dependencies into a virtual environment
python3 -m venv .venv
.venv/bin/pip install -r mcp-requirements.txt

# Run the server
DOCS_PATH=chainguard-ai-docs/chainguard-ai-docs.md \
CATALOG_PATH=chainguard-ai-docs/package-mappings.json \
.venv/bin/python mcp-server.py
```

The container runs as a non-root user, so pass `--user` to let it write to the mounted directory and to leave the extracted files owned by you.

To run this script under Claude Desktop, point the configuration at the local files:

```json
{
  "mcpServers": {
    "chainguard-docs": {
      "command": "/path/to/.venv/bin/python",
      "args": ["/path/to/mcp-server.py"],
      "env": {
        "DOCS_PATH": "/path/to/chainguard-ai-docs.md",
        "CATALOG_PATH": "/path/to/package-mappings.json"
      }
    }
  }
}
```

## Self-host with HTTP transport

Run your own HTTP instance when you need to expose the server inside a firewall or with custom configuration.

### From the standalone script

```bash
.venv/bin/python mcp-server.py --transport http --port 8080
```

The server binds to `http://0.0.0.0:8080` with the MCP endpoint at `/mcp`.

Environment variables work too:

```bash
MCP_TRANSPORT=http MCP_PORT=8080 .venv/bin/python mcp-server.py
```

### From Docker

```bash
docker run --rm -p 8080:8080 ghcr.io/chainguard-dev/ai-docs:latest serve-mcp-http
```

Point your MCP client at `http://localhost:8080/mcp`.

### CLI flags

| Flag | Env var | Default | Description |
| --- | --- | --- | --- |
| `--transport` | `MCP_TRANSPORT` | `stdio` | Transport mode: `stdio` or `http` |
| `--host` | `MCP_HOST` | `0.0.0.0` | HTTP server bind address |
| `--port` | `MCP_PORT` | `8080` | HTTP server port |

## Use the documentation without a server

The documentation bundle is one Markdown file holding every page on this site, plus the Dockerfile Converter mappings. It carries its compilation date at the top of the file.

### Download the bundle

Download the bundle directly. It refreshes nightly.

```bash
curl -LO https://edu.chainguard.dev/downloads/chainguard-complete-docs.md
```

### Extract the bundle from the container image

The container image carries the same bundle, with checksums and a verification script, and rebuilds whenever the documentation changes. Run the image with no command to print its available commands. To verify the bundle and extract it:

```bash
docker pull ghcr.io/chainguard-dev/ai-docs:latest

docker run --rm ghcr.io/chainguard-dev/ai-docs:latest verify

docker run --rm --user "$(id -u):$(id -g)" \
  -v $(pwd):/output ghcr.io/chainguard-dev/ai-docs:latest extract /output
```

The extracted bundle is `chainguard-ai-docs/chainguard-ai-docs.md`.

To verify the container image's signature before you use it:

```bash
cosign verify ghcr.io/chainguard-dev/ai-docs:latest \
  --certificate-identity-regexp ".*github.com/chainguard-dev/edu.*" \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
```

### Give the bundle to an AI tool

The bundle is larger than most AI tools can hold in a single conversation. Tools that index attached files, such as a project knowledge base, handle it better than a chat that reads the whole file at once. For most questions, the MCP server is the better fit, because it returns only the sections that match.

To use the bundle:

1. Download or extract the bundle.
2. Add the file to your AI tool's project knowledge, or attach it to a conversation.
3. Ask your question. The AI tool answers from Chainguard's documentation rather than from its training data alone.

## Security features

The container image follows the standard Chainguard pattern:

- Built on `cgr.dev/chainguard/wolfi-base`
- Runs as a non-root user
- Signed with Cosign
- Rebuilt whenever the documentation changes, so known CVEs don't accumulate

Each build also scans the bundle for credential patterns before publishing it. For the compilation process and verification steps, refer to [AI documentation security](/ai-docs-security/). The [build logs](https://github.com/chainguard-dev/edu/actions/workflows/compile-ai-docs-from-gcs.yaml) and the [compilation scripts](https://github.com/chainguard-dev/edu/tree/main/scripts) are public.

## Troubleshooting

### Server does not appear in Claude Desktop

1. Confirm that the configuration file path is correct for your platform.
2. Restart Claude Desktop after editing the file.
3. Check Claude Desktop's logs for parse or connection errors.
4. For the local Docker block, confirm Docker is running.

### Connection issues

Test the hosted server with `curl`:

```bash
curl -X POST https://mcp.edu.chainguard.dev/mcp \
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

### An AI tool can't find image details

AI Docs has no live container image data. Connect [`cg-oci`](/platform/mcp-servers/cg-oci/) for live registry data, or look up the image in the [Chainguard Containers Directory](https://images.chainguard.dev/). Refer to [Container image data](#container-image-data).

### Documentation out of date

The hosted server updates automatically. For the local Docker setup, pull a fresh image:

```bash
docker pull ghcr.io/chainguard-dev/ai-docs:latest
```

## Resources

- [Chainguard MCP servers overview](/platform/mcp-servers/overview/)
- [`cg-oci`: the Chainguard container registry MCP server](/platform/mcp-servers/cg-oci/)
- [Model Context Protocol documentation](https://modelcontextprotocol.io/)
- [Chainguard MCP blog post](https://www.chainguard.dev/unchained/meet-chainguard-mcps-bringing-supply-chain-security-to-the-ai-era)
- [AI documentation security](/ai-docs-security/)
- [Chainguard Containers Directory](https://images.chainguard.dev/)

## Need help?

- [Get support](/get-started/get-support/)
- [Community Slack](https://join.slack.com/t/chainguardcommunity/shared_invite/zt-3nttdr807-V9BJHayWvsB0KbHsfZO5Rw)
- [GitHub Issues](https://github.com/chainguard-dev/edu/issues)
