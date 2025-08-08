---
title: "Developer Resources"
lead: "AI-ready documentation bundle for development"
description: "Compiled Chainguard documentation optimized for use with AI coding assistants"
type: "article"
date: 2025-07-29T10:00:00+00:00
lastmod: 2025-07-29T10:00:00+00:00
draft: false
images: []
weight: 50
toc: false
---

## AI-Ready Documentation Bundle

This page provides compiled Chainguard documentation optimized for use with AI coding assistants like Claude, ChatGPT, GitHub Copilot, and others. Choose between our cryptographically signed direct downloads or our secure container distribution.

### What's Included

A comprehensive collection of Chainguard documentation including:
- Complete Chainguard Images documentation
- Security best practices and CVE management
- Migration guides and tutorials
- API references and code examples
- Wolfi, melange, and apko documentation

## Download AI Documentation Bundle

Choose your preferred secure distribution method:

### Signed Direct Downloads

Download and verify our cryptographically signed documentation:

<div style="border: 2px solid #4CAF50; padding: 20px; border-radius: 8px; margin: 20px 0;">
  <h4>Security Features</h4>
  <ul>
    <li>Signed with Sigstore/Cosign</li>
    <li>SHA-256 checksums included</li>
    <li>SBOM for transparency</li>
    <li>Automated security scanning</li>
  </ul>
</div>

#### Download Options

| Format | Size | Signature | Verification |
|--------|------|-----------|--------------|
| [Markdown Bundle](https://github.com/chainguard-dev/edu/releases/download/ai-docs/chainguard-ai-docs.tar.gz) | 1.7MB | [.sig](https://github.com/chainguard-dev/edu/releases/download/ai-docs/chainguard-ai-docs.tar.gz.sig) | [Instructions](#verify-direct) |
| [Individual Files](https://github.com/chainguard-dev/edu/releases/latest) | Varies | Each signed | [Instructions](#verify-direct) |

#### Quick Verification {#verify-direct}

```bash
# Download bundle and signature
curl -LO https://github.com/chainguard-dev/edu/releases/download/ai-docs/chainguard-ai-docs.tar.gz
curl -LO https://github.com/chainguard-dev/edu/releases/download/ai-docs/chainguard-ai-docs.tar.gz.sig

# Verify with cosign
cosign verify-blob \
  --certificate-identity-regexp ".*github.com/chainguard-dev/edu.*" \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com \
  --signature chainguard-ai-docs.tar.gz.sig \
  chainguard-ai-docs.tar.gz

# Extract if verification passes
tar -xzf chainguard-ai-docs.tar.gz
```

### Container Distribution

For maximum security, use our signed container image:

<div style="border: 2px solid #2196F3; padding: 20px; border-radius: 8px; margin: 20px 0;">
  <h4>Additional Container Security</h4>
  <ul>
    <li>Signed container image</li>
    <li>Immutable distribution</li>
    <li>Built on Chainguard Images</li>
    <li>Zero CVEs base image</li>
    <li>SLSA Level 3 provenance</li>
  </ul>
</div>

```bash
# Verify and pull container
cosign verify cgr.dev/chainguard/ai-docs:latest \
  --certificate-identity-regexp ".*" \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com

# Extract documentation
docker run --rm -v $(pwd):/output cgr.dev/chainguard/ai-docs:latest extract /output

# Or inspect first
docker run --rm cgr.dev/chainguard/ai-docs:latest verify
docker run --rm cgr.dev/chainguard/ai-docs:latest list-contents
```

### Verification Details

Both distribution methods include:

1. **Cosign Signatures**: Keyless signing via Sigstore
2. **Transparency Log**: Entries in Rekor
3. **SBOM**: Software Bill of Materials
4. **Checksums**: SHA-256 for all files
5. **Provenance**: Build attestations

### Choose Your Method

| Method | Best For | Verification | Tools Needed |
|--------|----------|--------------|--------------|
| **Direct Download** | Simple integration, CI/CD pipelines | Cosign CLI | cosign |
| **Container** | Maximum security, isolated verification | Container signatures | docker, cosign |

### Security Transparency

<div style="background-color: var(--blockquote-background); border: 1px solid var(--sidebar-item-list-item-selected-background); padding: 16px; border-radius: 6px; margin: 20px 0;">
  <strong>Security First:</strong> Our documentation bundles are compiled with extensive security measures.
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

To compile manually:

```bash
python3 scripts/compile_docs.py
```

### Need Help?

If you have questions or need assistance:
- Visit [Chainguard Support](https://support.chainguard.dev)
- Join our [Community Slack](https://chainguard.dev/slack)
- Review our [Documentation](https://edu.chainguard.dev)