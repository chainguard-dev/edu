---
title: "valkey-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public valkey-fips Chainguard Image."
date: 2024-07-10 00:36:03
lastmod: 2024-07-10 00:36:03
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/valkey-fips/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/valkey-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/valkey-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/valkey-fips/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **valkey-fips** Image.

|              | latest-dev               | latest                   |
|--------------|--------------------------|--------------------------|
| Default User | `valkey`                 | `valkey`                 |
| Entrypoint   | `/usr/bin/valkey-server` | `/usr/bin/valkey-server` |
| CMD          | not specified            | not specified            |
| Workdir      | `/data`                  | `/data`                  |
| Has apk?     | yes                      | no                       |
| Has a shell? | yes                      | yes                      |

Check the [tags history page](/chainguard/chainguard-images/reference/valkey-fips/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                               | latest-dev | latest |
|-------------------------------|------------|--------|
| `apk-tools`                   | X          |        |
| `bash`                        | X          | X      |
| `busybox`                     | X          | X      |
| `ca-certificates-bundle`      | X          | X      |
| `chainguard-baselayout`       | X          | X      |
| `git`                         | X          |        |
| `glibc`                       | X          | X      |
| `glibc-locale-posix`          | X          | X      |
| `ld-linux`                    | X          | X      |
| `libbrotlicommon1`            | X          |        |
| `libbrotlidec1`               | X          |        |
| `libcrypt1`                   | X          | X      |
| `libcrypto3`                  | X          | X      |
| `libcurl-openssl4`            | X          |        |
| `libexpat1`                   | X          |        |
| `libidn2`                     | X          |        |
| `libnghttp2-14`               | X          |        |
| `libpcre2-8-0`                | X          |        |
| `libpsl`                      | X          |        |
| `libssl3`                     | X          | X      |
| `libunistring`                | X          |        |
| `libxcrypt`                   | X          | X      |
| `ncurses`                     | X          | X      |
| `ncurses-terminfo-base`       | X          | X      |
| `openssl-config-fipshardened` | X          | X      |
| `openssl-provider-fips`       | X          | X      |
| `posix-libc-utils`            | X          | X      |
| `valkey`                      | X          | X      |
| `valkey-cli`                  | X          | X      |
| `wget`                        | X          |        |
| `wolfi-baselayout`            | X          | X      |
| `zlib`                        | X          |        |

