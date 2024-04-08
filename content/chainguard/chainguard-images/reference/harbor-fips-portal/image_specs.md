---
title: "harbor-fips-portal Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public harbor-fips-portal Chainguard Image."
date: 2024-04-08 00:38:35
lastmod: 2024-04-08 00:38:35
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/harbor-fips-portal/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/harbor-fips-portal/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/harbor-fips-portal/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/harbor-fips-portal/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **harbor-fips-portal** Image.

|              | latest-dev               | latest                   |
|--------------|--------------------------|--------------------------|
| Default User | `nginx`                  | `nginx`                  |
| Entrypoint   | `nginx -g 'daemon off;'` | `nginx -g 'daemon off;'` |
| CMD          | not specified            | not specified            |
| Workdir      | `/`                      | `/`                      |
| Has apk?     | yes                      | no                       |
| Has a shell? | yes                      | no                       |

Check the [tags history page](/chainguard/chainguard-images/reference/harbor-fips-portal/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                   | latest-dev | latest |
|-----------------------------------|------------|--------|
| `apk-tools`                       | X          |        |
| `bash`                            | X          |        |
| `busybox`                         | X          |        |
| `ca-certificates-bundle`          | X          | X      |
| `chainguard-baselayout`           | X          | X      |
| `git`                             | X          |        |
| `glibc`                           | X          | X      |
| `glibc-locale-posix`              | X          | X      |
| `harbor-2.10-portal-nginx-config` | X          | X      |
| `harbor-fips-2.10-portal`         | X          | X      |
| `ld-linux`                        | X          | X      |
| `libbrotlicommon1`                | X          |        |
| `libbrotlidec1`                   | X          |        |
| `libcrypt1`                       | X          | X      |
| `libcrypto3`                      | X          | X      |
| `libcurl-openssl4`                | X          |        |
| `libexpat1`                       | X          |        |
| `libgcc`                          | X          | X      |
| `libidn2`                         | X          |        |
| `libnghttp2-14`                   | X          |        |
| `libpcre2-8-0`                    | X          |        |
| `libpsl`                          | X          |        |
| `libssl3`                         | X          | X      |
| `libstdc++`                       | X          | X      |
| `libunistring`                    | X          |        |
| `libxcrypt`                       | X          | X      |
| `ncurses`                         | X          |        |
| `ncurses-terminfo-base`           | X          |        |
| `nginx-mainline`                  | X          | X      |
| `openssl-config-fipshardened`     | X          | X      |
| `openssl-provider-fips`           | X          | X      |
| `pcre`                            | X          | X      |
| `wget`                            | X          |        |
| `wolfi-baselayout`                | X          | X      |
| `zlib`                            | X          | X      |

