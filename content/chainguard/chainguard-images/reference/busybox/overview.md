---
title: "Image Overview: busybox"
type: "article"
description: "Overview: busybox Chainguard Images"
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

`stable` [cgr.dev/chainguard/busybox](cgr.dev/chainguard/busybox)
| Tags           | Aliases                                         |
|----------------|-------------------------------------------------|
| `latest`       | 1, 1.36, 1.36.0, 1.36.0-r1                      |
| `latest-glibc` | glibc-1, glibc-1.35, glibc-1.35.0, glibc-1.35.0 |



Container image with only busybox and libc (available in both musl and glibc variants). Suitable for running any binaries that only have a dependency on glibc/musl.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/busybox:latest
```
