---
title: "harbor-registry-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public harbor-registry-fips Chainguard Image."
date: 2024-05-03 00:45:55
lastmod: 2024-05-03 00:45:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/harbor-registry-fips/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/harbor-registry-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/harbor-registry-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/harbor-registry-fips/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **harbor-registry-fips** Image.

|              | latest-dev                                                       | latest                                                           |
|--------------|------------------------------------------------------------------|------------------------------------------------------------------|
| Default User | `harbor`                                                         | `harbor`                                                         |
| Entrypoint   | `/usr/bin/registry_DO_NOT_USE_GC serve /etc/registry/config.yml` | `/usr/bin/registry_DO_NOT_USE_GC serve /etc/registry/config.yml` |
| CMD          | not specified                                                    | not specified                                                    |
| Workdir      | `/`                                                              | `/`                                                              |
| Has apk?     | yes                                                              | no                                                               |
| Has a shell? | yes                                                              | no                                                               |

Check the [tags history page](/chainguard/chainguard-images/reference/harbor-registry-fips/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                               | latest-dev | latest |
|-------------------------------|------------|--------|
| `apk-tools`                   | X          |        |
| `bash`                        | X          |        |
| `busybox`                     | X          |        |
| `ca-certificates-bundle`      | X          | X      |
| `chainguard-baselayout`       | X          | X      |
| `git`                         | X          |        |
| `glibc`                       | X          | X      |
| `glibc-locale-posix`          | X          | X      |
| `harbor-registry-fips`        | X          | X      |
| `ld-linux`                    | X          | X      |
| `libbrotlicommon1`            | X          |        |
| `libbrotlidec1`               | X          |        |
| `libcrypt1`                   | X          |        |
| `libcrypto3`                  | X          | X      |
| `libcurl-openssl4`            | X          |        |
| `libexpat1`                   | X          |        |
| `libidn2`                     | X          |        |
| `libnghttp2-14`               | X          |        |
| `libpcre2-8-0`                | X          |        |
| `libpsl`                      | X          |        |
| `libssl3`                     | X          | X      |
| `libunistring`                | X          |        |
| `libxcrypt`                   | X          |        |
| `ncurses`                     | X          |        |
| `ncurses-terminfo-base`       | X          |        |
| `openssl-config-fipshardened` | X          | X      |
| `openssl-provider-fips`       | X          | X      |
| `wget`                        | X          |        |
| `wolfi-baselayout`            | X          | X      |
| `zlib`                        | X          |        |

