---
title: "melange Overview"
type: "article"
description: "melange Overview"
date: 2022-10-17T11:07:52+02:00
lastmod: 2022-17-10T11:07:52+02:00
draft: false
tags: ["MELANGE", "OVERVIEW"]
images: []
menu:
  docs:
    parent: "melange"
weight: 10
toc: true
---
[melange](https://github.com/chainguard-dev/melange) is an [apk](https://wiki.alpinelinux.org/wiki/Package_management) builder tool that uses declarative pipelines to create apk packages.
From a single YAML file, users are able to generate multi-architecture apks that can be injected directly into [apko](https://github.com/chainguard-dev/apko) builds. This renders apko and melange a [good combination for container image factories](https://blog.chainguard.dev/secure-your-software-factory-with-melange-and-apko/).

The following diagram contains an overview of the apko and melange ecosystem and how they work together to compose apk-based images, using either Alpine or Wolfi as base system.

![The diagram shows an overview of the apko and melange ecosystem and their relationships. melange apks can be used to compose both Alpine-based and Wolfi-based container images using apko.](apko_melange_ecosystem.png)

melange offers the following features:

- **Fully reproducible by default.** Run melange twice and you will get exactly the same binary.
- **Pipeline-oriented builds.** Every step of the build pipeline is defined and controlled by you, unlike traditional package managers which have distinct phases.
- **Multi-architecture by default.** QEMU is used to emulate various architectures, avoiding the need for cross-compilation steps.

apko and [melange](/open-source/melange) are part of the open source toolkit developed by Chainguard to build [Wolfi](/open-source/wolfi) and [Chainguard Images](/chainguard/chainguard-images).
