---
title: "clang Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public clang Chainguard Image variants"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/clang/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/clang/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/clang/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/clang/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **clang** Image.

## Variants Compared
The **clang** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev       | latest           |
|--------------|------------------|------------------|
| Default User | `root`           | `root`           |
| Entrypoint   | `/usr/bin/clang` | `/usr/bin/clang` |
| CMD          | `--help`         | `--help`         |
| Workdir      | `/work`          | `/work`          |
| Has apk?     | yes              | no               |
| Has a shell? | yes              | yes              |

Check the [tags history page](/chainguard/chainguard-images/reference/clang/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          |        |
| `binutils`               | X          | X      |
| `build-base`             | X          | X      |
| `busybox`                | X          | X      |
| `ca-certificates-bundle` | X          | X      |
| `clang-15`               | X          | X      |
| `clang-15-default`       | X          | X      |
| `gcc`                    | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-dev`              | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `gmp`                    | X          | X      |
| `isl`                    | X          | X      |
| `ld-linux`               | X          | X      |
| `libLLVM-15`             | X          | X      |
| `libatomic`              | X          | X      |
| `libbrotlicommon1`       | X          |        |
| `libbrotlidec1`          | X          |        |
| `libclang-cpp-15`        | X          | X      |
| `libcrypt1`              | X          | X      |
| `libcrypto3`             | X          |        |
| `libcurl-openssl4`       | X          |        |
| `libexpat1`              | X          |        |
| `libffi`                 | X          | X      |
| `libgcc`                 | X          | X      |
| `libgo`                  | X          | X      |
| `libgomp`                | X          | X      |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libssl3`                | X          |        |
| `libstdc++`              | X          | X      |
| `libstdc++-dev`          | X          | X      |
| `libxml2`                | X          | X      |
| `linux-headers`          | X          | X      |
| `make`                   | X          | X      |
| `mpc`                    | X          | X      |
| `mpfr`                   | X          | X      |
| `ncurses`                | X          |        |
| `ncurses-terminfo-base`  | X          |        |
| `nss-db`                 | X          | X      |
| `nss-hesiod`             | X          | X      |
| `openssl-config`         | X          |        |
| `pkgconf`                | X          | X      |
| `posix-cc-wrappers`      | X          | X      |
| `wolfi-baselayout`       | X          | X      |
| `xz`                     | X          | X      |
| `zlib`                   | X          | X      |

