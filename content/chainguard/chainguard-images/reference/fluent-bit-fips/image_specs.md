---
title: "fluent-bit-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public fluent-bit-fips Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-06-07 00:46:50
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

|              | latest-dev                                 |
|--------------|--------------------------------------------|
| Default User | `root`                                     |
| Entrypoint   | `/usr/bin/fluent-bit`                      |
| CMD          | `--config=/fluent-bit/etc/fluent-bit.conf` |
| Workdir      | not specified                              |
| Has apk?     | yes                                        |
| Has a shell? | yes                                        |

Check the [tags history page](/chainguard/chainguard-images/reference/fluent-bit-fips/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                               | latest-dev |
|-------------------------------|------------|
| `apk-tools`                   | X          |
| `bash`                        | X          |
| `busybox`                     | X          |
| `ca-certificates-bundle`      | X          |
| `chainguard-baselayout`       | X          |
| `fluent-bit-3.0`              | X          |
| `fluent-bit-3.0-compat`       | X          |
| `git`                         | X          |
| `glibc`                       | X          |
| `glibc-locale-posix`          | X          |
| `ld-linux`                    | X          |
| `libbrotlicommon1`            | X          |
| `libbrotlidec1`               | X          |
| `libcap`                      | X          |
| `libcrypt1`                   | X          |
| `libcrypto3`                  | X          |
| `libcurl-openssl4`            | X          |
| `libexpat1`                   | X          |
| `libgcc`                      | X          |
| `libidn2`                     | X          |
| `libnghttp2-14`               | X          |
| `libpcre2-8-0`                | X          |
| `libpq-16`                    | X          |
| `libpsl`                      | X          |
| `libssl3`                     | X          |
| `libsystemd`                  | X          |
| `libunistring`                | X          |
| `libxcrypt`                   | X          |
| `ncurses`                     | X          |
| `ncurses-terminfo-base`       | X          |
| `openssl-config-fipshardened` | X          |
| `openssl-provider-fips`       | X          |
| `wget`                        | X          |
| `wolfi-baselayout`            | X          |
| `yaml`                        | X          |
| `zlib`                        | X          |

