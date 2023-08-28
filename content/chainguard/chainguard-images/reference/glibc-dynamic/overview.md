---
title: "Image Overview: glibc-dynamic"
type: "article"
description: "Overview: glibc-dynamic Chainguard Image"
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

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | August 26th  | `sha256:82e81ff2757c3a6bc05a390042c1858c0ca5a055444d2c8d50d3227df22d925c` |
|  `latest`     | August 4th   | `sha256:652ca01119b8ff8aa590384eadb840fb1145fca9ceb87f77e6df48601037a846` |



Base image with just enough to run arbitrary glibc binaries.

This image is meant to be used as just a base image only. It does not contain any programs that can be run, other than `/sbin/ldconfig`.

You must bring your own artifacts to use this image, e.g. with a Docker multi-stage build. If you want locale support other than `C.UTF-8`, you must bring your own locale data as well. This may change in the future based on user feedback.

See also [musl-dynamic](https://github.com/chainguard-images/images/tree/main/images/musl-dynamic) which is an equivalent image for running dynamically-linked musl binaries.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/glibc-dynamic:latest
```

