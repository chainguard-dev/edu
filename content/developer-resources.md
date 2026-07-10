---
title: "Developer Resources"
lead: "AI-ready documentation bundle for development"
description: "Compiled Chainguard documentation optimized for use with AI coding assistants"
type: "article"
date: 2025-07-29T10:00:00+00:00
lastmod: 2026-05-20T00:00:00+00:00
draft: false
images: []
weight: 50
toc: false
---

## AI-ready documentation bundle

This page describes a compiled bundle of Chainguard documentation that you can feed to AI coding assistants such as Claude, ChatGPT, or GitHub Copilot. Use it through the Chainguard-built container image or run the bundle as a Python MCP server.

### What's included

- Complete Chainguard Containers documentation
- Security best practices and CVE management
- Migration guides and tutorials
- API references and code examples
- Wolfi, melange, and apko documentation
- Compliance and supply chain security guides

## Download the AI documentation bundle

<div style="background-color: var(--blockquote-background); border-left: 4px solid var(--link-color, #2196F3); padding: 20px; border-radius: 4px; margin: 20px 0;">
  <h3 style="margin-top: 0; color: var(--body-color);">MCP server support</h3>
  <p style="color: var(--body-color);">Run the container as an <strong>MCP (Model Context Protocol) server</strong> for searchable, on-demand access to Chainguard documentation in AI assistants and IDEs.</p>
  <p><a href="/mcp-server-ai-docs/" style="font-weight: bold; text-decoration: none; color: var(--link-color, #2196F3);">→ Full MCP server documentation</a></p>
</div>

Two distribution methods are available:

<div style="background-color: var(--blockquote-background); border-left: 4px solid #4CAF50; padding: 16px; border-radius: 4px; margin: 20px 0;">
  <strong>Container distribution is recommended.</strong><br>
  The Chainguard container image includes verification scripts, runs as a non-root user, and is built on <code>wolfi-base</code>. Use it unless you have a reason to download files directly.
</div>

### Container distribution

Pull the container, then run it to print usage, verify the bundle, or extract the documentation:

```bash
# Pull the container image (built on Chainguard wolfi-base)
docker pull ghcr.io/chainguard-dev/ai-docs:latest

# Print available commands
docker run --rm ghcr.io/chainguard-dev/ai-docs:latest

# Verify documentation integrity
docker run --rm ghcr.io/chainguard-dev/ai-docs:latest verify

# Extract documentation to the current directory
docker run --rm -v $(pwd):/output ghcr.io/chainguard-dev/ai-docs:latest extract /output
```

**Container features:**

- Built on Chainguard's minimal `wolfi-base` image
- Runs as a non-root user
- Includes verification scripts and checksums
- Signed with Cosign
- Rebuilt weekly

**Verify the container signature:**

```bash
cosign verify ghcr.io/chainguard-dev/ai-docs:latest \
  --certificate-identity-regexp ".*github.com/chainguard-dev/edu.*" \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
```

### MCP server (Model Context Protocol)

**Recommended for:** developers, agent workflows, IDE integration.

Run the same container as an MCP server so AI assistants can search the documentation on demand:

```bash
# Run as MCP server
docker run --rm -i ghcr.io/chainguard-dev/ai-docs:latest serve-mcp
```

**Available MCP tools:**

- `search_docs` — search across all documentation
- `get_image_docs` — return docs for a specific container image
- `list_images` — list and filter available images, with optional upstream mappings
- `get_security_docs` — return CVE and security information
- `get_tool_docs` — return Wolfi, apko, melange, or chainctl docs
- `find_package_equivalent` — map a Debian, Fedora, or Alpine package to its Wolfi equivalent
- `check_image_freshness` — query the registry for current image tags

**Claude Desktop configuration:**

Add this block to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "chainguard-docs": {
      "command": "docker",
      "args": ["run", "--rm", "-i", "ghcr.io/chainguard-dev/ai-docs:latest", "serve-mcp"]
    }
  }
}
```

To use the hosted server instead of running a container locally, see the [hosted server instructions](/mcp-server-ai-docs/#hosted-server-recommended) — Claude Desktop reaches it through the [`mcp-remote`](https://github.com/geelen/mcp-remote) bridge. A [standalone Python script](/mcp-server-ai-docs/#standalone-installation-without-docker) is also available for setups without Docker.

[**Full MCP server documentation →**](/mcp-server-ai-docs/)

### Quick start

```bash
# Extract current documentation from the container image
docker run --rm -v $(pwd):/output ghcr.io/chainguard-dev/ai-docs:latest extract /output

# The extracted file 'chainguard-ai-docs.md' is ready to use with your AI assistant
```

### Security features

<div style="border: 2px solid #4CAF50; padding: 20px; border-radius: 8px; margin: 20px 0;">
  <h4>Bundle security</h4>
  <ul>
    <li>Container image signed with Sigstore/Cosign</li>
    <li>Distributed through GitHub Container Registry</li>
    <li>Rebuilt weekly through GitHub Actions</li>
    <li>Scanned with gitleaks during the build</li>
  </ul>
</div>

### Security transparency

<div style="background-color: var(--blockquote-background); border: 1px solid var(--sidebar-item-list-item-selected-background); padding: 16px; border-radius: 6px; margin: 20px 0;">
  <strong>Security first.</strong> The documentation bundles are compiled under controls described on the security page.
  <a href="/ai-docs-security" style="font-weight: bold;">Learn about our security practices →</a>
</div>

Security resources:

- **[Security and compilation process](/ai-docs-security)** — measures and verification steps
- [Build logs](https://github.com/chainguard-dev/edu/actions/workflows/compile-docs.yml) — public compilation logs
- [Source code](https://github.com/chainguard-dev/edu/tree/main/scripts) — open-source compilation scripts

### How to use the bundle with AI assistants

1. Download and verify the documentation bundle using one of the methods above.
2. Open your AI assistant (Claude, ChatGPT, and others).
3. Upload or paste the markdown file into the conversation.
4. Start coding with Chainguard context available to the assistant.

### Example prompts for common tasks

Once the documentation is loaded, try these prompts with your AI assistant:

#### Container security and CVEs

- "Search for Chainguard container security best practices and CVE management"
- "How do I migrate from Docker Hub images to Chainguard images?"
- "Show me examples of using Chainguard images in production"
- "What's the difference between Chainguard's latest and latest-dev tags?"
- "How do I scan Chainguard images for vulnerabilities?"
- "Explain Chainguard's approach to zero CVE images"

#### Development workflows

- "Find information about debugging distroless containers"
- "How do I use Chainguard images with Kubernetes?"
- "What are the differences between Chainguard development and production images?"
- "Show me how to use multi-stage builds with Chainguard images"
- "How do I add custom packages to a Chainguard image?"
- "Create a Dockerfile using Chainguard's Python image for a Flask app"

#### Specific technologies

- "Show me Chainguard's Python/Node.js/Go image documentation"
- "Find FIPS-compliant container information"
- "How do I use Chainguard images for AI/ML workloads?"
- "What Java versions are available in Chainguard images?"
- "How to use Chainguard's PostgreSQL image with custom extensions"
- "Show examples of using Chainguard's NGINX image with custom configs"

#### Security and compliance

- "Search for SBOM and supply chain security information"
- "Find information about Chainguard's compliance certifications"
- "How does Chainguard help with CVE remediation?"
- "Explain how to verify Chainguard image signatures with cosign"
- "What are Chainguard's SLSA compliance levels?"
- "How to generate and analyze SBOMs for Chainguard images"

#### CI/CD integration

- "How do I use Chainguard images in GitHub Actions?"
- "Show me examples of using Chainguard images with GitLab CI"
- "How to set up automated vulnerability scanning for Chainguard images"
- "Best practices for caching Chainguard images in CI pipelines"
- "How to use chainctl in CI/CD workflows"

#### Troubleshooting

- "How do I troubleshoot 'command not found' errors in distroless images?"
- "Why is my application failing to start in a Chainguard image?"
- "How to debug permission issues in Chainguard containers"
- "Common migration issues when moving from Alpine to Wolfi-based images"
- "How to identify missing dependencies in distroless containers"

#### Architecture and best practices

- "Explain the architecture of Wolfi and how it differs from Alpine"
- "What is apko and how does it relate to Chainguard images?"
- "Best practices for minimizing image size with Chainguard"
- "How to implement a secure software supply chain with Chainguard"
- "Explain melange and its role in package building"

### Benefits for AI-assisted development

- **Complete context.** The assistant can see all Chainguard documentation at once.
- **Better code suggestions.** The assistant grounds its output in actual Chainguard patterns.
- **Faster development.** No need to search through multiple documentation pages.
- **Accurate answers.** Responses come from official Chainguard documentation rather than the model's training data.

### Updates

The bundle is rebuilt weekly. The compilation date appears at the top of the downloaded file.

### Need help?

If you have questions or need assistance:

- Visit [Chainguard Support](https://support.chainguard.dev?utm=docs)
- Join our [community Slack](https://go.chainguard.dev/slack?utm=docs)
- Browse the [documentation site](https://edu.chainguard.dev)
