---
title: "node Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public node Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-03-15 00:51:40
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/node/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/node/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/node/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/node/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **node** Image.

|              | latest-dev      | latest-fips-dev | latest-fips     | latest          |
|--------------|-----------------|-----------------|-----------------|-----------------|
| Default User | `node`          | `node`          | `node`          | `node`          |
| Entrypoint   | `/usr/bin/node` | `/usr/bin/node` | `/usr/bin/node` | `/usr/bin/node` |
| CMD          | `--help`        | `--help`        | `--help`        | `--help`        |
| Workdir      | `/app`          | `/app`          | `/app`          | `/app`          |
| Has apk?     | yes             | yes             | no              | no              |
| Has a shell? | yes             | yes             | yes             | yes             |

Check the [tags history page](/chainguard/chainguard-images/reference/node/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                               | latest-dev | latest-fips-dev | latest-fips | latest |
|-------------------------------|------------|-----------------|-------------|--------|
| `apk-tools`                   | X          | X               |             |        |
| `bash`                        | X          | X               |             |        |
| `binutils`                    | X          |                 |             |        |
| `build-base`                  | X          |                 |             |        |
| `busybox`                     | X          | X               | X           | X      |
| `c-ares`                      | X          | X               | X           | X      |
| `ca-certificates-bundle`      | X          | X               | X           | X      |
| `chainguard-baselayout`       | X          | X               | X           | X      |
| `dumb-init`                   | X          |                 |             | X      |
| `gcc`                         | X          |                 |             |        |
| `gdbm`                        | X          |                 |             |        |
| `git`                         | X          | X               |             |        |
| `glibc`                       | X          | X               | X           | X      |
| `glibc-dev`                   | X          |                 |             |        |
| `glibc-locale-posix`          | X          | X               | X           | X      |
| `gmp`                         | X          |                 |             |        |
| `icu`                         | X          | X               | X           | X      |
| `isl`                         | X          |                 |             |        |
| `ld-linux`                    | X          | X               | X           | X      |
| `libatomic`                   | X          |                 |             |        |
| `libbrotlicommon1`            | X          | X               | X           | X      |
| `libbrotlidec1`               | X          | X               | X           | X      |
| `libbrotlienc1`               | X          | X               | X           | X      |
| `libbz2-1`                    | X          |                 |             |        |
| `libcrypt1`                   | X          | X               | X           | X      |
| `libcrypto3`                  | X          | X               | X           | X      |
| `libcurl-openssl4`            | X          | X               |             |        |
| `libev`                       | X          | X               | X           | X      |
| `libexpat1`                   | X          | X               |             |        |
| `libffi`                      | X          |                 |             |        |
| `libgcc`                      | X          | X               | X           | X      |
| `libgo`                       | X          |                 |             |        |
| `libgomp`                     | X          |                 |             |        |
| `libidn2`                     | X          |                 |             |        |
| `libnghttp2-14`               | X          | X               | X           | X      |
| `libpcre2-8-0`                | X          | X               |             |        |
| `libpsl`                      | X          |                 |             |        |
| `libssl3`                     | X          | X               | X           | X      |
| `libstdc++`                   | X          | X               | X           | X      |
| `libstdc++-dev`               | X          |                 |             |        |
| `libunistring`                | X          |                 |             |        |
| `libuv`                       | X          |                 |             | X      |
| `linux-headers`               | X          |                 |             |        |
| `make`                        | X          |                 |             |        |
| `mpc`                         | X          |                 |             |        |
| `mpdecimal`                   | X          |                 |             |        |
| `mpfr`                        | X          |                 |             |        |
| `ncurses`                     | X          | X               |             |        |
| `ncurses-terminfo-base`       | X          | X               |             |        |
| `nghttp2`                     | X          | X               | X           | X      |
| `nodejs-21`                   | X          |                 |             | X      |
| `npm`                         | X          | X               | X           | X      |
| `nss-db`                      | X          |                 |             |        |
| `nss-hesiod`                  | X          |                 |             |        |
| `openssl-config`              | X          |                 |             | X      |
| `pkgconf`                     | X          |                 |             |        |
| `posix-cc-wrappers`           | X          |                 |             |        |
| `python-3.11`                 | X          |                 |             |        |
| `python-3.11-base`            | X          |                 |             |        |
| `readline`                    | X          |                 |             |        |
| `sqlite-libs`                 | X          |                 |             |        |
| `wget`                        | X          |                 |             |        |
| `wolfi-baselayout`            | X          | X               | X           | X      |
| `xz`                          | X          |                 |             |        |
| `yarn`                        | X          |                 |             |        |
| `zlib`                        | X          | X               | X           | X      |
| `nodejs-18`                   |            | X               | X           |        |
| `openssl-config-fipshardened` |            | X               | X           |        |
| `openssl-provider-fips`       |            | X               | X           |        |

