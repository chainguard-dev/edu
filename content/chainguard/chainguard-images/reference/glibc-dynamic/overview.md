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
|  `latest-dev` | July 19th    | `sha256:00c3ce1ab854c0aec92c5dc709893088bc5bb3f27d466c55568f66d888063584` |
|  `latest`     | July 11th    | `sha256:84330a5c2f3b425a77320bc599a6a813fa986aab9b6a0fd7f58d753d6fe2143e` |



Base image with just enough to run arbitrary glibc binaries.

This image is meant to be used as just a base image only. It does not contain any programs that can be run, other than `/sbin/ldconfig`.

You must bring your own artifacts to use this image, e.g. with a Docker multi-stage build. If you want locale support other than `C.UTF-8`, you must bring your own locale data as well. This may change in the future based on user feedback.

See also [musl-dynamic](https://github.com/chainguard-images/images/tree/main/images/musl-dynamic) which is an equivalent image for running dynamically-linked musl binaries.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/glibc-dynamic:latest
```

