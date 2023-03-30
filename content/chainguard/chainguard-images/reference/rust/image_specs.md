---
title: "rust Image Variants"
type: "article"
description: "Detailed specs for rust Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "rust"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **rust** Image.

## Variants Compared
The **rust** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest           |
|--------------|------------------|
| Default User | `nonroot`        |
| Entrypoint   | `/usr/bin/rustc` |
| CMD          | `--help`         |
| Workdir      | `/work`          |
| Has apk?     | no               |
| Has a shell? | yes              |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest |
|--------------------------|--------|
| `wolfi-baselayout`       | X      |
| `ca-certificates-bundle` | X      |
| `busybox`                | X      |
| `rust`                   | X      |
| `build-base`             | X      |

