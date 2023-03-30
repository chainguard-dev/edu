---
title: "kubectl Image Variants"
type: "article"
description: "Detailed specs for kubectl Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "kubectl"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **kubectl** Image.

## Variants Compared
The **kubectl** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest             |
|--------------|--------------------|
| Default User | `nonroot`          |
| Entrypoint   | `/usr/bin/kubectl` |
| CMD          | `help`             |
| Workdir      | not specified      |
| Has apk?     | no                 |
| Has a shell? | yes                |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest |
|--------------------------|--------|
| `ca-certificates-bundle` | X      |
| `busybox`                | X      |
| `kubectl`                | X      |
| `wolfi-baselayout`       | X      |

