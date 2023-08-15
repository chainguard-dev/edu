---
title: "cluster-autoscaler Image Variants"
type: "article"
description: "Detailed information about the public cluster-autoscaler Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "cluster-autoscaler"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **cluster-autoscaler** Image.

## Variants Compared
The **cluster-autoscaler** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                    | latest                        |
|--------------|-------------------------------|-------------------------------|
| Default User | `cluster-autoscaler`          | `cluster-autoscaler`          |
| Entrypoint   | `/usr/bin/cluster-autoscaler` | `/usr/bin/cluster-autoscaler` |
| CMD          | not specified                 | not specified                 |
| Workdir      | `/`                           | `/`                           |
| Has apk?     | yes                           | no                            |
| Has a shell? | yes                           | no                            |

Check the [tags history page](/chainguard/chainguard-images/reference/cluster-autoscaler/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                             | latest-dev | latest |
|-----------------------------|------------|--------|
| `apk-tools`                 | X          |        |
| `bash`                      | X          |        |
| `busybox`                   | X          |        |
| `ca-certificates-bundle`    | X          | X      |
| `cluster-autoscaler`        | X          | X      |
| `cluster-autoscaler-compat` | X          | X      |
| `git`                       | X          |        |
| `glibc`                     | X          |        |
| `glibc-locale-posix`        | X          |        |
| `ld-linux`                  | X          |        |
| `libbrotlicommon1`          | X          |        |
| `libbrotlidec1`             | X          |        |
| `libcrypt1`                 | X          |        |
| `libcrypto3`                | X          |        |
| `libcurl-openssl4`          | X          |        |
| `libexpat1`                 | X          |        |
| `libnghttp2-14`             | X          |        |
| `libpcre2-8-0`              | X          |        |
| `libssl3`                   | X          |        |
| `ncurses`                   | X          |        |
| `ncurses-terminfo-base`     | X          |        |
| `openssl-config`            | X          |        |
| `wolfi-baselayout`          | X          | X      |
| `zlib`                      | X          |        |
