---
title: "r-base Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public r-base Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/r-base/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/r-base/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/r-base/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/r-base/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **r-base** Image.

## Variants Compared
The **r-base** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev    | latest        |
|--------------|---------------|---------------|
| Default User | `nonroot`     | `nonroot`     |
| Entrypoint   | `/usr/bin/R`  | `/usr/bin/R`  |
| CMD          | `--help`      | `--help`      |
| Workdir      | not specified | not specified |
| Has apk?     | yes           | no            |
| Has a shell? | yes           | yes           |

Check the [tags history page](/chainguard/chainguard-images/reference/r-base/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `R`                      | X          | X      |
| `apk-tools`              | X          |        |
| `bash`                   | X          |        |
| `busybox`                | X          | X      |
| `ca-certificates-bundle` | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `icu`                    | X          | X      |
| `ld-linux`               | X          | X      |
| `libbrotlicommon1`       | X          | X      |
| `libbrotlidec1`          | X          | X      |
| `libbz2-1`               | X          | X      |
| `libcrypt1`              | X          | X      |
| `libcrypto3`             | X          |        |
| `libcurl-rustls4`        | X          | X      |
| `libexpat1`              | X          |        |
| `libgcc`                 | X          | X      |
| `libgfortran`            | X          | X      |
| `libgomp`                | X          | X      |
| `libice`                 | X          | X      |
| `libjpeg-turbo`          | X          | X      |
| `libnghttp2-14`          | X          | X      |
| `libpcre2-8-0`           | X          | X      |
| `libpng`                 | X          | X      |
| `libsm`                  | X          | X      |
| `libssl3`                | X          |        |
| `libstdc++`              | X          | X      |
| `libuuid`                | X          | X      |
| `libwebp`                | X          | X      |
| `libx11`                 | X          | X      |
| `libxau`                 | X          | X      |
| `libxcb`                 | X          | X      |
| `libxdmcp`               | X          | X      |
| `libxext`                | X          | X      |
| `libxmu`                 | X          | X      |
| `libxt`                  | X          | X      |
| `libzstd1`               | X          | X      |
| `ncurses`                | X          | X      |
| `ncurses-terminfo-base`  | X          | X      |
| `openblas`               | X          | X      |
| `openssl-config`         | X          |        |
| `readline`               | X          | X      |
| `tiff`                   | X          | X      |
| `wolfi-baselayout`       | X          | X      |
| `xz`                     | X          | X      |
| `zlib`                   | X          | X      |

