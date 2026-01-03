---
title: "Developer Resources"
lead: "AI-ready documentation bundle for development"
description: "Compiled Chainguard documentation optimized for use with AI coding assistants"
type: "article"
date: 2025-07-29T10:00:00+00:00
lastmod: 2026-01-02T21:00:00+00:00
draft: false
images: []
weight: 50
toc: false
---

## AI-Ready Documentation Bundle

This page provides compiled Chainguard documentation optimized for use with AI coding assistants like Claude, ChatGPT, GitHub Copilot, and others. Choose between our cryptographically signed direct downloads or our secure container distribution.

### What's Included

A comprehensive collection of Chainguard documentation including:
- Complete Chainguard Containers documentation
- Security best practices and CVE management
- Migration guides and tutorials
- API references and code examples
- Wolfi, melange, and apko documentation
- Compliance and supply chain security guides

## Download AI Documentation Bundle

<div style="background-color: #e3f2fd; border-left: 4px solid #2196F3; padding: 20px; border-radius: 4px; margin: 20px 0;">
  <h3 style="margin-top: 0;">🚀 New: MCP Server Support</h3>
  <p>Run the container as an <strong>MCP (Model Context Protocol) server</strong> for searchable, on-demand access to Chainguard documentation in AI assistants and IDEs.</p>
  <p><a href="/chainguard/mcp-server-ai-docs/" style="font-weight: bold; text-decoration: none;">→ Full MCP Server Documentation</a></p>
</div>

Choose your preferred distribution method:

<div style="background-color: var(--blockquote-background); border-left: 4px solid #4CAF50; padding: 16px; border-radius: 4px; margin: 20px 0;">
  <strong>🐳 Container Distribution Recommended</strong><br>
  For enhanced security and verification, we recommend using the Chainguard container image. It includes built-in verification, runs as non-root, and is built on our secure <code>wolfi-base</code> image.
</div>

### GitHub Release

| Format | Description | Verification |
|--------|-------------|-------------|
| [Latest Release](https://github.com/chainguard-dev/edu/releases/tag/ai-docs-latest) | Cryptographically signed documentation bundle (~1.7MB) | Includes Cosign signatures and certificates |

### Container Distribution

Pull the secure, Chainguard-based container with embedded documentation:

```bash
# Pull the container image (built on Chainguard wolfi-base)
docker pull ghcr.io/chainguard-dev/ai-docs:latest

# View available commands and usage
docker run --rm ghcr.io/chainguard-dev/ai-docs:latest

# Verify documentation integrity
docker run --rm ghcr.io/chainguard-dev/ai-docs:latest verify

# Extract documentation to current directory
docker run --rm -v $(pwd):/output ghcr.io/chainguard-dev/ai-docs:latest extract /output
```

**Container Features:**
- Built on Chainguard's minimal `wolfi-base` image
- Runs as non-root user for enhanced security
- Includes verification scripts and checksums
- Cryptographically signed with Cosign
- Automatically updated weekly

**Verify Container Signature:**
```bash
# Verify the container image signature with Cosign
cosign verify ghcr.io/chainguard-dev/ai-docs:latest \
  --certificate-identity-regexp ".*" \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
```

### MCP Server (Model Context Protocol)

**Recommended for:** Developers, agent workflows, IDE integration

Run the container as an MCP server to provide AI assistants with searchable, on-demand access to Chainguard documentation:

```bash
# Run as MCP server
docker run --rm -i ghcr.io/chainguard-dev/ai-docs:latest serve-mcp
```

**MCP Tools Available:**
- `search_docs` - Search across all documentation
- `get_image_docs` - Get specific container image docs
- `list_images` - List available images
- `get_security_docs` - Get CVE and security information
- `get_tool_docs` - Get wolfi/apko/melange/chainctl docs

**Claude Desktop Configuration:**

Add to your `claude_desktop_config.json`:

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

**Benefits:**
- Efficient context usage - only retrieve what you need
- Searchable and queryable documentation
- Perfect for automated workflows
- Works with Claude Desktop, Cursor, and other MCP-compatible tools

[**Full MCP Server Documentation →**](/chainguard/mcp-server-ai-docs/)

### Quick Start

```bash
# Download the documentation bundle from GitHub releases
curl -LO https://github.com/chainguard-dev/edu/releases/download/ai-docs-latest/chainguard-ai-docs.tar.gz

# Extract the markdown file
tar -xzf chainguard-ai-docs.tar.gz

# The extracted file 'chainguard-ai-docs.md' is ready to use with your AI assistant
```

### Security Features

<div style="border: 2px solid #4CAF50; padding: 20px; border-radius: 8px; margin: 20px 0;">
  <h4>Available Security Features</h4>
  <ul>
    <li>Signed releases with Sigstore/Cosign</li>
    <li>Container distribution via GitHub Container Registry</li>
    <li>Automated updates via GitHub Actions</li>
    <li>Security scanning with gitleaks</li>
  </ul>
</div>


### Security Transparency

<div style="background-color: var(--blockquote-background); border: 1px solid var(--sidebar-item-list-item-selected-background); padding: 16px; border-radius: 6px; margin: 20px 0;">
  <strong>Security First:</strong> Our documentation bundles are compiled with security measures.
  <a href="/ai-docs-security" style="font-weight: bold;">Learn about our security practices →</a>
</div>

View our security resources:
- **[Security and Compilation Process](/ai-docs-security)** - Detailed security measures and verification
- [Build Logs](https://github.com/chainguard-dev/edu/actions/workflows/compile-docs.yml) - Public compilation logs
- [Source Code](https://github.com/chainguard-dev/edu/tree/main/scripts) - Open source compilation scripts

### How to Use with AI Assistants

1. **Download and verify** the documentation bundle using one of the methods above
2. **Open your AI assistant** (Claude, ChatGPT, etc.)
3. **Upload or paste the markdown file** into your conversation
4. **Start coding** with full Chainguard context available to your AI assistant

### Example Prompts for Common Tasks

Once you've loaded the documentation, try these prompts with your AI assistant:

#### Container Security and CVEs
- "Search for Chainguard container security best practices and CVE management"
- "How do I migrate from Docker Hub images to Chainguard images?"
- "Show me examples of using Chainguard images in production"
- "What's the difference between Chainguard's latest and latest-dev tags?"
- "How do I scan Chainguard images for vulnerabilities?"
- "Explain Chainguard's approach to zero CVE images"

#### Development Workflows
- "Find information about debugging distroless containers"
- "How do I use Chainguard images with Kubernetes?"
- "What are the differences between Chainguard development and production images?"
- "Show me how to use multi-stage builds with Chainguard images"
- "How do I add custom packages to a Chainguard image?"
- "Create a Dockerfile using Chainguard's Python image for a Flask app"

#### Specific Technologies
- "Show me Chainguard's Python/Node.js/Go image documentation"
- "Find FIPS-compliant container information"
- "How do I use Chainguard images for AI/ML workloads?"
- "What Java versions are available in Chainguard images?"
- "How to use Chainguard's PostgreSQL image with custom extensions"
- "Show examples of using Chainguard's NGINX image with custom configs"

#### Security and Compliance
- "Search for SBOM and supply chain security information"
- "Find information about Chainguard's compliance certifications"
- "How does Chainguard help with CVE remediation?"
- "Explain how to verify Chainguard image signatures with cosign"
- "What are Chainguard's SLSA compliance levels?"
- "How to generate and analyze SBOMs for Chainguard images"

#### CI/CD Integration
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

#### Architecture and Best Practices
- "Explain the architecture of Wolfi and how it differs from Alpine"
- "What is apko and how does it relate to Chainguard images?"
- "Best practices for minimizing image size with Chainguard"
- "How to implement a secure software supply chain with Chainguard"
- "Explain melange and its role in package building"

### Benefits for AI-Assisted Development

- **Complete Context**: AI assistants have access to all Chainguard documentation at once
- **Better Code Suggestions**: AI can reference actual Chainguard patterns and best practices
- **Faster Development**: No need to search through multiple documentation pages
- **Accurate Answers**: AI responses are based on official Chainguard documentation

### Updates

The bundle is regenerated periodically. Check the timestamp in the downloaded file for the compilation date.

### Need Help?

If you have questions or need assistance:
- Visit [Chainguard Support](https://support.chainguard.dev?utm=docs)
- Join our [Community Slack](https://go.chainguard.dev/slack?utm=docs)
- Review our [Documentation](https://edu.chainguard.dev)