---
title: "tigera-operator Image Variants"
type: "article"
description: "Detailed specs for tigera-operator Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "tigera-operator"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **tigera-operator** Image.

## Variants Compared
The **tigera-operator** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest              | latest-dev          |
|--------------|---------------------|---------------------|
| Default User | `tigera-operator`   | `tigera-operator`   |
| Entrypoint   | `/usr/bin/operator` | `/usr/bin/operator` |
| CMD          | `--help`            | `--help`            |
| Workdir      | not specified       | not specified       |
| Has apk?     | no                  | yes                 |
| Has a shell? | no                  | yes                 |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `wolfi-baselayout`       | X      | X          |
| `ca-certificates-bundle` | X      | X          |
| `tigera-operator`        | X      | X          |
| `glibc`                  | X      | X          |
| `apk-tools`              |        | X          |
| `bash`                   |        | X          |
| `busybox`                |        | X          |
| `git`                    |        | X          |

