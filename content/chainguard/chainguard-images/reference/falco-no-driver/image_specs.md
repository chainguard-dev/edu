---
title: "falco-no-driver Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public falco-no-driver Chainguard Image variants"
date: 2023-12-22 00:18:53
lastmod: 2023-12-22 00:18:53
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/falco-no-driver/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/falco-no-driver/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/falco-no-driver/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/falco-no-driver/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **falco-no-driver** Image.

## Variants Compared
The **falco-no-driver** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev       | latest           |
|--------------|------------------|------------------|
| Default User | `root`           | `root`           |
| Entrypoint   | `/usr/bin/falco` | `/usr/bin/falco` |
| CMD          | not specified    | not specified    |
| Workdir      | not specified    | not specified    |
| Has apk?     | yes              | no               |
| Has a shell? | yes              | no               |

Check the [tags history page](/chainguard/chainguard-images/reference/falco-no-driver/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          |        |
| `busybox`                | X          |        |
| `ca-certificates-bundle` | X          | X      |
| `falco-no-driver`        | X          | X      |
| `falco-rules`            | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `ld-linux`               | X          | X      |
| `libbrotlicommon1`       | X          |        |
| `libbrotlidec1`          | X          |        |
| `libcrypt1`              | X          |        |
| `libcrypto3`             | X          |        |
| `libcurl-openssl4`       | X          |        |
| `libexpat1`              | X          |        |
| `libgcc`                 | X          | X      |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libssl3`                | X          |        |
| `ncurses`                | X          |        |
| `ncurses-terminfo-base`  | X          |        |
| `openssl-config`         | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `zlib`                   | X          |        |

