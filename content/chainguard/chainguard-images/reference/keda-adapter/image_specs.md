---
title: "keda-adapter Image Variants"
type: "article"
description: "Detailed information about the public keda-adapter Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "keda-adapter"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **keda-adapter** Image.

## Variants Compared
The **keda-adapter** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                                                          | latest                                                              |
|--------------|---------------------------------------------------------------------|---------------------------------------------------------------------|
| Default User | `nonroot`                                                           | `nonroot`                                                           |
| Entrypoint   | `/usr/bin/keda-adapter --secure-port=6443 --logtostderr=true --v=0` | `/usr/bin/keda-adapter --secure-port=6443 --logtostderr=true --v=0` |
| CMD          | not specified                                                       | not specified                                                       |
| Workdir      | not specified                                                       | not specified                                                       |
| Has apk?     | yes                                                                 | no                                                                  |
| Has a shell? | yes                                                                 | yes                                                                 |

Check the [tags history page](/chainguard/chainguard-images/reference/keda-adapter/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          |        |
| `busybox`                | X          | X      |
| `ca-certificates-bundle` | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `keda-adapter`           | X          | X      |
| `keda-compat`            | X          | X      |
| `ld-linux`               | X          | X      |
| `libbrotlicommon1`       | X          |        |
| `libbrotlidec1`          | X          |        |
| `libcrypt1`              | X          | X      |
| `libcrypto3`             | X          |        |
| `libcurl-openssl4`       | X          |        |
| `libexpat1`              | X          |        |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libssl3`                | X          |        |
| `ncurses`                | X          |        |
| `ncurses-terminfo-base`  | X          |        |
| `openssl-config`         | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `zlib`                   | X          |        |
