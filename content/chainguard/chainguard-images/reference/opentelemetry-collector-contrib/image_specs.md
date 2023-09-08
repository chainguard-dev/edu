---
title: "opentelemetry-collector-contrib Image Variants"
type: "article"
description: "Detailed information about the public opentelemetry-collector-contrib Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "opentelemetry-collector-contrib"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **opentelemetry-collector-contrib** Image.

## Variants Compared
The **opentelemetry-collector-contrib** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                 | latest                     |
|--------------|----------------------------|----------------------------|
| Default User | `65532`                    | `65532`                    |
| Entrypoint   | `/usr/bin/otelcol-contrib` | `/usr/bin/otelcol-contrib` |
| CMD          | not specified              | not specified              |
| Workdir      | not specified              | not specified              |
| Has apk?     | yes                        | no                         |
| Has a shell? | yes                        | yes                        |

Check the [tags history page](/chainguard/chainguard-images/reference/opentelemetry-collector-contrib/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                          | latest-dev | latest |
|------------------------------------------|------------|--------|
| `apk-tools`                              | X          |        |
| `bash`                                   | X          |        |
| `busybox`                                | X          | X      |
| `ca-certificates-bundle`                 | X          | X      |
| `git`                                    | X          |        |
| `glibc`                                  | X          | X      |
| `glibc-locale-posix`                     | X          | X      |
| `ld-linux`                               | X          | X      |
| `libbrotlicommon1`                       | X          |        |
| `libbrotlidec1`                          | X          |        |
| `libcrypt1`                              | X          | X      |
| `libcrypto3`                             | X          |        |
| `libcurl-openssl4`                       | X          |        |
| `libexpat1`                              | X          |        |
| `libnghttp2-14`                          | X          |        |
| `libpcre2-8-0`                           | X          |        |
| `libssl3`                                | X          |        |
| `ncurses`                                | X          |        |
| `ncurses-terminfo-base`                  | X          |        |
| `openssl-config`                         | X          |        |
| `opentelemetry-collector-contrib`        | X          | X      |
| `opentelemetry-collector-contrib-compat` | X          | X      |
| `wolfi-baselayout`                       | X          | X      |
| `zlib`                                   | X          |        |
