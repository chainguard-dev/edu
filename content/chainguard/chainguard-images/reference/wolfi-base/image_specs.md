---
title: "wolfi-base Image Variants"
type: "article"
description: "Detailed information about the public wolfi-base Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "wolfi-base"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **wolfi-base** Image.

## Variants Compared
The **wolfi-base** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest        |
|--------------|---------------|
| Default User | `root`        |
| Entrypoint   | ``            |
| CMD          | `/bin/sh -l`  |
| Workdir      | not specified |
| Has apk?     | yes           |
| Has a shell? | yes           |

Check the [tags history page](/chainguard/chainguard-images/reference/wolfi-base/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest |
|--------------------------|--------|
| `apk-tools`              | X      |
| `busybox`                | X      |
| `ca-certificates-bundle` | X      |
| `glibc`                  | X      |
| `glibc-locale-posix`     | X      |
| `ld-linux`               | X      |
| `libcrypt1`              | X      |
| `libcrypto3`             | X      |
| `libssl3`                | X      |
| `openssl-config`         | X      |
| `wolfi-base`             | X      |
| `wolfi-baselayout`       | X      |
| `wolfi-keys`             | X      |
| `zlib`                   | X      |
