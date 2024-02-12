---
title: "node Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public node Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-02-12 00:21:23
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/node/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/node/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/node/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/node/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **node** Image.

## Variants Compared
The **node** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev      | latest          |
|--------------|-----------------|-----------------|
| Default User | `node`          | `node`          |
| Entrypoint   | `/usr/bin/node` | `/usr/bin/node` |
| CMD          | `--help`        | `--help`        |
| Workdir      | `/app`          | `/app`          |
| Has apk?     | yes             | no              |
| Has a shell? | yes             | yes             |

Check the [tags history page](/chainguard/chainguard-images/reference/node/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          |        |
| `binutils`               | X          |        |
| `build-base`             | X          |        |
| `busybox`                | X          | X      |
| `c-ares`                 | X          | X      |
| `ca-certificates-bundle` | X          | X      |
| `gcc`                    | X          |        |
| `gdbm`                   | X          |        |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-dev`              | X          |        |
| `glibc-locale-posix`     | X          | X      |
| `gmp`                    | X          |        |
| `icu`                    | X          | X      |
| `isl`                    | X          |        |
| `ld-linux`               | X          | X      |
| `libatomic`              | X          |        |
| `libbrotlicommon1`       | X          | X      |
| `libbrotlidec1`          | X          | X      |
| `libbrotlienc1`          | X          | X      |
| `libbz2-1`               | X          |        |
| `libcrypt1`              | X          | X      |
| `libcrypto3`             | X          | X      |
| `libcurl-openssl4`       | X          |        |
| `libev`                  | X          | X      |
| `libexpat1`              | X          |        |
| `libffi`                 | X          |        |
| `libgcc`                 | X          | X      |
| `libgo`                  | X          |        |
| `libgomp`                | X          |        |
| `libidn2`                | X          |        |
| `libnghttp2-14`          | X          | X      |
| `libpcre2-8-0`           | X          |        |
| `libpsl`                 | X          |        |
| `libssl3`                | X          | X      |
| `libstdc++`              | X          | X      |
| `libstdc++-dev`          | X          |        |
| `libunistring`           | X          |        |
| `libuv`                  | X          | X      |
| `linux-headers`          | X          |        |
| `make`                   | X          |        |
| `mpc`                    | X          |        |
| `mpdecimal`              | X          |        |
| `mpfr`                   | X          |        |
| `ncurses`                | X          |        |
| `ncurses-terminfo-base`  | X          |        |
| `nghttp2`                | X          | X      |
| `nodejs-20`              | X          | X      |
| `npm`                    | X          | X      |
| `nss-db`                 | X          |        |
| `nss-hesiod`             | X          |        |
| `openssl-config`         | X          | X      |
| `pkgconf`                | X          |        |
| `posix-cc-wrappers`      | X          |        |
| `python-3.11`            | X          |        |
| `readline`               | X          |        |
| `sqlite-libs`            | X          |        |
| `wget`                   | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `xz`                     | X          |        |
| `yarn`                   | X          |        |
| `zlib`                   | X          | X      |

