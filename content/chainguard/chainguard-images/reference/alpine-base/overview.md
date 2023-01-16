---
title: "Image Overview: alpine-base"
type: "article"
description: "Overview: alpine-base Chainguard Images"
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

| | |
| - | - |
| **Status** | stable |
| **OCI Reference** | `cgr.dev/chainguard/alpine-base` |
| **Variants/Tags** | ![](https://storage.googleapis.com/chainguard-images-build-outputs/summary/alpine-base.svg) |
---
<!--monopod:end-->

Alpine base image built with [apko](https://github.com/chainguard-dev/apko). Uses packages from the [Alpine distribution](https://www.alpinelinux.org/).

```
docker run cgr.dev/chainguard/alpine-base echo "hello"
```

See the [examples/](./examples/) directory for how
to use this as a base image.
