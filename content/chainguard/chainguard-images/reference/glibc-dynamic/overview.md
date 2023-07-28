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
|  `latest-dev` | July 27th    | `sha256:1d8c8c96430721522d5e651b26fc19f7c1c94f61b09a7d7037757d6faf0e6e56` |
|  `latest`     | July 26th    | `sha256:9876aed3271b116aed70bd4c37d5e94bbf13940e440c29783a1e0886f96fee20` |



Base image with just enough to run arbitrary glibc binaries.

This image is meant to be used as just a base image only. It does not contain any programs that can be run, other than `/sbin/ldconfig`.

You must bring your own artifacts to use this image, e.g. with a Docker multi-stage build. If you want locale support other than `C.UTF-8`, you must bring your own locale data as well. This may change in the future based on user feedback.

See also [musl-dynamic](https://github.com/chainguard-images/images/tree/main/images/musl-dynamic) which is an equivalent image for running dynamically-linked musl binaries.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/glibc-dynamic:latest
```

