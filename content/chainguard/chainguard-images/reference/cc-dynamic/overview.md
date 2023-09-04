---
title: "Image Overview: cc-dynamic"
type: "article"
description: "Overview: cc-dynamic Chainguard Image"
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

[cgr.dev/chainguard/cc-dynamic](https://github.com/chainguard-images/images/tree/main/images/cc-dynamic)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | August 31st  | `sha256:bacd35b7bc4461e642752e02b78037a390b54535e31e115396f0eb9b3f0115f4` |
|  `latest`     | August 31st  | `sha256:3e98234383b7e953285a7cc5364facb294a2a2c506bab4ec7352b090ac966ca6` |



Base image with just enough to run arbitrary binaries that may require gcc or cc libraries.
These are typically C++ or Rust binaries.

This image is meant to be used as just a base image only. It does not contain any programs that can be run, other than `/sbin/ldconfig`.

You must bring your own artifacts to use this image, e.g. with a Docker multi-stage build. If you want locale support other than `C.UTF-8`, you must bring your own locale data as well. This may change in the future based on user feedback.

This image is deprecated.  Use the `glibc-dynamic` image instead which is designed to cover the same use cases.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/cc-dynamic:latest
```

