---
title: "Package and Image Name Mappings"
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

When migrating to Chainguard Containers, you may notice that some package and image names differ from their upstream counterparts. This guide explains why these mappings exist and provides a comprehensive reference of how Chainguard maps image and package names to our container ecosystem.

## Why Chainguard Remaps Package Names

Different Linux distributions often use different names for the same software. For example, Debian calls its C compiler package `build-essential`, while Alpine calls the equivalent package `build-base` and Fedora uses `gcc` and related packages. Chainguard Containers standardize these names to provide consistency regardless of which distribution you're migrating from.

In some cases, upstream package names can be ambiguous or misleading. For instance, `netcat-traditional` becomes `netcat-openbsd` to specify the implementation, and `google-chrome-stable` maps to `chromium` to reflect the open-source base.

Some distributions split a single piece of software into many sub-packages, while others bundle functionality together. Chainguard's package naming reflects a more streamlined approach that reduces the number of packages you need to install, minimizing the attack surface by avoiding unnecessary package splits.

### Container Image Name Conventions

For container images, Chainguard follows naming conventions that prioritize:
- **Specificity**: Instead of generic names, we use descriptive names (e.g., `argocd-repo-server` instead of just `argocd`)
- **Consistency**: All our images follow similar naming patterns
- **Discoverability**: Names that clearly indicate the software's purpose


### Using package mappings

When you're using Chainguard's [Dockerfile Converter (dfc)](/chainguard/migration/dockerfile-conversion/), these mappings are applied automatically. The tool recognizes upstream package and image names and translates them to their Chainguard equivalents.

For manual migrations, you can reference the following tables to find the correct package or image name you need.


## Package Name Mappings

### Debian/Ubuntu Packages

The following table shows how Debian and Ubuntu package names (used with `apt`, `apt-get`) map to Chainguard package names (used with `apk`).

{{< package-mappings/debian-packages >}}

### Fedora/RedHat/UBI Packages

The following table shows how Fedora, RedHat, and UBI package names (used with `yum`, `dnf`, `microdnf`) map to Chainguard package names.

{{< package-mappings/fedora-packages >}}

### Alpine Packages

Alpine Linux package names generally align with Chainguard's package names, as both use `apk` and share similar package management philosophies. In most cases, no mapping is necessary when migrating from Alpine to Chainguard Containers.

## Image Name Mappings

The following table shows how upstream container image names map to Chainguard Containers. Note that wildcard patterns (indicated by `*`) match multiple variants of an image name.

{{< package-mappings/image-mappings >}}

## Learn More

For more information about working with Chainguard Containers and package management, you can check out our overview of [Chainguard's Package Model](/chainguard/chainguard-images/features/packages/package-model/). Additionally, you may find our doc on [Using the Dockerfile Converter](/chainguard/migration/dockerfile-conversion/) to be useful.
