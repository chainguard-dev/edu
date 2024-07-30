---
title: "Wolfi FAQs"
type: "article"
description: "Frequently asked questions about Wolfi, a Linux undistro"
date: 2022-09-01T08:49:31+00:00
lastmod: 2022-10-15T08:49:31+00:00
draft: false
tags: ["Wolfi", "FAQ"]
images: []
menu:
  docs:
    parent: "wolfi"
weight: 300
toc: true
---
### What is Wolfi and how does it compare to Alpine?
Wolfi is our Linux _undistro_  designed from the ground up to support newer computing paradigms such as containers. Although Wolfi has a few similar design principles as Alpine (such as using apk), it is a different distribution that is focused on supply chain security. Unlike Alpine, Wolfi does not currently build its own Linux kernel, instead relying on the host environment (e.g. a container runtime) to provide one.

### Is Wolfi free to use?
Yes, Wolfi is free and will always be.

## Can I mix packages from Alpine repositories into a Wolfi-based image?
No, it's not possible to mix Alpine apks with Wolfi apks. If your image requires dependencies that are currently only available for Alpine, you might consider opening a new issue in the [wolfi-os](https://github.com/chainguard-dev/wolfi-os/) repository to suggest the new package addition, or use [melange](https://github.com/chainguard-dev/melange) to build a custom apk for your image.

### Can I use Wolfi on the Desktop?
No. Wolfi is an un-distro, or distroless base to be used within the container / OCI ecosystem. Desktop distributions require additional software that is out of scope for Wolfi's roadmap.

### Who maintains Wolfi?
Wolfi was created and is currently maintained by [Chainguard](https://chainguard.dev).

### What are the plans for long-term Wolfi governance?
We intend for Wolfi to be a community-driven project, which means over time it will have multi-vendor governance and maintainers. For now we're focused on building the project and community, and will revisit this in several months when a community has formed.

## Where can I get security feeds for Wolfi?
See [SECURITY.md](https://github.com/wolfi-dev/.github/blob/main/SECURITY.md) for information about reporting security incidents concerning and consuming security data about Wolfi.