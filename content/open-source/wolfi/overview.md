---
title: "Wolfi Overview"
type: "article"
description: "Getting started with Wolfi, the Linux undistro for secure container images"
lead: "Introducing Wolfi, the Linux undistro for secure container images"
date: 2022-09-01T08:49:31+00:00
lastmod: 2024-05-02T08:49:31+00:00
draft: false
tags: ["Wolfi", "Overview"]
images: []
menu:
  docs:
    parent: "wolfi"
weight: 100
toc: true
---

[Wolfi](https://github.com/wolfi-dev) is a community Linux [undistro](#why-undistro) designed for the container and cloud-native era. Chainguard started the Wolfi project to build [Chainguard Containers](/chainguard/chainguard-images/overview), our collection of curated [distroless](/chainguard/chainguard-images/getting-started-distroless/) images that meet the requirements of a secure software supply chain. This required a Linux distribution with components at the appropriate granularity and with support for [glibc](https://www.gnu.org/software/libc/).

Building our own undistro also allows us to ensure packages have full provenance and metadata for supporting modern supply-chain security needs.

## Why Undistro

We call Wolfi an undistro because unlike a [typical Linux distribution](https://en.wikipedia.org/wiki/Linux_distribution) designed to run on bare-metal, Wolfi is a stripped-down distro designed for the cloud-native era. It doesn't have a kernel of its own, instead relying on the environment (such as the container runtime) to provide one. This separation of concerns in Wolfi means it is adaptable to a range of environments.

Wolfi is the base we use to build [Chainguard Containers](/chainguard/chainguard-images/overview), our open source distroless images that are available free of charge.

## Wolfi Features

Wolfi, whose name was inspired by the [world's smallest octopus](https://en.wikipedia.org/wiki/Octopus_wolfi), has some key features that differentiates it from other distributions that focus on container/cloud-native environments:

- Provides a high-quality, build-time SBOM as standard for all packages
- Packages are designed to be granular and independent, to support minimal images
- Uses the proven and reliable apk package format
- Fully declarative and reproducible build system
- Designed to support glibc

Wolfi enables Chainguard to solve the software supply chain security problem from the outside in. It gives developers the secure-by-default base they need to build software, it scales to support organizations running massive environments and provides the control needed to fix most modern supply chain threats. Wolfi builds all packages directly from source, allowing us to fix vulnerabilities or apply customizations that improve the supply chain security posture of everything from compilers to language package managers.

## Quickstart

This site's [Wolfi section](/open-source/wolfi/) contains full information on Wolfi and how to build Wolfi packages, but if you
would like to quickly review how to work with Wolfi, try the [wolfi-base
image](https://images.chainguard.dev/directory/image/wolfi-base/overview?utm_source=cg-academy&utm_medium=referral&utm_campaign=dev-enablement&utm_content=edu-content-open-source-wolfi-overview). You can run it with:

```sh
docker run -it cgr.dev/chainguard/wolfi-base
```

This should start a Wolfi container where you can explore the file system and investigate which
packages are available. This container is intentionally minimal - it includes the filesystem for
Wolfi, a package manager (apk) and a shell, but not much else. You will need to use apk to install
any tools you need. Here is an example session:

```
docker run -it cgr.dev/chainguard/wolfi-base
ce557598406a:/# cat /etc/os-release
ID=wolfi
NAME="Wolfi"
PRETTY_NAME="Wolfi"
VERSION_ID="20230201"
HOME_URL="https://wolfi.dev"
ce557598406a:/# apk update
fetch https://packages.wolfi.dev/os/aarch64/APKINDEX.tar.gz
 [https://packages.wolfi.dev/os]
OK: 15046 distinct packages available
ce557598406a:/# curl
/bin/sh: curl: not found
ce557598406a:/# apk add curl
(1/5) Installing libbrotlicommon1 (1.0.9-r3)
(2/5) Installing libbrotlidec1 (1.0.9-r3)
(3/5) Installing libnghttp2-14 (1.55.1-r0)
(4/5) Installing libcurl-openssl4 (8.2.1-r0)
(5/5) Installing curl (8.2.1-r0)
OK: 13 MiB in 19 packages
ce557598406a:/# curl google.com
...
```
