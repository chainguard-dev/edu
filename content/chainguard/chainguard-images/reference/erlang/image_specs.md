---
title: "erlang Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public erlang Chainguard Image variants"
date: 2023-12-05 16:09:03
lastmod: 2023-12-05 16:09:03
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/erlang/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/erlang/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/erlang/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/erlang/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **erlang** Image.

## Variants Compared
The **erlang** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev     | latest         |
|--------------|----------------|----------------|
| Default User | `root`         | `root`         |
| Entrypoint   | `/usr/bin/erl` | `/usr/bin/erl` |
| CMD          | not specified  | not specified  |
| Workdir      | not specified  | not specified  |
| Has apk?     | yes            | no             |
| Has a shell? | yes            | yes            |

Check the [tags history page](/chainguard/chainguard-images/reference/erlang/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          |        |
| `busybox`                | X          | X      |
| `ca-certificates-bundle` | X          | X      |
| `erlang-26`              | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `ld-linux`               | X          | X      |
| `libbrotlicommon1`       | X          |        |
| `libbrotlidec1`          | X          |        |
| `libcrypt1`              | X          | X      |
| `libcrypto3`             | X          | X      |
| `libcurl-openssl4`       | X          |        |
| `libexpat1`              | X          |        |
| `libgcc`                 | X          | X      |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libssl3`                | X          |        |
| `libstdc++`              | X          | X      |
| `ncurses`                | X          | X      |
| `ncurses-terminfo-base`  | X          | X      |
| `openssl-config`         | X          | X      |
| `wolfi-baselayout`       | X          | X      |
| `zlib`                   | X          | X      |

