---
title: "powershell Image Variants"
type: "article"
description: "Detailed specs for powershell Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "powershell"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **powershell** Image.

## Variants Compared
The **powershell** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-root`

The table has detailed information about each of these variants.

|              | latest          | latest-root     |
|--------------|-----------------|-----------------|
| Default User | `nonroot`       | `root`          |
| Entrypoint   | `/usr/bin/pwsh` | `/usr/bin/pwsh` |
| CMD          | not specified   | not specified   |
| Workdir      | not specified   | not specified   |
| Has apk?     | no              | no              |
| Has a shell? | yes             | yes             |

## Image Dependencies
The table shows package distribution across all variants.

|                    | latest | latest-root |
|--------------------|--------|-------------|
| `busybox`          | X      | X           |
| `powershell`       | X      | X           |
| `wolfi-baselayout` | X      | X           |

