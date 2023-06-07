---
title: "buck2 Image Variants"
type: "article"
description: "Detailed specs for buck2 Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "buck2"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **buck2** Image.

## Variants Compared
The **buck2** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest           | latest-dev       |
|--------------|------------------|------------------|
| Default User | `nonroot`        | `nonroot`        |
| Entrypoint   | `/usr/bin/buck2` | `/usr/bin/buck2` |
| CMD          | `help`           | `help`           |
| Workdir      | not specified    | not specified    |
| Has apk?     | no               | yes              |
| Has a shell? | yes              | yes              |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `ca-certificates-bundle` | X      | X          |
| `buck2`                  | X      | X          |
| `build-base`             | X      | X          |
| `wolfi-baselayout`       | X      | X          |
| `bash`                   | X      | X          |
| `busybox`                | X      | X          |
| `clang-15`               | X      | X          |
| `git`                    | X      | X          |
| `llvm-lld`               | X      | X          |
| `apk-tools`              |        | X          |

