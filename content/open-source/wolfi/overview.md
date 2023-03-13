---
title: "Wolfi Overview"
type: "article"
description: "Getting started with Wolfi, the Linux undistro for secure container images"
lead: "Introducing Wolfi, the Linux undistro for secure container images"
date: 2022-09-01T08:49:31+00:00
lastmod: 2022-09-01T08:49:31+00:00
draft: false
tags: ["WOLFI", "OVERVIEW"]
images: []
menu:
  docs:
    parent: "wolfi"
weight: 100
toc: true
---
[Wolfi](https://github.com/wolfi-dev) is a community Linux [undistro](#why-undistro) designed for the container and cloud-native era. Chainguard started the Wolfi project to enable building  [Chainguard Images](/chainguard/chainguard-images/overview), our collection of curated [distroless]( https://blog.chainguard.dev/minimal-container-images-towards-a-more-secure-future/)  images that meet the requirements of a secure software supply chain. This required a Linux distribution with components at the appropriate granularity and with support for both [glibc](https://www.gnu.org/software/libc/) and [musl](https://www.musl-libc.org/), something that was not yet available in the cloud-native Linux ecosystem.

Building our own undistro also allows us to ensure packages have full provenance and metadata for supporting modern supply-chain security needs.

## Why Undistro

We call Wolfi an undistro because unlike a [typical Linux distribution](https://en.wikipedia.org/wiki/Linux_distribution) designed to run on bare-metal, Wolfi is a stripped-down distro designed for the cloud-native era. It doesn't have a kernel of its own, instead relying on the environment (such as the container runtime) to provide one. This separation of concerns in Wolfi means it is adaptable to a range of environments.

Wolfi is the base we use to build [Chainguard Images](/chainguard/chainguard-images/overview), our open source distroless images that are available free of charge.

## Wolfi Features

Wolfi, whose name was inspired by the [world's smallest octopus](https://en.wikipedia.org/wiki/Octopus_wolfi), has some key features that differentiates it from other distributions that focus on container/cloud-native environments:

- Provides a high-quality, build-time SBOM as standard for all packages
- Packages are designed to be granular and independent, to support minimal images
- Uses the proven and reliable apk package format
- Fully declarative and reproducible build system
- Designed to support glibc and musl

Wolfi enables Chainguard to solve the software supply chain security problem from the outside in. It gives developers the secure-by-default base they need to build software, it scales to support organizations running massive environments and provides the control needed to fix most modern supply chain threats. Wolfi builds all packages directly from source, allowing us to fix vulnerabilities or apply customizations that improve the supply chain security posture of everything from compilers to language package managers.
