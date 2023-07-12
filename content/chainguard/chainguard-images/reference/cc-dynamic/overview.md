---
title: "Image Overview: Cc-dynamic"
type: "article"
description: "Overview: Cc-dynamic Chainguard Image"
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

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest-dev` | 20 hours ago | `sha256:e0aad14b57e7ba41e51eccfe93d6bac3c928a34cb2d8e056a69869e074f83f01` |
| `latest`     | 20 hours ago | `sha256:fdb7305a66e1c254bfc248d5e4a65b254dc7c5dcc1e6cdb97b391efb3bfcc1b1` |



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
