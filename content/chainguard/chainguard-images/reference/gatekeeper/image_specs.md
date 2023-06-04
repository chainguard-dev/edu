---
title: "gatekeeper Image Variants"
type: "article"
description: "Detailed specs for gatekeeper Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "gatekeeper"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **gatekeeper** Image.

## Variants Compared
The **gatekeeper** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest        | latest-dev    |
|--------------|---------------|---------------|
| Default User | `nonroot`     | `nonroot`     |
| Entrypoint   | `manager`     | `manager`     |
| CMD          | `--help`      | `--help`      |
| Workdir      | not specified | not specified |
| Has apk?     | no            | yes           |
| Has a shell? | no            | yes           |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `wolfi-baselayout`       | X      | X          |
| `ca-certificates-bundle` | X      | X          |
| `gatekeeper`             | X      | X          |
| `gatekeeper-compat`      | X      | X          |
| `apk-tools`              |        | X          |
| `bash`                   |        | X          |
| `busybox`                |        | X          |
| `git`                    |        | X          |

