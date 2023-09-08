---
title: "prometheus-mysqld-exporter Image Variants"
type: "article"
description: "Detailed information about the public prometheus-mysqld-exporter Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "prometheus-mysqld-exporter"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **prometheus-mysqld-exporter** Image.

## Variants Compared
The **prometheus-mysqld-exporter** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                 | latest                     |
|--------------|----------------------------|----------------------------|
| Default User | `65532`                    | `65532`                    |
| Entrypoint   | `/usr/bin/mysqld_exporter` | `/usr/bin/mysqld_exporter` |
| CMD          | not specified              | not specified              |
| Workdir      | not specified              | not specified              |
| Has apk?     | yes                        | yes                        |
| Has a shell? | yes                        | yes                        |

Check the [tags history page](/chainguard/chainguard-images/reference/prometheus-mysqld-exporter/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                              | latest-dev | latest |
|------------------------------|------------|--------|
| `apk-tools`                  | X          | X      |
| `bash`                       | X          |        |
| `busybox`                    | X          | X      |
| `ca-certificates-bundle`     | X          | X      |
| `git`                        | X          |        |
| `glibc`                      | X          | X      |
| `glibc-locale-posix`         | X          | X      |
| `ld-linux`                   | X          | X      |
| `libbrotlicommon1`           | X          |        |
| `libbrotlidec1`              | X          |        |
| `libcrypt1`                  | X          | X      |
| `libcrypto3`                 | X          | X      |
| `libcurl-openssl4`           | X          |        |
| `libexpat1`                  | X          |        |
| `libnghttp2-14`              | X          |        |
| `libpcre2-8-0`               | X          |        |
| `libssl3`                    | X          | X      |
| `ncurses`                    | X          |        |
| `ncurses-terminfo-base`      | X          |        |
| `openssl-config`             | X          | X      |
| `prometheus-mysqld-exporter` | X          | X      |
| `wolfi-base`                 | X          | X      |
| `wolfi-baselayout`           | X          | X      |
| `wolfi-keys`                 | X          | X      |
| `zlib`                       | X          | X      |
