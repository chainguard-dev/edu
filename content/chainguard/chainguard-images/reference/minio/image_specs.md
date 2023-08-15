---
title: "Minio Public Image Variants"
type: "article"
description: "Detailed information about the public Minio Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Minio"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **Minio** Image.

## Variants Compared
The **minio** Chainguard Image currently has 4 public variants: 

- `client-latest-dev`
- `client-latest`
- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | client-latest-dev | client-latest | latest-dev       | latest           |
|--------------|-------------------|---------------|------------------|------------------|
| Default User | `minio`           | `minio`       | `minio`          | `minio`          |
| Entrypoint   | `/usr/bin/mc`     | `/usr/bin/mc` | `/usr/bin/minio` | `/usr/bin/minio` |
| CMD          | not specified     | not specified | not specified    | not specified    |
| Workdir      | not specified     | not specified | not specified    | not specified    |
| Has apk?     | yes               | no            | yes              | no               |
| Has a shell? | yes               | yes           | yes              | no               |

Check the [tags history page](/chainguard/chainguard-images/reference/minio/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | client-latest-dev | client-latest | latest-dev | latest |
|--------------------------|-------------------|---------------|------------|--------|
| `apk-tools`              | X                 |               | X          |        |
| `bash`                   | X                 | X             | X          |        |
| `busybox`                | X                 |               | X          |        |
| `ca-certificates-bundle` | X                 | X             | X          | X      |
| `git`                    | X                 |               | X          |        |
| `glibc`                  | X                 | X             | X          |        |
| `glibc-locale-posix`     | X                 | X             | X          |        |
| `ld-linux`               | X                 | X             | X          |        |
| `libbrotlicommon1`       | X                 |               | X          |        |
| `libbrotlidec1`          | X                 |               | X          |        |
| `libcrypt1`              | X                 |               | X          |        |
| `libcrypto3`             | X                 |               | X          |        |
| `libcurl-openssl4`       | X                 |               | X          |        |
| `libexpat1`              | X                 |               | X          |        |
| `libnghttp2-14`          | X                 |               | X          |        |
| `libpcre2-8-0`           | X                 |               | X          |        |
| `libssl3`                | X                 |               | X          |        |
| `mc`                     | X                 | X             |            |        |
| `ncurses`                | X                 | X             | X          |        |
| `ncurses-terminfo-base`  | X                 | X             | X          |        |
| `openssl-config`         | X                 |               | X          |        |
| `wolfi-baselayout`       | X                 | X             | X          | X      |
| `zlib`                   | X                 |               | X          |        |
| `minio`                  |                   |               | X          | X      |
