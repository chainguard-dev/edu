---
title: "timoni Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public timoni Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/timoni/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/timoni/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/timoni/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/timoni/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **timoni** Image.

## Variants Compared
The **timoni** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev        | latest            |
|--------------|-------------------|-------------------|
| Default User | `nonroot`         | `nonroot`         |
| Entrypoint   | `/usr/bin/timoni` | `/usr/bin/timoni` |
| CMD          | `help`            | `help`            |
| Workdir      | not specified     | not specified     |
| Has apk?     | yes               | no                |
| Has a shell? | yes               | no                |

Check the [tags history page](/chainguard/chainguard-images/reference/timoni/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          |        |
| `busybox`                | X          |        |
| `ca-certificates-bundle` | X          | X      |
| `git`                    | X          | X      |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `kubectl-1.28`           | X          | X      |
| `kubectl-latest`         | X          | X      |
| `ld-linux`               | X          | X      |
| `libbrotlicommon1`       | X          | X      |
| `libbrotlidec1`          | X          | X      |
| `libcrypt1`              | X          |        |
| `libcrypto3`             | X          | X      |
| `libcurl-openssl4`       | X          | X      |
| `libexpat1`              | X          | X      |
| `libnghttp2-14`          | X          | X      |
| `libpcre2-8-0`           | X          | X      |
| `libssl3`                | X          | X      |
| `ncurses`                | X          |        |
| `ncurses-terminfo-base`  | X          |        |
| `openssl-config`         | X          | X      |
| `timoni`                 | X          | X      |
| `wolfi-baselayout`       | X          | X      |
| `zlib`                   | X          | X      |

