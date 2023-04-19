---
title: "zot Image Variants"
type: "article"
description: "Detailed specs for zot Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "zot"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **zot** Image.

## Variants Compared
The **zot** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest         | latest-dev     |
|--------------|----------------|----------------|
| Default User | `nonroot`      | `nonroot`      |
| Entrypoint   | `/usr/bin/zot` | `/usr/bin/zot` |
| CMD          | `--help`       | `--help`       |
| Workdir      | not specified  | not specified  |
| Has apk?     | no             | yes            |
| Has a shell? | no             | yes            |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `ca-certificates-bundle` | X      | X          |
| `zot`                    | X      | X          |
| `wolfi-baselayout`       | X      | X          |
| `apk-tools`              |        | X          |
| `bash`                   |        | X          |
| `busybox`                |        | X          |
| `git`                    |        | X          |

