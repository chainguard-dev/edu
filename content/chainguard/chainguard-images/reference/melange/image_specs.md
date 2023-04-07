---
title: "melange Image Variants"
type: "article"
description: "Detailed specs for melange Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "melange"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **melange** Image.

## Variants Compared
The **melange** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest             |
|--------------|--------------------|
| Default User | `root`             |
| Entrypoint   | `/usr/bin/melange` |
| CMD          | `--help`           |
| Workdir      | `/work`            |
| Has apk?     | yes                |
| Has a shell? | yes                |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest |
|--------------------------|--------|
| `alpine-keys`            | X      |
| `ca-certificates-bundle` | X      |
| `wolfi-base`             | X      |
| `bubblewrap`             | X      |
| `melange`                | X      |
| `wolfi-baselayout`       | X      |

