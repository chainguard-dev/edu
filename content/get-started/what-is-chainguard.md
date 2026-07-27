---
title: "What is Chainguard?"
linktitle: "What is Chainguard?"
lead: "A high-level introduction to Chainguard: the problem it solves, the products it offers, and what makes them different."
description: "An overview of Chainguard: its mission to be the secure source for open source, its products (Containers, Libraries, and OS), and the Factory that builds them."
type: "article"
date: 2026-07-23T00:00:00+00:00
lastmod: 2026-07-23T00:00:00+00:00
draft: false
tags: ["Getting Started"]
images: []
weight: 001
---

Nearly every modern application is built on open source software. That software is powerful, but it arrives with problems: vulnerabilities (including publicly disclosed [CVEs](https://edu.chainguard.dev/software-security/glossary/#cve)), unpatched dependencies, unclear provenance, and the constant work of keeping it all up to date. Tracking and fixing these issues across a large codebase consumes engineering time that could go toward building products.

Chainguard's mission is to be the secure source for open source. Rather than leaving you to patch and harden open source software yourself, Chainguard rebuilds it from source in a hardened build environment, keeps it continuously updated, and distributes it with the metadata you need to verify what you're running. The result is software that carries low-to-no known CVEs and requires far less remediation work from your team.

## What Chainguard offers

Chainguard rebuilds open source software into products you can adopt directly, depending on how you consume dependencies:

- **[Chainguard Containers](/chainguard/chainguard-images/overview/)** are minimal, hardened container images. Following a distroless philosophy, each image includes only your application and its essential runtime dependencies, minimizing the overall attack surface. This minimalism is a large part of why they carry [low-to-no CVEs](/chainguard/chainguard-images/about/zerocve/).
- **[Chainguard Libraries](/chainguard/libraries/overview/)** bring the same approach to language dependencies. They're drop-in replacements for open source packages in the Java, Python, and JavaScript ecosystems, rebuilt from verified sources and continuously monitored.

You pull Chainguard Containers and Libraries from a single, policy-aware endpoint, the [Chainguard Repository](/chainguard/chainguard-repository/overview/).

Containers and Libraries are where most teams start, but Chainguard secures more than these. Its other products include:

- **[Chainguard OS](/chainguard/chainguard-os/overview/)**, the hardened Linux foundation the other products build on.
- **[Chainguard VMs](/chainguard/vms/overview/)**, minimal virtual machine images for cloud and hypervisor workloads.
- **[Chainguard Actions](/chainguard/actions/overview/)**, hardened replacements for popular GitHub Actions.
- **[Chainguard Guardener](/chainguard/guardener/)**, tooling to harden your own source code.
- **[Chainguard Agent Skills](/chainguard/agent-skills/overview/)**, security-reviewed skills for AI agents.

## The Chainguard Factory

Behind these products is the [Chainguard Factory](/platform/factory/overview/), the automated build system at the heart of what Chainguard does. The Factory continuously monitors thousands of open source projects. When a new upstream release appears, it fetches the source, verifies it, rebuilds it, retests it, and publishes signed packages built from source along with SBOMs and provenance metadata.

Because the Factory does this work for you, adopting a Chainguard artifact immediately reduces your software supply chain risk. Because Chainguard maintains the artifact continuously, those security improvements continue over time with minimal changes to your existing workflows.

## Why Chainguard

Compared with using artifacts from public repositories, Chainguard gives you:

- **Low-to-no CVEs**, so your team spends less time triaging and patching vulnerabilities.
- **A minimal attack surface**, because artifacts ship with only what they need to run.
- **Verifiable provenance** through signatures, SBOMs, and builds from source, so you can prove what's in your software supply chain.
- **Continuous updates**, so patches land automatically instead of waiting for manual upgrades.

## Where to go next

- Ready to try an image? Work through a [container example](/get-started/containers-examples/) for your language or service.
- Replacing dependencies instead? Start with the [libraries on-ramp](/get-started/libraries-examples/).
- Moving existing workloads over? Step through the [migration guides](/chainguard/migration/).
