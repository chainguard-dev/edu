---
title: "zig Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public zig Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/zig/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/zig/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/zig/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/zig/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **zig** Image.

## Variants Compared
The **zig** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev     | latest         |
|--------------|----------------|----------------|
| Default User | `root`         | `root`         |
| Entrypoint   | `/usr/bin/zig` | `/usr/bin/zig` |
| CMD          | `help`         | `help`         |
| Workdir      | not specified  | not specified  |
| Has apk?     | yes            | no             |
| Has a shell? | yes            | yes            |

Check the [tags history page](/chainguard/chainguard-images/reference/zig/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          |        |
| `busybox`                | X          | X      |
| `ca-certificates-bundle` | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `ld-linux`               | X          | X      |
| `libLLVM-16`             | X          | X      |
| `libbrotlicommon1`       | X          |        |
| `libbrotlidec1`          | X          |        |
| `libclang-cpp-16`        | X          | X      |
| `libcrypt1`              | X          | X      |
| `libcrypto3`             | X          |        |
| `libcurl-rustls4`        | X          |        |
| `libexpat1`              | X          |        |
| `libffi`                 | X          | X      |
| `libgcc`                 | X          | X      |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libssl3`                | X          |        |
| `libstdc++`              | X          | X      |
| `libxml2`                | X          | X      |
| `llvm-lld-16`            | X          | X      |
| `ncurses`                | X          |        |
| `ncurses-terminfo-base`  | X          |        |
| `openssl-config`         | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `xz`                     | X          | X      |
| `zig`                    | X          | X      |
| `zlib`                   | X          | X      |

