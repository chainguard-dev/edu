---
title: "Image Overview: musl-dynamic"
type: "article"
description: "Overview: musl-dynamic Chainguard Images"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "images-reference"
weight: 600
toc: true
---

<!--monopod:start-->

| | |
| - | - |
| **Status** | stable |
| **OCI Reference** | `cgr.dev/chainguard/musl-dynamic` |
| **Variants/Tags** | ![](https://storage.googleapis.com/chainguard-images-build-outputs/summary/musl-dynamic.svg) |
---
<!--monopod:end-->

Base image with just enough files to run static binaries!

This image is meant to be used as a base image only, and is otherwise useless. It contains the `alpine-baselayout-data` package from Alpine, which is just a set of data files needed to support glibc and musl static binaries at runtime.

This image can be used with `ko build`, `docker`, etc, but is only suitable for running static binaries.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/musl-dynamic:latest
```
# Usage

See the [examples/](./examples/) directory for
an example C program and associated Dockerfile
that can be used with this image.
