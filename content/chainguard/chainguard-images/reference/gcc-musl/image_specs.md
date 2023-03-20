---
title: "gcc-musl Image Variants"
type: "article"
description: "Detailed specs for gcc-musl Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "gcc-musl"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **gcc-musl** Image.

## Variants Compared
The **gcc-musl** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest         |
|--------------|----------------|
| Default User | `root`         |
| Entrypoint   | `/usr/bin/gcc` |
| CMD          | `--help`       |
| Workdir      | `/work`        |
| Has apk?     | no             |
| Has a shell? | yes            |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest |
|--------------------------|--------|
| `ca-certificates-bundle` | X      |
| `alpine-baselayout-data` | X      |
| `alpine-release`         | X      |
| `gcc`                    | X      |
| `musl-dev`               | X      |
| `busybox`                | X      |
