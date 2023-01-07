---
title: "busybox"
hide_title: yes
type: "article"
description: "Reference docs for the busybox Chainguard Image"
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
# busybox
| | |
| - | - |
| **Status** | stable |
| **OCI Reference** | `cgr.dev/chainguard/busybox` |
| **Variants/Tags** | `latest`, `latest-glibc` |
---
<!--monopod:end-->

Container image with only busybox and libc (available in both musl and glibc variants). Suitable for running any binaries that only have a dependency on glibc/musl.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/busybox:latest
```
