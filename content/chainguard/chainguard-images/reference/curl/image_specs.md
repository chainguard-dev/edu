---
title: "Curl Public Image Variants"
type: "article"
description: "Detailed information about the public Curl Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Curl"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **Curl** Image.

## Variants Compared
The **curl** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest          |
|--------------|-----------------|
| Default User | `curl`          |
| Entrypoint   | `/usr/bin/curl` |
| CMD          | not specified   |
| Workdir      | not specified   |
| Has apk?     | no              |
| Has a shell? | no              |

Check the [tags history page](/chainguard/chainguard-images/reference/curl/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest |
|--------------------------|--------|
| `ca-certificates-bundle` | X      |
| `curl`                   | X      |
| `glibc`                  | X      |
| `glibc-locale-posix`     | X      |
| `ld-linux`               | X      |
| `libbrotlicommon1`       | X      |
| `libbrotlidec1`          | X      |
| `libcurl-rustls4`        | X      |
| `libgcc`                 | X      |
| `libnghttp2-14`          | X      |
| `wolfi-baselayout`       | X      |
| `zlib`                   | X      |
