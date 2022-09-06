---
title: "Overview"
type: "article"
description: "Chainguard Images Overview"
lead: "A primer on Chainguard images and the distroless philosophy"
date: 2022-09-01T08:49:31+00:00
lastmod: 2022-09-01T08:49:31+00:00
contributors: ["Erika Heidi"]
draft: false
images: []
menu:
  docs:
    parent: "chainguard-images"
weight: 100
toc: true
---

Chainguard images are minimalist, distroless images powered by [Wolfi](/open-source/wolfi/getting-started-with-wolfi), our Linux _undistro_ designed from the ground up to produce container images that meet the requirements of a secure software supply chain.

## Why Distroless

_Distroless_ is a type of container image that includes only the bare minimum to build and/or execute production-ready applications and runtime environments.

Unlike traditional container images that are built layer-by-layer and carry on an unnecessary amount of tools and software, distroless images have a much smaller footprint, which results in a smaller surface of attack and less potential vulnerabilities.

Although many users will consider the typically smaller image size as an important reason to migrate to distroless images, the reduced number of CVEs detected in such images is a crucial advantage of choosing distroless over traditional images.
