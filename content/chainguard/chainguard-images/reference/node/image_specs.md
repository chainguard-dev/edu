---
title: "node Image Variants"
type: "article"
description: "Detailed specs for node Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "node"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **node** Image.

## Variants Compared
The **node** Chainguard Image currently has 2 public variants: 

- `latest`
- `19`

The table has detailed information about each of these variants.

|              | latest          | 19              |
|--------------|-----------------|-----------------|
| Default User | `node`          | `node`          |
| Entrypoint   | `/usr/bin/node` | `/usr/bin/node` |
| CMD          | `--help`        | `--help`        |
| Workdir      | `/app`          | `/app`          |
| Has apk?     | no              | no              |
| Has a shell? | yes             | yes             |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | 19 |
|--------------------------|--------|----|
| `busybox`                | X      | X  |
| `ca-certificates-bundle` | X      | X  |
| `nghttp2`                | X      | X  |
| `nodejs`                 | X      |    |
| `wolfi-baselayout`       | X      | X  |
| `nodejs-19`              |        | X  |
