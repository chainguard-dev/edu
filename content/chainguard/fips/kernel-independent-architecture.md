---
title: "Kernel-Independent FIPS Architecture"
linktitle: "Kernel-Independent FIPS"
type: "article"
description: "Technical deep-dive into Chainguard's kernel-independent FIPS implementation using userspace entropy sources"
date: 2025-10-16T08:00:00+00:00
lastmod: 2025-10-16T08:00:00+00:00
draft: false
tags: ["FIPS", "Architecture", "Entropy"]
images: []
weight: 050
toc: true
---

## Overview

Chainguard FIPS Containers use a userspace entropy source instead of relying on the host kernel to provide validated randomness. This kernel-independent design allows FIPS containers to run on any recent Linux kernel, eliminating the traditional requirement for kernels configured in FIPS mode.

This architectural approach addresses a longstanding limitation in deploying FIPS-compliant workloads (FIPS being the U.S. federal cryptographic standard) by removing kernel dependencies that previously restricted deployment options, prevented local development, and limited cloud platform choices.

## Chainguard's Architecture

### Core Components

**Jitterentropy library**: A userspace entropy generator that produces randomness from CPU execution timing variations. This library runs entirely within the container and has its own NIST SP 800-90B Entropy Source Validation (ESV).

**OpenSSL FIPS provider**: The CMVP-validated cryptographic module (Certificate [#4282](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4282)) that uses the userspace entropy source instead of kernel entropy.

**Self-contained packaging**: Both the entropy source and cryptographic module are bundled in the container image, making each container self-sufficient for FIPS compliance.

### How It Works

When a Chainguard FIPS container starts:

1. The container includes the Jitterentropy library with SP 800-90B validation
2. OpenSSL is configured at build time to use the userspace entropy source
3. Cryptographic operations obtain entropy from Jitterentropy running in userspace
4. No kernel entropy source is required or accessed

The FIPS cryptographic boundary is entirely within the container. The host kernel is not part of the compliance story.

### Validation Architecture

The design relies on two separate NIST certifications:

**CMVP Certificate #4282**: Validates the OpenSSL FIPS provider's cryptographic algorithms. This certificate includes a caveat noting that an approved entropy source is required.

**ESV Certificate**: Validates the Jitterentropy library as meeting SP 800-90B entropy requirements, satisfying the CMVP certificate's entropy caveat.

The entropy source sits outside the cryptographic boundary but is independently validated. This architecture is sound and meets NIST requirements.

## Why This Matters

### The Problem with Traditional FIPS Containers

Before kernel-independent FIPS, containers relied on the host kernel to provide SP 800-90B validated entropy through `/dev/random`. This meant:

**Kernel must be in FIPS mode**: Organizations had to provision and maintain kernels configured for FIPS, typically older LTS versions.

**Limited deployment options**:
- Cloud platforms without FIPS-enabled kernels (GKE with COS, AWS Bottlerocket, Azure Linux) were unavailable
- Latest instance types and hardware often unsupported
- Specific Linux distributions and versions required

**Development environment gaps**: Developers couldn't run FIPS containers on workstations, creating a gap between local development and production.

**CI/CD complexity**: Testing FIPS applications required dedicated infrastructure with FIPS-enabled kernels.

### Chainguard's Solution Benefits

**Any Linux kernel**: Deploy on any recent kernel without FIPS mode configuration. Use latest kernels with security patches and performance improvements.

**All cloud platforms**: Run on GKE, EKS, AKS, and other managed Kubernetes services regardless of their kernel configuration.

**Local development**: Test FIPS containers on developer workstations (macOS, Windows WSL2, Linux) without special setup.

**Standard CI/CD**: Use existing pipeline infrastructure without FIPS-specific runners.

**Latest hardware**: Access newest instance types and hardware optimizations immediately.

**Simplified operations**: Container updates handle FIPS compliance. No separate kernel maintenance track.

## Supported Runtimes and Languages

Kernel-independent FIPS is available for:

**Go** (versions 1.21+): Uses OpenSSL via golang-fips/go or microsoft/go implementations.

**Python** (versions 3.10-3.13): Native OpenSSL integration through `_ssl` and `hashlib` modules.

**Node.js** (versions 18-23): Built-in crypto module uses OpenSSL.

**.NET** (versions 6-8): System.Security.Cryptography uses OpenSSL on Linux.

**PHP** (versions 8.2-8.3): OpenSSL extension provides cryptographic functions.

**C/C++**: Direct OpenSSL API usage with FIPS provider.

**Java** (versions 11, 17, 21): As of August 2025, supports kernel-independent FIPS using Bouncy Castle Entropy Provider with Jitterentropy.

### Java's Transition

Java deserves special mention as it recently gained kernel-independent capability.

**Before August 2025**: Java-based FIPS images required the host kernel in FIPS mode because the Bouncy Castle FIPS provider (BC-FJA) lacked its own entropy source.

**August 2025 update**: Chainguard integrated Jitterentropy with a Bouncy Castle Entropy Provider, enabling Java FIPS containers to run on any kernel. Java images now ship with this configuration by default.

Read more: [Kernel-Independent FIPS for Java](https://www.chainguard.dev/unchained/announcing-kernel-independent-fips-for-java)

## What Still Requires Kernel FIPS Mode

A few use cases remain kernel-dependent:

**Certain Kubernetes CNI plugins**: Some Container Network Interface plugins require kernel cryptographic modules for network encryption.

**LUKS2 full-disk encryption**: Disk encryption operates at the block device level, requiring kernel cryptographic support.

**StrongSwan VPN**: IPsec VPN implementations typically use kernel cryptographic modules.

These involve kernel-level operations where userspace entropy cannot be substituted. For these workloads, configure the host kernel in FIPS mode.

## Verifying Kernel Independence

Check an image's SBOM (Software Bill of Materials) to verify kernel independence.

For images built from November 7, 2024 onward, the SBOM must contain:

```
libcrypto3>=3.4.0-r2
openssl-config-fipshardened>=3.4.0-r3
```

These package versions indicate userspace entropy source configuration.

Retrieve an image's SBOM:

```bash
cosign download sbom cgr.dev/ORGANIZATION/IMAGE:TAG
```

Then search for the required packages and versions.

## Architecture Comparison

### Traditional FIPS Stack

```
┌─────────────────────────┐
│   Application Code      │
├─────────────────────────┤
│  FIPS Crypto Module     │ ← CMVP Validated
├─────────────────────────┤
│   Container Runtime     │
└─────────────────────────┘
           ↓ (entropy request)
┌─────────────────────────┐
│   Host Kernel           │ ← Must be in FIPS mode
│   /dev/random           │ ← SP 800-90B source
└─────────────────────────┘
           ↓
┌─────────────────────────┐
│   Hardware RNG          │
└─────────────────────────┘
```

### Chainguard Kernel-Independent Stack

```
┌─────────────────────────┐
│   Application Code      │
├─────────────────────────┤
│  FIPS Crypto Module     │ ← CMVP Validated
├─────────────────────────┤
│  Jitterentropy Library  │ ← SP 800-90B Validated
├─────────────────────────┤
│   Container Runtime     │
└─────────────────────────┘
           ↓ (CPU timing)
┌─────────────────────────┐
│   Any Linux Kernel      │ ← No FIPS mode required
└─────────────────────────┘
```

### Feature Comparison

| Aspect | Traditional FIPS | Chainguard Kernel-Independent |
|--------|------------------|-------------------------------|
| **Kernel requirement** | Must be in FIPS mode | Any recent Linux kernel |
| **Entropy source** | Kernel (`/dev/random`) | Userspace (Jitterentropy) |
| **Developer testing** | Requires FIPS VM/hardware | Works on local workstation |
| **Cloud platforms** | Limited to FIPS-enabled kernels | All platforms supported |
| **Instance types** | Restricted to older hardware | Latest hardware available |
| **CI/CD** | Special FIPS infrastructure | Standard pipelines |
| **Validation** | CMVP cert + kernel validation | CMVP cert + ESV cert |
| **Container portability** | Limited | Full portability |
| **Maintenance** | Kernel + container updates | Container updates only |

## Performance Considerations

Userspace entropy generation raises performance questions, but testing shows minimal impact.

**Jitterentropy overhead**: Minimal on modern processors. The library generates entropy from CPU timing jitter, which is fast.

**Comparison to kernel entropy**: Userspace entropy can be **faster** in some cases by avoiding context switches and system calls to kernel space.

**Entropy caching**: OpenSSL caches entropy appropriately. Frequent cryptographic operations don't repeatedly call the entropy source.

**Production validation**: Chainguard FIPS images have been tested in production workloads with no significant performance degradation.

If you encounter performance issues, profile your application to identify the actual bottleneck before assuming entropy generation is the cause.

## Technical Deep Dive

### Cryptographic Boundaries

Understanding what's inside versus outside the FIPS boundary is essential.

**Inside the boundary**: OpenSSL FIPS provider containing:
- Approved cryptographic algorithms (AES, SHA-2, SHA-3, RSA, EdDSA, etc.)
- Key management functions
- Self-tests and integrity checks

**Outside the boundary**:
- Jitterentropy library (separately validated under SP 800-90B)
- Application code calling OpenSSL APIs
- Operating system services

The entropy source validation satisfies the cryptographic module's requirements without being inside the CMVP boundary. This separation is architecturally appropriate and compliant.

### Entropy Generation

Jitterentropy works by:

1. **Measuring CPU timing variations**: Execute code loops and measure execution time with high-resolution timers
2. **Collecting jitter**: Timing variations arise from CPU pipeline effects, cache behavior, interrupts, and other micro-architectural events
3. **Extracting entropy**: Statistical analysis determines how much entropy is present in the timing measurements
4. **SP 800-90B validation**: NIST testing confirms the source produces sufficient entropy

This approach is entirely in userspace and doesn't require hardware random number generators or kernel support.

### OpenSSL Configuration

Chainguard configures OpenSSL at build time to:

- Load the FIPS provider automatically
- Configure the provider to use Jitterentropy for entropy
- Operate in approved-only mode (no non-approved algorithms)
- Enforce FIPS configuration at runtime (cannot be disabled)

The `openssl-config-fipshardened` package implements these configurations. Applications using OpenSSL automatically get FIPS-validated cryptography without code changes.

## Next Steps

- [Getting Started with FIPS](/chainguard/fips/getting-started/) - Deploy your first FIPS container
- [Frequently Asked Questions](/chainguard/fips/faqs/) - Common questions about FIPS implementation
- [Blog: Kernel-Independent FIPS Images](https://www.chainguard.dev/unchained/kernel-independent-fips-images) - Original announcement with additional details
- [Blog: Kernel-Independent FIPS for Java](https://www.chainguard.dev/unchained/announcing-kernel-independent-fips-for-java) - Java-specific implementation
