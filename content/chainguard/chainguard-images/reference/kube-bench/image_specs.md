---
title: "kube-bench Image Variants"
type: "article"
description: "Detailed specs for kube-bench Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "kube-bench"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **kube-bench** Image.

## Variants Compared
The **kube-bench** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                |
|--------------|-----------------------|
| Default User | `root`                |
| Entrypoint   | `/usr/bin/kube-bench` |
| CMD          | `help`                |
| Workdir      | `/etc/kube-bench`     |
| Has apk?     | no                    |
| Has a shell? | no                    |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest |
|--------------------------|--------|
| `wolfi-baselayout`       | X      |
| `ca-certificates-bundle` | X      |
| `procps`                 | X      |
| `kube-bench`             | X      |
| `kube-bench-configs`     | X      |

