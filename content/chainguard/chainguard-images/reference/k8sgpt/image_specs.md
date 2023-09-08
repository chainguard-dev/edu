---
title: "k8sgpt Image Variants"
type: "article"
description: "Detailed information about the public k8sgpt Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "k8sgpt"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **k8sgpt** Image.

## Variants Compared
The **k8sgpt** Chainguard Image currently has 3 public variants: 

- `latest`
- `operator-latest-dev`
- `operator-latest`

The table has detailed information about each of these variants.

|              | latest        | operator-latest-dev | operator-latest |
|--------------|---------------|---------------------|-----------------|
| Default User | `65532`       | `65532`             | `65532`         |
| Entrypoint   | `k8sgpt`      | `manager`           | `manager`       |
| CMD          | not specified | not specified       | not specified   |
| Workdir      | not specified | not specified       | not specified   |
| Has apk?     | no            | yes                 | no              |
| Has a shell? | no            | yes                 | no              |

Check the [tags history page](/chainguard/chainguard-images/reference/k8sgpt/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest | operator-latest-dev | operator-latest |
|--------------------------|--------|---------------------|-----------------|
| `ca-certificates-bundle` | X      | X                   | X               |
| `k8sgpt`                 | X      |                     |                 |
| `wolfi-baselayout`       | X      | X                   | X               |
| `apk-tools`              |        | X                   |                 |
| `bash`                   |        | X                   |                 |
| `busybox`                |        | X                   |                 |
| `git`                    |        | X                   |                 |
| `glibc`                  |        | X                   | X               |
| `glibc-locale-posix`     |        | X                   | X               |
| `k8sgpt-operator`        |        | X                   | X               |
| `ld-linux`               |        | X                   | X               |
| `libbrotlicommon1`       |        | X                   |                 |
| `libbrotlidec1`          |        | X                   |                 |
| `libcrypt1`              |        | X                   |                 |
| `libcrypto3`             |        | X                   |                 |
| `libcurl-openssl4`       |        | X                   |                 |
| `libexpat1`              |        | X                   |                 |
| `libnghttp2-14`          |        | X                   |                 |
| `libpcre2-8-0`           |        | X                   |                 |
| `libssl3`                |        | X                   |                 |
| `ncurses`                |        | X                   |                 |
| `ncurses-terminfo-base`  |        | X                   |                 |
| `openssl-config`         |        | X                   |                 |
| `zlib`                   |        | X                   |                 |
