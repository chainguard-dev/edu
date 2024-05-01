---
title: "gcc-glibc Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public gcc-glibc Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-05-01 00:46:56
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/gcc-glibc/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/gcc-glibc/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/gcc-glibc/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gcc-glibc/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **gcc-glibc** Image.

|              | latest-dev     | latest         |
|--------------|----------------|----------------|
| Default User | `root`         | `root`         |
| Entrypoint   | `/usr/bin/gcc` | `/usr/bin/gcc` |
| CMD          | `--help`       | `--help`       |
| Workdir      | `/work`        | `/work`        |
| Has apk?     | yes            | no             |
| Has a shell? | yes            | yes            |

Check the [tags history page](/chainguard/chainguard-images/reference/gcc-glibc/tags_history/) for the full list of available tags.

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
| `chainguard-baselayout`  | X          | X      |
| `gcc`                    | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-dev`              | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `gmp`                    | X          | X      |
| `isl`                    | X          | X      |
| `ld-linux`               | X          | X      |
| `libatomic`              | X          | X      |
| `libbrotlicommon1`       | X          |        |
| `libbrotlidec1`          | X          |        |
| `libcrypt1`              | X          | X      |
| `libcrypto3`             | X          |        |
| `libcurl-openssl4`       | X          |        |
| `libexpat1`              | X          |        |
| `libgcc`                 | X          | X      |
| `libgo`                  | X          | X      |
| `libgomp`                | X          | X      |
| `libidn2`                | X          |        |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libpsl`                 | X          |        |
| `libssl3`                | X          |        |
| `libstdc++`              | X          | X      |
| `libstdc++-dev`          | X          | X      |
| `libunistring`           | X          |        |
| `libxcrypt`              | X          | X      |
| `libxcrypt-dev`          | X          | X      |
| `linux-headers`          | X          | X      |
| `make`                   | X          | X      |
| `mpc`                    | X          | X      |
| `mpfr`                   | X          | X      |
| `ncurses`                | X          |        |
| `ncurses-terminfo-base`  | X          |        |
| `nss-db`                 | X          | X      |
| `nss-hesiod`             | X          | X      |
| `pkgconf`                | X          | X      |
| `posix-cc-wrappers`      | X          | X      |
| `wget`                   | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `zlib`                   | X          | X      |

