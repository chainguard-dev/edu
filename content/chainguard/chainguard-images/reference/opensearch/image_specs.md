---
title: "opensearch Image Variants"
type: "article"
description: "Detailed information about the public opensearch Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "opensearch"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **opensearch** Image.

## Variants Compared
The **opensearch** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                      | latest                          |
|--------------|---------------------------------|---------------------------------|
| Default User | `opensearch`                    | `opensearch`                    |
| Entrypoint   | `/usr/bin/docker-entrypoint.sh` | `/usr/bin/docker-entrypoint.sh` |
| CMD          | `opensearchwrapper`             | `opensearchwrapper`             |
| Workdir      | not specified                   | not specified                   |
| Has apk?     | yes                             | no                              |
| Has a shell? | yes                             | yes                             |

Check the [tags history page](/chainguard/chainguard-images/reference/opensearch/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          | X      |
| `busybox`                | X          | X      |
| `ca-certificates-bundle` | X          | X      |
| `fontconfig-config`      | X          | X      |
| `freetype`               | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `java-cacerts`           | X          | X      |
| `java-common`            | X          | X      |
| `ld-linux`               | X          | X      |
| `libbrotlicommon1`       | X          | X      |
| `libbrotlidec1`          | X          | X      |
| `libbz2-1`               | X          | X      |
| `libcrypt1`              | X          | X      |
| `libcrypto3`             | X          |        |
| `libcurl-openssl4`       | X          |        |
| `libexpat1`              | X          | X      |
| `libfontconfig1`         | X          | X      |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libpng`                 | X          | X      |
| `libssl3`                | X          |        |
| `ncurses`                | X          | X      |
| `ncurses-terminfo-base`  | X          | X      |
| `openjdk-11-default-jvm` | X          | X      |
| `openjdk-11-jre`         | X          | X      |
| `openjdk-11-jre-base`    | X          | X      |
| `opensearch-2`           | X          | X      |
| `openssl-config`         | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `zlib`                   | X          | X      |
