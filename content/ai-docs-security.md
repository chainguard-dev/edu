---
title: "AI Documentation Security"
lead: "Security and transparency for AI-ready documentation"
description: "Learn about the security measures and compilation process for Chainguard's AI documentation bundles"
type: "article"
date: 2025-07-30T10:00:00+00:00
lastmod: 2026-09-30T13:19:11+00:00
draft: false
images: []
weight: 20
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
- **Bundle Size Limit**: The build fails if the compiled bundle exceeds 50 MB
- **Extension Filtering**: Only `.md`, `.html`, `.json`, and `.yaml` files are processed

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
- **Build Provenance**: GitHub Actions workflow attestations
- **Container Signing**: Images signed by immutable digest with Cosign

## Compilation Process

### Source Repositories

Documentation is compiled from the **chainguard-dev/edu** repository:

1. **Documentation pages**: every page published on this site
2. **Dockerfile Converter mappings**: the package and image mappings from **chainguard-dev/dfc**, which a nightly job copies into the edu repository

### Build Environment

- **GitHub Actions**: Secure, ephemeral build environment
- **Resource Limits**: CPU and memory constraints enforced
- **Restricted Egress**: Network access limited to required endpoints via [StepSecurity Harden Runner](https://github.com/step-security/harden-runner)
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

### Container Image Verification

Verify the container image signature before pulling documentation:

```bash
cosign verify ghcr.io/chainguard-dev/ai-docs:latest \
  --certificate-identity-regexp ".*github.com/chainguard-dev/edu.*" \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
```

## Build Frequency

- **Scheduled Builds**: Nightly at 2 AM UTC
- **On-Demand**: Triggered by documentation changes and by changes to the compilation scripts
- **Container Distribution**: Updated container pushed to GHCR on each build

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

The compiler reads only the edu repository, so a clone is all it needs. It writes the bundle to `static/downloads/chainguard-complete-docs.md`.

### How do I verify the build logs?

Build logs are public on GitHub Actions:

- [View Build Logs](https://github.com/chainguard-dev/edu/actions/workflows/compile-ai-docs-from-gcs.yaml)

### What if verification fails?

1. Ensure you have the latest version of cosign
2. Check your internet connection (for transparency log verification)
3. Try downloading the files again
4. Report persistent issues to support@chainguard.dev

## Additional Resources

- [Sigstore Documentation](https://docs.sigstore.dev/)
- [Cosign Installation](https://docs.sigstore.dev/cosign/system_config/installation/)
- [Supply Chain Security](https://slsa.dev/)
- [Chainguard Security Practices](https://security.chainguard.dev/)
