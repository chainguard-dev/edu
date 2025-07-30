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
menu:
  main:
    weight: -1
    parent: ""
---

## AI-Ready Documentation Bundle

This page provides a compiled version of Chainguard documentation in a single file, optimized for use with AI coding assistants like Claude, ChatGPT, GitHub Copilot, and others.

### What's Included

A comprehensive collection of Chainguard documentation and resources compiled into a single file.

### Download Documentation

Choose your preferred format:

<div style="text-align: center; margin: 40px 0;">
  <div style="display: inline-block; margin: 10px;">
    <a href="/downloads/chainguard-complete-docs.md" 
       download="chainguard-complete-docs.md" 
       class="btn btn-primary"
       style="background-color: #1a73e8; color: white; padding: 12px 24px; text-decoration: none; border-radius: 6px; display: inline-block;">
      📄 Markdown (11MB)
    </a>
  </div>
  <div style="display: inline-block; margin: 10px;">
    <a href="/downloads/chainguard-complete-docs.zip" 
       download="chainguard-complete-docs.zip" 
       class="btn btn-primary"
       style="background-color: #1a73e8; color: white; padding: 12px 24px; text-decoration: none; border-radius: 6px; display: inline-block;">
      📦 ZIP (1.7MB)
    </a>
  </div>
  <div style="display: inline-block; margin: 10px;">
    <a href="/downloads/chainguard-complete-docs.tar.gz" 
       download="chainguard-complete-docs.tar.gz" 
       class="btn btn-primary"
       style="background-color: #1a73e8; color: white; padding: 12px 24px; text-decoration: none; border-radius: 6px; display: inline-block;">
      📦 TAR.GZ (1.7MB)
    </a>
  </div>
</div>

### How to Use with AI Assistants

1. **Download the documentation bundle** using the button above
2. **Open your AI assistant** (Claude, ChatGPT, etc.)
3. **Upload or paste the markdown file** into your conversation
4. **Start coding** with full Chainguard context available to your AI assistant

### Example Prompts for Common Tasks

Once you've loaded the documentation, try these prompts with your AI assistant:

#### Container Security & CVEs
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

#### Security & Compliance
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

#### Architecture & Best Practices
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