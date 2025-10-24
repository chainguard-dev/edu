---
title: "Package Name Mappings"
linktitle: "Package Name Mappings"
type: "article"
description: "Understanding how Chainguard maps upstream package and image names to Chainguard Containers"
date: 2025-10-23T11:07:52+02:00
lastmod: 2025-10-23T11:07:52+02:00
draft: false
tags: ["Chainguard Containers", "Packages"]
images: []
menu:
  docs:
    parent: "about"
weight: 050
toc: true
---

When migrating to Chainguard Containers, you may notice that some package and image names differ from their upstream counterparts. This guide explains why these mappings exist and provides a comprehensive reference of how Chainguard maps upstream names to our container ecosystem.

## Why Chainguard Remaps Package Names

Chainguard Containers are built on [Wolfi](/open-source/wolfi/overview/), our Linux undistro designed specifically for containers. As part of this approach, we've made intentional decisions about package naming that serve several purposes:

### Consistency Across Distributions

Different Linux distributions often use different names for the same software. For example:
- Debian calls its C compiler package `build-essential`
- Alpine calls the equivalent package `build-base`
- Fedora uses `gcc` and related packages

Wolfi and Chainguard Containers standardize these names to provide consistency regardless of which distribution you're migrating from.

### Simplified Package Management

Some distributions split a single piece of software into many sub-packages, while others bundle functionality together. Chainguard's naming reflects a more streamlined approach that:
- Reduces the number of packages you need to install
- Makes dependencies clearer
- Minimizes the attack surface by avoiding unnecessary package splits

### Semantic Clarity

In some cases, upstream package names can be ambiguous or misleading. For instance:
- `python3` in Debian maps to `python-3` in Wolfi/Chainguard for clarity
- `netcat-traditional` becomes `netcat-openbsd` to specify the implementation
- `google-chrome-stable` maps to `chromium`, reflecting the open-source base

### Container Image Name Conventions

For container images, Chainguard follows naming conventions that prioritize:
- **Specificity**: Instead of generic names, we use descriptive names (e.g., `argocd-repo-server` instead of just `argocd`)
- **Consistency**: All our images follow similar naming patterns
- **Discoverability**: Names that clearly indicate the software's purpose

## Using Package Mappings

When you're using Chainguard's [Dockerfile Converter (dfc)](/chainguard/migration/dockerfile-conversion/), these mappings are applied automatically. The tool recognizes upstream package and image names and translates them to their Chainguard equivalents.

For manual migrations, you can reference the tables below to find the correct package or image name.

## Package Name Mappings

### Debian/Ubuntu Packages

The following table shows how Debian and Ubuntu package names (used with `apt`, `apt-get`) map to Wolfi/Chainguard package names (used with `apk`).

{{< package-mappings/debian-packages >}}

### Fedora/RedHat/UBI Packages

The following table shows how Fedora, RedHat, and UBI package names (used with `yum`, `dnf`, `microdnf`) map to Wolfi/Chainguard package names.

{{< package-mappings/fedora-packages >}}

### Alpine Packages

Alpine Linux package names generally align with Wolfi package names, as both use `apk` and share similar package management philosophies. In most cases, no mapping is necessary when migrating from Alpine to Chainguard Containers.

## Image Name Mappings

The following table shows how upstream container image names map to Chainguard Containers. Note that wildcard patterns (indicated by `*`) match multiple variants of an image name.

{{< package-mappings/image-mappings >}}

## Keeping Mappings Up to Date

The package and image mappings shown above are automatically updated from Chainguard's [dfc repository](https://github.com/chainguard-dev/dfc/blob/main/pkg/dfc/builtin-mappings.yaml) every time this site is built. This ensures you always have access to the latest mapping information without any manual intervention.

If you encounter a package or image that isn't listed here, you can:
1. Check if the package exists in Wolfi with the same name
2. Search the [Wolfi package repository](https://github.com/wolfi-dev/os) to see if it's available under a different name
3. Search the [Chainguard Images Directory](https://images.chainguard.dev/) to find available container images
4. Contribute to the [dfc project](https://github.com/chainguard-dev/dfc) to suggest new mappings

## Learn More

For more information about working with Chainguard Containers and package management, see:
- [Using the Dockerfile Converter](/chainguard/migration/dockerfile-conversion/)
- [Chainguard's Package Model](/chainguard/chainguard-images/features/packages/package-model/)
- [Wolfi Overview](/open-source/wolfi/overview/)
- [Debian Compatibility](/chainguard/migration/compatibility/debian-compatibility/)
