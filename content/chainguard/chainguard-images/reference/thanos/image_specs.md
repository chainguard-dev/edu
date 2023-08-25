---
title: "thanos Image Variants"
type: "article"
description: "Detailed information about the public thanos Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "thanos"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **thanos** Image.

## Variants Compared
The **thanos** Chainguard Image currently has 4 public variants: 

- `latest-dev`
- `latest`
- `operator-latest-dev`
- `operator-latest`

The table has detailed information about each of these variants.

|              | latest-dev    | latest        | operator-latest-dev | operator-latest    |
|--------------|---------------|---------------|---------------------|--------------------|
| Default User | `thanos`      | `thanos`      | `nonroot`           | `nonroot`          |
| Entrypoint   | `thanos`      | `thanos`      | `/usr/bin/manager`  | `/usr/bin/manager` |
| CMD          | not specified | not specified | not specified       | not specified      |
| Workdir      | not specified | not specified | not specified       | not specified      |
| Has apk?     | yes           | no            | yes                 | no                 |
| Has a shell? | yes           | no            | yes                 | no                 |

Check the [tags history page](/chainguard/chainguard-images/reference/thanos/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest | operator-latest-dev | operator-latest |
|--------------------------|------------|--------|---------------------|-----------------|
| `apk-tools`              | X          |        | X                   |                 |
| `bash`                   | X          |        | X                   |                 |
| `busybox`                | X          |        | X                   |                 |
| `ca-certificates-bundle` | X          | X      | X                   | X               |
| `git`                    | X          |        | X                   |                 |
| `glibc`                  | X          |        | X                   | X               |
| `glibc-locale-posix`     | X          |        | X                   | X               |
| `ld-linux`               | X          |        | X                   | X               |
| `libbrotlicommon1`       | X          |        | X                   |                 |
| `libbrotlidec1`          | X          |        | X                   |                 |
| `libcrypt1`              | X          |        | X                   |                 |
| `libcrypto3`             | X          |        | X                   |                 |
| `libcurl-openssl4`       | X          |        | X                   |                 |
| `libexpat1`              | X          |        | X                   |                 |
| `libnghttp2-14`          | X          |        | X                   |                 |
| `libpcre2-8-0`           | X          |        | X                   |                 |
| `libssl3`                | X          |        | X                   |                 |
| `ncurses`                | X          |        | X                   |                 |
| `ncurses-terminfo-base`  | X          |        | X                   |                 |
| `openssl-config`         | X          |        | X                   |                 |
| `thanos`                 | X          | X      |                     |                 |
| `wolfi-baselayout`       | X          | X      | X                   | X               |
| `zlib`                   | X          |        | X                   |                 |
| `thanos-operator`        |            |        | X                   | X               |
| `thanos-operator-compat` |            |        | X                   | X               |

