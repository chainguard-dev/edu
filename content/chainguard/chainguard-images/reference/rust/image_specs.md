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
The **rust** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest           | latest-dev       |
|--------------|------------------|------------------|
| Default User | `nonroot`        | `nonroot`        |
| Entrypoint   | `/usr/bin/rustc` | `/usr/bin/rustc` |
| CMD          | `--help`         | `--help`         |
| Workdir      | `/work`          | `/work`          |
| Has apk?     | no               | yes              |
| Has a shell? | yes              | yes              |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `wolfi-baselayout`       | X      | X          |
| `ca-certificates-bundle` | X      | X          |
| `busybox`                | X      | X          |
| `rust`                   | X      | X          |
| `build-base`             | X      | X          |
| `apk-tools`              |        | X          |
| `bash`                   |        | X          |
| `git`                    |        | X          |
| `rustup`                 |        | X          |

