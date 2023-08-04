---
title: "Image Overview: graalvm-native"
type: "article"
description: "Overview: graalvm-native Chainguard Image"
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

[cgr.dev/chainguard/graalvm-native](https://github.com/chainguard-images/images/tree/main/images/graalvm-native)

| Tag (s)   | Last Changed | Digest                                                                    |
|-----------|--------------|---------------------------------------------------------------------------|
|  `latest` | August 3rd   | `sha256:64e2205c3b0a8fd7950d830e68a2ae373fd806e6e7d4e9609d5b383cde5f4ceb` |



Base image with just enough files to run native GraalVM native-image binaries.

This image includes `glibc` and `libz`, and is designed to contain exactly what's needed to run GraalVM native-image binaries.

This image is meant to be used as a base image only, and is otherwise useless.  It contains the `wolfi-baselayout-data` package from Wolfi, which is just a set of data files needed to support glibc static binaries at runtime.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/graalvm-native:latest
```

## Users

The image has a single user `nonroot` with uid `65532`, belonging to gid `65532`.

