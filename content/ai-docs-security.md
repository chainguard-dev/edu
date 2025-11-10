---
title: "AI Documentation Security"
lead: "Security and transparency for AI-ready documentation"
description: "Learn about the security measures and compilation process for Chainguard's AI documentation bundles"
type: "article"
date: 2025-07-30T10:00:00+00:00
lastmod: 2025-07-30T10:00:00+00:00
draft: false
images: []
weight: 60
seo:
  robots: "noindex, follow"
menu:
  main:
    identifier: "ai-docs-security"
    parent: ""
    weight: 9999
    hidden: true
---

## Overview

Chainguard's AI documentation bundles are compiled with multiple security measures to ensure developers can trust the content they're using with AI coding assistants. This page details our security practices and compilation process.

## Security Measures

### 1. Automated Security Scanning

Every compilation runs through multiple security checks:

- **Secret Detection**: We scan for API keys, tokens, and other sensitive data
- **Pattern Matching**: Common secret patterns are automatically redacted
- **File Size Limits**: Individual files limited to 10MB, total bundle to 50MB
- **Extension Filtering**: Only `.md`, `.html`, and `.json` files are processed

### 2. Cryptographic Signatures

All documentation bundles are signed using Sigstore/Cosign:

- **Keyless Signing**: Using OIDC identity verification
- **Transparency Log**: All signatures recorded in Rekor
- **Certificate Chain**: Full certificate provided for verification
- **Multiple Signatures**: Both individual files and bundles are signed

### 3. Content Integrity

We ensure content hasn't been tampered with:

- **SHA-256 Checksums**: For all files in the bundle
- **Signed Checksums**: The checksum file itself is signed
- **Build Provenance**: SLSA Level 3 attestations
- **Immutable Artifacts**: Released versions never change

## Compilation Process

### Source Repositories

Documentation is compiled from these official repositories:

1. **chainguard-dev/edu**: Main documentation site
2. **chainguard-dev/courses**: Learning materials
3. **chainguard-images/images-private**: Image documentation

### Build Environment

- **GitHub Actions**: Secure, ephemeral build environment
- **Resource Limits**: CPU and memory constraints enforced
- **No Network Access**: During compilation phase
- **Minimal Permissions**: Only required repository access

### What Gets Filtered

During compilation, we automatically remove:

- Environment variables and secrets
- Internal URLs and endpoints
- Base64 encoded data blocks
- Private key materials
- Authentication tokens

Example patterns we redact:
- `api_key=...`
- `password=...`
- `-----BEGIN PRIVATE KEY-----`
- GitHub tokens (`ghp_`, `ghs_`)

## Verification Guide

### Direct Download Verification

```bash
# 1. Download files
curl -LO https://github.com/chainguard-dev/edu/releases/download/ai-docs-latest/chainguard-ai-docs.tar.gz
curl -LO https://github.com/chainguard-dev/edu/releases/download/ai-docs-latest/chainguard-ai-docs.tar.gz.sig
curl -LO https://github.com/chainguard-dev/edu/releases/download/ai-docs-latest/chainguard-ai-docs.tar.gz.crt

# 2. Verify signature
cosign verify-blob \
  --certificate chainguard-ai-docs.tar.gz.crt \
  --signature chainguard-ai-docs.tar.gz.sig \
  --certificate-identity "https://github.com/chainguard-dev/edu/.github/workflows/compile-public-docs.yml@refs/heads/main" \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com \
  chainguard-ai-docs.tar.gz

# 3. Extract contents
tar -xzf chainguard-ai-docs.tar.gz
```

## Build Frequency

- **Automatic Builds**: Daily at 2 AM UTC
- **On-Demand**: When documentation changes
- **Releases**: Weekly signed releases

## Security Reporting

If you discover a security issue:

1. **Do NOT** open a public issue
2. Email security@chainguard.dev
3. Include:
   - Description of the issue
   - Steps to reproduce
   - Potential impact

## FAQ

### Why are some sections marked [REDACTED]?

This indicates our security scanner detected potentially sensitive information and removed it to protect our systems and users.

### Can I build the bundle myself?

Yes! The compilation scripts are open source:

```bash
git clone https://github.com/chainguard-dev/edu
cd edu
python3 scripts/compile_docs.py
```

### How do I verify the build logs?

Build logs are public on GitHub Actions:
- [View Build Logs](https://github.com/chainguard-dev/edu/actions/workflows/compile-docs.yml)

### What if verification fails?

1. Ensure you have the latest version of cosign
2. Check your internet connection (for transparency log verification)
3. Try downloading the files again
4. Report persistent issues to support@chainguard.dev

## Additional Resources

- [Sigstore Documentation](https://docs.sigstore.dev/)
- [Cosign Installation](https://docs.sigstore.dev/cosign/system_config/installation/)
- [Supply Chain Security](https://slsa.dev/)
- [Chainguard Security Practices](https://www.chainguard.dev/security)
