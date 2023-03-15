---
title: "Image Overview: cc-dynamic"
type: "article"
description: "Overview: cc-dynamic Chainguard Images"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "images-reference"
weight: 500
toc: true
---

`stable` [cgr.dev/chainguard/cc-dynamic](https://github.com/chainguard-images/images/tree/main/images/cc-dynamic)
| Tags     | Aliases |
|----------|---------|
| `latest` |         |



Base image with just enough to run arbitrary binaries that may require gcc or cc libraries.
These are typically C++ or Rust binaries.

This image is meant to be used as just a base image only. It does not contain any programs that can be run, other than `/sbin/ldconfig`.

You must bring your own artifacts to use this image, e.g. with a Docker multi-stage build. If you want locale support other than `C.UTF-8`, you must bring your own locale data as well. This may change in the future based on user feedback.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/cc-dynamic:latest
```
