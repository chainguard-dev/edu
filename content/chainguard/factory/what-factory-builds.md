---
title: "What does the Chainguard Factory build?"
linktitle: "What the Factory Builds"
type: "article"
description: "Interview with Dustin Kirkland about the products and artifacts created by the Chainguard Factory"
date: 2025-08-02T16:00:00+00:00
lastmod: 2025-08-02T16:00:00+00:00
draft: false
tags: ["Chainguard Factory", "Chainguard Containers", "Video", "Overview"]
images: []
menu:
  docs:
    parent: "chainguard-factory"
weight: 020
toc: true
contentType: "product-docs"
---

{{< youtube V4xIcHDhBhw >}}

## Transcript

**Interviewer**: So Dustin, what does the Factory actually build every day?

**Dustin Kirkland**: Yeah, so the input is open source software that's coming in from thousands of upstream maintainers who are very much the experts in what they do. That goes into our Factory. We apply our build automation system and, importantly, our quality control and testing system.

Out of that comes a series of artifacts. We produce APKs, which is our package format. We produce container images, which is the output that our customers typically run in their Docker and Kubernetes environments. We also produce virtual machines that get loaded automatically into Google, Amazon, and Azure public clouds, as well as images that can run in QEMU and VMware on-prem.

And it also produces libraries. So we're rebuilding from source not just open source projects that yield packages, but we're also rebuilding open source software that yields Java artifacts—JAR files—and Python modules—Python wheels. All of those are packaged up and built and tested from a Chainguard perspective, and we publish those into a variety of different registries and artifact repositories that our customers can then consume securely inside of their environment.
