---
title: "fluent-bit-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public fluent-bit-fips Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-04-30 00:52:22
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/fluent-bit-fips/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/fluent-bit-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/fluent-bit-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/fluent-bit-fips/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **fluent-bit-fips** Image.

|              | latest-dev                                 | latest                                     |
|--------------|--------------------------------------------|--------------------------------------------|
| Default User | `root`                                     | `root`                                     |
| Entrypoint   | `/usr/bin/fluent-bit`                      | `/usr/bin/fluent-bit`                      |
| CMD          | `--config=/fluent-bit/etc/fluent-bit.conf` | `--config=/fluent-bit/etc/fluent-bit.conf` |
| Workdir      | not specified                              | not specified                              |
| Has apk?     | yes                                        | no                                         |
| Has a shell? | yes                                        | no                                         |

Check the [tags history page](/chainguard/chainguard-images/reference/fluent-bit-fips/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                               | latest-dev | latest |
|-------------------------------|------------|--------|
| `apk-tools`                   | X          |        |
| `bash`                        | X          |        |
| `busybox`                     | X          |        |
| `ca-certificates-bundle`      | X          | X      |
| `chainguard-baselayout`       | X          | X      |
| `fluent-bit-3.0`              | X          | X      |
| `fluent-bit-3.0-compat`       | X          | X      |
| `git`                         | X          |        |
| `glibc`                       | X          | X      |
| `glibc-locale-posix`          | X          | X      |
| `ld-linux`                    | X          | X      |
| `libbrotlicommon1`            | X          |        |
| `libbrotlidec1`               | X          |        |
| `libcap`                      | X          | X      |
| `libcrypt1`                   | X          |        |
| `libcrypto3`                  | X          | X      |
| `libcurl-openssl4`            | X          |        |
| `libexpat1`                   | X          |        |
| `libgcc`                      | X          | X      |
| `libidn2`                     | X          |        |
| `libnghttp2-14`               | X          |        |
| `libpcre2-8-0`                | X          |        |
| `libpq-16`                    | X          | X      |
| `libpsl`                      | X          |        |
| `libssl3`                     | X          | X      |
| `libsystemd`                  | X          | X      |
| `libunistring`                | X          |        |
| `libxcrypt`                   | X          |        |
| `ncurses`                     | X          |        |
| `ncurses-terminfo-base`       | X          |        |
| `openssl-config-fipshardened` | X          | X      |
| `openssl-provider-fips`       | X          | X      |
| `wget`                        | X          |        |
| `wolfi-baselayout`            | X          | X      |
| `yaml`                        | X          | X      |
| `zlib`                        | X          | X      |

