---
title: "python Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public python Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-03-08 00:56:03
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/python/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/python/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/python/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/python/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **python** Image.

|              | latest-dev        | latest-fips-dev   | latest-fips       | latest            |
|--------------|-------------------|-------------------|-------------------|-------------------|
| Default User | `nonroot`         | `nonroot`         | `nonroot`         | `nonroot`         |
| Entrypoint   | `/usr/bin/python` | `/usr/bin/python` | `/usr/bin/python` | `/usr/bin/python` |
| CMD          | not specified     | not specified     | not specified     | not specified     |
| Workdir      | not specified     | not specified     | not specified     | not specified     |
| Has apk?     | yes               | yes               | no                | no                |
| Has a shell? | yes               | yes               | no                | no                |

Check the [tags history page](/chainguard/chainguard-images/reference/python/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                               | latest-dev | latest-fips-dev | latest-fips | latest |
|-------------------------------|------------|-----------------|-------------|--------|
| `apk-tools`                   | X          | X               |             |        |
| `bash`                        | X          | X               |             |        |
| `binutils`                    | X          | X               |             |        |
| `build-base`                  | X          | X               |             |        |
| `busybox`                     | X          | X               |             |        |
| `ca-certificates-bundle`      | X          | X               | X           | X      |
| `chainguard-baselayout`       | X          | X               | X           | X      |
| `gcc`                         | X          | X               |             |        |
| `gdbm`                        | X          | X               | X           | X      |
| `git`                         | X          | X               |             |        |
| `glibc`                       | X          | X               | X           | X      |
| `glibc-dev`                   | X          | X               |             |        |
| `glibc-locale-posix`          | X          | X               | X           | X      |
| `gmp`                         | X          | X               |             |        |
| `isl`                         | X          | X               |             |        |
| `ld-linux`                    | X          | X               | X           | X      |
| `libatomic`                   | X          | X               |             |        |
| `libbrotlicommon1`            | X          | X               |             |        |
| `libbrotlidec1`               | X          | X               |             |        |
| `libbz2-1`                    | X          | X               | X           | X      |
| `libcrypt1`                   | X          | X               | X           | X      |
| `libcrypto3`                  | X          | X               | X           | X      |
| `libcurl-openssl4`            | X          | X               |             |        |
| `libexpat1`                   | X          | X               | X           | X      |
| `libffi`                      | X          | X               | X           | X      |
| `libgcc`                      | X          | X               | X           | X      |
| `libgo`                       | X          | X               |             |        |
| `libgomp`                     | X          | X               |             |        |
| `libidn2`                     | X          |                 |             |        |
| `libnghttp2-14`               | X          | X               |             |        |
| `libpcre2-8-0`                | X          | X               |             |        |
| `libpsl`                      | X          |                 |             |        |
| `libssl3`                     | X          | X               | X           | X      |
| `libstdc++`                   | X          | X               | X           | X      |
| `libstdc++-dev`               | X          | X               |             |        |
| `libunistring`                | X          |                 |             |        |
| `linux-headers`               | X          | X               |             |        |
| `make`                        | X          | X               |             |        |
| `mpc`                         | X          | X               |             |        |
| `mpdecimal`                   | X          | X               | X           | X      |
| `mpfr`                        | X          | X               |             |        |
| `ncurses`                     | X          | X               | X           | X      |
| `ncurses-terminfo-base`       | X          | X               | X           | X      |
| `nss-db`                      | X          | X               |             |        |
| `nss-hesiod`                  | X          | X               |             |        |
| `openssl-config`              | X          |                 |             | X      |
| `pkgconf`                     | X          | X               |             |        |
| `posix-cc-wrappers`           | X          | X               |             |        |
| `py3.12-pip`                  | X          |                 |             |        |
| `py3.12-setuptools`           | X          |                 |             |        |
| `python-3.12`                 | X          |                 |             | X      |
| `python-3.12-default`         | X          |                 |             | X      |
| `python-3.12-dev`             | X          |                 |             |        |
| `readline`                    | X          | X               | X           | X      |
| `sqlite-libs`                 | X          | X               | X           | X      |
| `wget`                        | X          |                 |             |        |
| `wolfi-baselayout`            | X          | X               | X           | X      |
| `xz`                          | X          | X               | X           | X      |
| `zlib`                        | X          | X               | X           | X      |
| `openssl-config-fipshardened` |            | X               | X           |        |
| `openssl-provider-fips`       |            | X               | X           |        |
| `py3.11-pip`                  |            | X               |             |        |
| `py3.11-setuptools`           |            | X               |             |        |
| `python-3.11`                 |            | X               | X           |        |
| `python-3.11-dev`             |            | X               |             |        |

