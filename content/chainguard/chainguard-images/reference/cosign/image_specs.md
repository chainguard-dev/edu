---
title: "cosign Image Variants"
type: "article"
description: "Detailed specs for cosign Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "cosign"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **cosign** Image.

## Variants Compared
The **cosign** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest            |
|--------------|-------------------|
| Default User | `nonroot`         |
| Entrypoint   | `/usr/bin/cosign` |
| CMD          | `help`            |
| Workdir      | not specified     |
| Has apk?     | no                |
| Has a shell? | yes               |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest |
|--------------------------|--------|
| `ca-certificates-bundle` | X      |
| `busybox`                | X      |
| `cosign`                 | X      |
| `wolfi-baselayout`       | X      |
