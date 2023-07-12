---
title: "Image Overview: Glibc-dynamic"
type: "article"
description: "Overview: Glibc-dynamic Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "images-reference"
weight: 500
toc: true
---

[cgr.dev/chainguard/glibc-dynamic](https://github.com/chainguard-images/images/tree/main/images/glibc-dynamic)

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest`     | 20 hours ago | `sha256:84330a5c2f3b425a77320bc599a6a813fa986aab9b6a0fd7f58d753d6fe2143e` |
| `latest-dev` | 20 hours ago | `sha256:cc4400fa6dcf522db3243e0bca42d75182bc893513cd650b4c68b8d8a723ded7` |



Base image with just enough to run arbitrary glibc binaries.

This image is meant to be used as just a base image only. It does not contain any programs that can be run, other than `/sbin/ldconfig`.

You must bring your own artifacts to use this image, e.g. with a Docker multi-stage build. If you want locale support other than `C.UTF-8`, you must bring your own locale data as well. This may change in the future based on user feedback.

See also [musl-dynamic](https://github.com/chainguard-images/images/tree/main/images/musl-dynamic) which is an equivalent image for running dynamically-linked musl binaries.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/glibc-dynamic:latest
```
