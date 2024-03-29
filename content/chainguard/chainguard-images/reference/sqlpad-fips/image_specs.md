---
title: "sqlpad-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public sqlpad-fips Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-03-29 00:47:42
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/sqlpad-fips/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/sqlpad-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/sqlpad-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/sqlpad-fips/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **sqlpad-fips** Image.

|              | latest-dev                                 | latest                                     |
|--------------|--------------------------------------------|--------------------------------------------|
| Default User | `nonroot`                                  | `nonroot`                                  |
| Entrypoint   | `node server.js --config ./config.dev.env` | `node server.js --config ./config.dev.env` |
| CMD          | not specified                              | not specified                              |
| Workdir      | `/usr/app/sqlpad-server`                   | `/usr/app/sqlpad-server`                   |
| Has apk?     | yes                                        | no                                         |
| Has a shell? | yes                                        | no                                         |

Check the [tags history page](/chainguard/chainguard-images/reference/sqlpad-fips/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                               | latest-dev | latest |
|-------------------------------|------------|--------|
| `apk-tools`                   | X          |        |
| `bash`                        | X          |        |
| `busybox`                     | X          |        |
| `c-ares`                      | X          | X      |
| `ca-certificates-bundle`      | X          | X      |
| `chainguard-baselayout`       | X          | X      |
| `git`                         | X          |        |
| `glibc`                       | X          | X      |
| `glibc-locale-posix`          | X          | X      |
| `icu`                         | X          | X      |
| `ld-linux`                    | X          | X      |
| `libbrotlicommon1`            | X          | X      |
| `libbrotlidec1`               | X          | X      |
| `libbrotlienc1`               | X          | X      |
| `libcrypt1`                   | X          |        |
| `libcrypto3`                  | X          | X      |
| `libcurl-openssl4`            | X          |        |
| `libexpat1`                   | X          |        |
| `libgcc`                      | X          | X      |
| `libidn2`                     | X          |        |
| `libnghttp2-14`               | X          | X      |
| `libpcre2-8-0`                | X          |        |
| `libpsl`                      | X          |        |
| `libssl3`                     | X          | X      |
| `libstdc++`                   | X          | X      |
| `libunistring`                | X          |        |
| `libuv`                       | X          | X      |
| `libxcrypt`                   | X          |        |
| `ncurses`                     | X          |        |
| `ncurses-terminfo-base`       | X          |        |
| `nodejs-18`                   | X          | X      |
| `openssl-config-fipshardened` | X          | X      |
| `openssl-provider-fips`       | X          | X      |
| `sqlpad`                      | X          | X      |
| `sqlpad-compat`               | X          | X      |
| `wget`                        | X          |        |
| `wolfi-baselayout`            | X          | X      |
| `yarn`                        | X          | X      |
| `zlib`                        | X          | X      |

