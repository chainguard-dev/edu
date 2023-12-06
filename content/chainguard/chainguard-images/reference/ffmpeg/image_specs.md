---
title: "ffmpeg Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public ffmpeg Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-12-06 18:44:36
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/ffmpeg/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/ffmpeg/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/ffmpeg/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/ffmpeg/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **ffmpeg** Image.

## Variants Compared
The **ffmpeg** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev        | latest            |
|--------------|-------------------|-------------------|
| Default User | `nonroot`         | `nonroot`         |
| Entrypoint   | `/usr/bin/ffmpeg` | `/usr/bin/ffmpeg` |
| CMD          | `--help`          | `--help`          |
| Workdir      | not specified     | not specified     |
| Has apk?     | yes               | no                |
| Has a shell? | yes               | no                |

Check the [tags history page](/chainguard/chainguard-images/reference/ffmpeg/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `aom-libs`               | X          | X      |
| `apk-tools`              | X          |        |
| `bash`                   | X          |        |
| `busybox`                | X          |        |
| `ca-certificates-bundle` | X          | X      |
| `ffmpeg`                 | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `ld-linux`               | X          | X      |
| `libavcodec60`           | X          | X      |
| `libavdevice60`          | X          | X      |
| `libavfilter9`           | X          | X      |
| `libavformat60`          | X          | X      |
| `libavutil58`            | X          | X      |
| `libbrotlicommon1`       | X          |        |
| `libbrotlidec1`          | X          |        |
| `libcrypt1`              | X          |        |
| `libcrypto3`             | X          |        |
| `libcurl-openssl4`       | X          |        |
| `libexpat1`              | X          |        |
| `libnghttp2-14`          | X          |        |
| `libogg`                 | X          | X      |
| `libpcre2-8-0`           | X          |        |
| `libssl3`                | X          |        |
| `libswresample4`         | X          | X      |
| `libswscale7`            | X          | X      |
| `libtheora`              | X          | X      |
| `ncurses`                | X          |        |
| `ncurses-terminfo-base`  | X          |        |
| `openssl-config`         | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `x264`                   | X          | X      |
| `zlib`                   | X          |        |

