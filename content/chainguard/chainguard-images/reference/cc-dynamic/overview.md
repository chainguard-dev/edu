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
|  `latest-dev` | July 27th    | `sha256:64d1b8955a4cd458d4f693b03aee5e6ad30c487e4815d129dd133a947bb5d60f` |
|  `latest`     | July 26th    | `sha256:de46baee7b0f3a57490cf9ceed9493beb8f3e7883e3467bb651a2c3c6c713f0d` |



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

