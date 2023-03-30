---
title: "apko Image Variants"
type: "article"
description: "Detailed specs for apko Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "apko"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **apko** Image.

## Variants Compared
The **apko** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest          |
|--------------|-----------------|
| Default User | `root`          |
| Entrypoint   | `/usr/bin/apko` |
| CMD          | `--help`        |
| Workdir      | `/work`         |
| Has apk?     | yes             |
| Has a shell? | yes             |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest |
|--------------------------|--------|
| `ca-certificates-bundle` | X      |
| `wolfi-base`             | X      |
| `alpine-keys`            | X      |
| `apko`                   | X      |

