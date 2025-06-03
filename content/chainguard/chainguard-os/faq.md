---
title: "Chainguard OS FAQs"
linktitle: "FAQs"
type: "article"
description: "Chainguard OS FAQs"
lead: "Frequently asked questions about Chainguard OS"
date: 2025-06-03T08:49:31+00:00
lastmod: 2025-06-03T08:49:31+00:00
draft: false
tags: ["Chainguard OS", "Product"]
images: []
menu:
  docs:
    parent: "chainguard-os"
weight: 020
toc: true
---

Learn answers to your questions about [Chainguard OS](/chainguard/chainguard-os/). 

## What is Chainguard OS?
Chainguard OS is a minimal, hardened Linux-based operating system designed for secure, containerized software delivery. Built in-house by Chainguard, it serves as the foundation for Chainguard’s container products and emphasizes continuous integration, immutable artifacts, and alignment with upstream software.

## What is the relationship between Chainguard OS and Wolfi?
Wolfi refers to the OS of Chainguard’s [free starter container images](/chainguard/chainguard-images/about/images-categories/#starter-containers).

Chainguard OS refers to the production-grade distribution that powers all other Chainguard products.

Please note that mixing-and-matching content across Wolfi and Chainguard OS is not supported. 

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
* Compliance — automatically generated SBOMs and provenance metadata for all artifacts.
* Operational efficiency — reduces long upgrade cycles and manual patching.
* Supply chain integrity — built using the [Chainguard Factory](https://www.youtube.com/watch?v=iU9hmW6hrGs) and adhering to [SLSA](https://slsa.dev/) standards.