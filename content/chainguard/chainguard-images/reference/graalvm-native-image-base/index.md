---
title: "graalvm-native-image-base"
hide_title: yes
type: "article"
description: "Reference docs for the graalvm-native-image-base Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "images-reference"
weight: 600
toc: true
---

<!--monopod:start-->
# graalvm-native-image-base
| | |
| - | - |
| **Status** | experimental |
| **OCI Reference** | `cgr.dev/chainguard/graalvm-native-image-base` |
| **Variants/Tags** | `latest` |
---
<!--monopod:end-->

Base image with just enough files to run native GraalVM native-image binaries.

This image includes `glibc` and `libz`, and is designed to contain exactly what's needed to run GraalVM native-image binaries.

This image is meant to be used as a base image only, and is otherwise useless.  It contains the `wolfi-baselayout-data` package from Wolfi, which is just a set of data files needed to support glibc static binaries at runtime.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/graalvm-native-image-base:latest
```

## Users

The image has a single user `nonroot` with uid `65532`, belonging to gid `65532`.
