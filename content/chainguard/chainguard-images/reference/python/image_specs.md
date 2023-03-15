---
title: "python Image Variants"
type: "article"
description: "Detailed specs for python Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "python"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **python** Image.

## Variants Compared
The **python** Chainguard Image currently has 2 public variants: 

- `3.10`
- `latest`

The table has detailed information about each of these variants.

|              | 3.10              | latest            |
|--------------|-------------------|-------------------|
| Default User | `nonroot`         | `nonroot`         |
| Entrypoint   | `/usr/bin/python` | `/usr/bin/python` |
| CMD          | not specified     | not specified     |
| Workdir      | not specified     | not specified     |
| Has apk?     | no                | no                |
| Has a shell? | no                | no                |

## Image Dependencies
The table shows package distribution across all variants.

|                          | 3.10 | latest |
|--------------------------|------|--------|
| `ca-certificates-bundle` | X    | X      |
| `python-3.10`            | X    |        |
| `wolfi-baselayout`       | X    | X      |
| `python-3.11`            |      | X      |
