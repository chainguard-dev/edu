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
|  `latest-dev` | August 4th   | `sha256:47e73dfe664e342a3c6854b9bba891cb8fdb23e555d2beb08876c0bdacee613a` |
|  `latest`     | August 4th   | `sha256:8f87825d5cacfb0af01c0e88acadb3fd630167a5acf41b7c1ae65dfda7e61ebf` |



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

