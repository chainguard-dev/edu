---
title: "gradle Image Variants"
type: "article"
description: "Detailed specs for gradle Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "gradle"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **gradle** Image.

## Variants Compared
The **gradle** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest            |
|--------------|-------------------|
| Default User | `gradle`          |
| Entrypoint   | `/usr/bin/gradle` |
| CMD          | not specified     |
| Workdir      | `/home/build`     |
| Has apk?     | no                |
| Has a shell? | yes               |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest |
|--------------------------|--------|
| `ca-certificates-bundle` | X      |
| `wolfi-baselayout`       | X      |
| `glibc-locale-en`        | X      |
| `busybox`                | X      |
| `gradle-8`               | X      |
