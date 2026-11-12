---
title: "Chainguard OS FAQs"
linktitle: "FAQ"
type: "article"
description: "Frequently asked questions about Chainguard OS, the secure operating system powering production Chainguard containers with enterprise features and continuous updates"
lead: "Chainguard OS powers production container images with enhanced security, continuous updates, and enterprise-grade features - find answers to common questions about this purpose-built container operating system."
date: 2025-07-03T08:49:31+00:00
lastmod: 2026-11-06T14:00:04+00:00
draft: false
tags: ["Chainguard OS"]
images: []
menu:
  docs:
    parent: "chainguard-os"
    identifier: "Chainguard OS FAQ"
weight: 30
toc: true
---

This FAQ addresses common questions about [Chainguard OS](/chainguard/chainguard-os/), the security-focused operating system that powers Chainguard's Production container images and enterprise features.

## What is Chainguard OS?

Chainguard OS is a minimal, hardened Linux-based operating system designed for secure, containerized software delivery. Built in-house by Chainguard, it serves as the foundation for Chainguard’s container products and emphasizes continuous integration, immutable artifacts, and alignment with upstream software.

## What is the relationship between Chainguard OS and Wolfi?

Wolfi is the open source core of Chainguard OS, and Chainguard builds and maintains both. Wolfi is the distribution behind Chainguard's [Free container images](/chainguard/containers/concepts/container-categories/#free-containers). Chainguard OS builds on Wolfi and adds packages and enterprise features, such as FIPS-validated packages and the EOL Grace Period. It's the distribution behind [Production container images](/chainguard/containers/concepts/container-categories/#production-containers) and Chainguard's other products.

The two work the same way. Both use the apk package format, and both are rolling releases: neither has major OS versions, and packages update continuously as upstream projects publish new releases. They differ in who can access them and what Chainguard commits to:

| Feature | Wolfi | Chainguard OS |
|---|---|---|
| Container images | Free containers, such as `wolfi-base` | Production containers, such as `chainguard-base` |
| Package repository | The public Wolfi repository, `https://apk.cgr.dev/chainguard`, which doesn't require authentication | Your organization's Private APK Repository, `https://apk.cgr.dev/$ORGANIZATION_ID`, which requires authentication |
| Vulnerability remediation SLAs | No | Yes |
| End-of-life (EOL) support | Updates stop when upstream support ends | Updates continue for an additional period under the [EOL Grace Period](/chainguard/containers/concepts/lifecycle-and-eol/eol-grace-period/) |
| FIPS-validated packages | No | Yes |
| How scanners identify the OS | As Wolfi | As Chainguard, so scanners use Chainguard's security feed |

Don't mix packages from Wolfi and Chainguard OS in the same container image. Chainguard doesn't support images that combine them.

To compare the `wolfi-base` and `chainguard-base` images in more detail, refer to [Choosing a base container](/chainguard/containers/concepts/choosing-a-base-container/).

## What are the core principles behind Chainguard OS?

Chainguard OS is built around four core principles:

1. Continuous Integration and Delivery (CI/CD)
1. Nano Updates and Rebuilds
1. Minimal, Hardened, Immutable Artifacts
1. Delta Minimization

Each of these principles ensures that Chainguard OS can provide a more secure and efficient platform for software distribution.

## What makes Chainguard OS different from traditional Linux distributions?

Chainguard OS is designed specifically for more secure and containerized application delivery. Our approach differs from traditional distros in several key ways:

* No LTS model: instead of fixed major releases, Chainguard OS continuously delivers updates in alignment with upstream changes.
* Purpose-built containers: Chainguard OS is focused on “application systems” instead of a general-purpose operating system.
* Minimal package footprint: Chainguard OS ships only what is strictly needed, avoiding unnecessary libraries and tools.
* Automation-driven: using CI/CD pipelines, Chainguard OS delivers more secure, tested, and verifiable artifacts.
* Ephemeral design: Chainguard OS embraces container-native patterns, making updates and rollbacks trivial.

## What are the benefits of using Chainguard OS?

* Security — reduced attack surface, hardened builds, and continuous patching.
* Compliance — automatically generated SBOMs and provenance metadata for all artifacts.
* Operational efficiency — reduces long upgrade cycles and manual patching.
* Supply chain integrity — built using the [Chainguard Factory](https://www.youtube.com/watch?v=iU9hmW6hrGs) and adhering to [SLSA](https://slsa.dev/) standards.
