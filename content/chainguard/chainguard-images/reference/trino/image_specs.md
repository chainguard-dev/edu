---
title: "trino Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public trino Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-01-15 00:20:04
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/trino/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/trino/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/trino/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/trino/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **trino** Image.

## Variants Compared
The **trino** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev           | latest               |
|--------------|----------------------|----------------------|
| Default User | `trino`              | `trino`              |
| Entrypoint   | `/usr/bin/run-trino` | `/usr/bin/run-trino` |
| CMD          | not specified        | not specified        |
| Workdir      | not specified        | not specified        |
| Has apk?     | yes                  | no                   |
| Has a shell? | yes                  | yes                  |

Check the [tags history page](/chainguard/chainguard-images/reference/trino/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                    | latest-dev | latest |
|------------------------------------|------------|--------|
| `apk-tools`                        | X          |        |
| `bash`                             | X          | X      |
| `busybox`                          | X          | X      |
| `ca-certificates`                  | X          | X      |
| `ca-certificates-bundle`           | X          | X      |
| `curl`                             | X          | X      |
| `fontconfig-config`                | X          | X      |
| `freetype`                         | X          | X      |
| `gdbm`                             | X          | X      |
| `git`                              | X          |        |
| `glibc`                            | X          | X      |
| `glibc-locale-posix`               | X          | X      |
| `java-cacerts`                     | X          | X      |
| `java-common`                      | X          | X      |
| `ld-linux`                         | X          | X      |
| `libbrotlicommon1`                 | X          | X      |
| `libbrotlidec1`                    | X          | X      |
| `libbz2-1`                         | X          | X      |
| `libcrypt1`                        | X          | X      |
| `libcrypto3`                       | X          | X      |
| `libcurl-openssl4`                 | X          | X      |
| `libexpat1`                        | X          | X      |
| `libffi`                           | X          | X      |
| `libfontconfig1`                   | X          | X      |
| `libgcc`                           | X          | X      |
| `libidn2`                          | X          | X      |
| `libnghttp2-14`                    | X          | X      |
| `libpcre2-8-0`                     | X          |        |
| `libpng`                           | X          | X      |
| `libpsl`                           | X          | X      |
| `libssl3`                          | X          | X      |
| `libstdc++`                        | X          | X      |
| `libtasn1`                         | X          | X      |
| `libunistring`                     | X          | X      |
| `mpdecimal`                        | X          | X      |
| `ncurses`                          | X          | X      |
| `ncurses-terminfo-base`            | X          | X      |
| `openjdk-17-default-jvm`           | X          | X      |
| `openjdk-17-jre`                   | X          | X      |
| `openjdk-17-jre-base`              | X          | X      |
| `openssl-config`                   | X          | X      |
| `p11-kit`                          | X          | X      |
| `p11-kit-trust`                    | X          | X      |
| `python-3.12`                      | X          | X      |
| `readline`                         | X          | X      |
| `sqlite-libs`                      | X          | X      |
| `trino`                            | X          | X      |
| `trino-config`                     | X          | X      |
| `trino-oci-entrypoint`             | X          | X      |
| `trino-plugin-exchange-filesystem` | X          | X      |
| `trino-plugin-jmx`                 | X          | X      |
| `trino-plugin-memory`              | X          | X      |
| `trino-plugin-tpcds`               | X          | X      |
| `trino-plugin-tpch`                | X          | X      |
| `wolfi-baselayout`                 | X          | X      |
| `xz`                               | X          | X      |
| `zlib`                             | X          | X      |

