---
title: "gitness Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public gitness Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/gitness/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/gitness/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/gitness/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gitness/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **gitness** Image.

## Variants Compared
The **gitness** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev         | latest             |
|--------------|--------------------|--------------------|
| Default User | `nonroot`          | `nonroot`          |
| Entrypoint   | `/usr/bin/gitness` | `/usr/bin/gitness` |
| CMD          | `server`           | `server`           |
| Workdir      | not specified      | not specified      |
| Has apk?     | yes                | no                 |
| Has a shell? | yes                | yes                |

Check the [tags history page](/chainguard/chainguard-images/reference/gitness/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          |        |
| `busybox`                | X          | X      |
| `ca-certificates-bundle` | X          | X      |
| `git`                    | X          | X      |
| `gitness`                | X          | X      |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `ld-linux`               | X          | X      |
| `libbrotlicommon1`       | X          | X      |
| `libbrotlidec1`          | X          | X      |
| `libcrypt1`              | X          | X      |
| `libcrypto3`             | X          |        |
| `libcurl-rustls4`        | X          | X      |
| `libexpat1`              | X          | X      |
| `libgcc`                 | X          | X      |
| `libnghttp2-14`          | X          | X      |
| `libpcre2-8-0`           | X          | X      |
| `libssl3`                | X          |        |
| `ncurses`                | X          |        |
| `ncurses-terminfo-base`  | X          |        |
| `openssl-config`         | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `zlib`                   | X          | X      |

