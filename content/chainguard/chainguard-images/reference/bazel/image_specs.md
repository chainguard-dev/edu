---
title: "bazel Image Variants"
type: "article"
description: "Detailed specs for bazel Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "bazel"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **bazel** Image.

## Variants Compared
The **bazel** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest           |
|--------------|------------------|
| Default User | `bazel`          |
| Entrypoint   | `/usr/bin/bazel` |
| CMD          | not specified    |
| Workdir      | `/home/bazel`    |
| Has apk?     | no               |
| Has a shell? | yes              |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest |
|--------------------------|--------|
| `ca-certificates-bundle` | X      |
| `openjdk-17`             | X      |
| `bash`                   | X      |
| `busybox`                | X      |
| `gcc`                    | X      |
| `git`                    | X      |
| `bazel-6`                | X      |
| `wolfi-baselayout`       | X      |

