---
title: "k8s-sidecar Image Variants"
type: "article"
description: "Detailed information about the public k8s-sidecar Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "k8s-sidecar"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **k8s-sidecar** Image.

## Variants Compared
The **k8s-sidecar** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                            | latest                                |
|--------------|---------------------------------------|---------------------------------------|
| Default User | `65532`                               | `65532`                               |
| Entrypoint   | `python -u /usr/share/app/sidecar.py` | `python -u /usr/share/app/sidecar.py` |
| CMD          | not specified                         | not specified                         |
| Workdir      | not specified                         | not specified                         |
| Has apk?     | yes                                   | no                                    |
| Has a shell? | yes                                   | yes                                   |

Check the [tags history page](/chainguard/chainguard-images/reference/k8s-sidecar/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          |        |
| `busybox`                | X          | X      |
| `ca-certificates-bundle` | X          | X      |
| `gdbm`                   | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `k8s-sidecar`            | X          | X      |
| `ld-linux`               | X          | X      |
| `libbrotlicommon1`       | X          |        |
| `libbrotlidec1`          | X          |        |
| `libbz2-1`               | X          | X      |
| `libcrypt1`              | X          | X      |
| `libcrypto3`             | X          | X      |
| `libcurl-openssl4`       | X          |        |
| `libexpat1`              | X          | X      |
| `libffi`                 | X          | X      |
| `libgcc`                 | X          | X      |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libssl3`                | X          | X      |
| `libstdc++`              | X          | X      |
| `mpdecimal`              | X          | X      |
| `ncurses`                | X          | X      |
| `ncurses-terminfo-base`  | X          | X      |
| `openssl-config`         | X          | X      |
| `python-3.11`            | X          | X      |
| `readline`               | X          | X      |
| `sqlite-libs`            | X          | X      |
| `wolfi-baselayout`       | X          | X      |
| `xz`                     | X          | X      |
| `zlib`                   | X          | X      |
