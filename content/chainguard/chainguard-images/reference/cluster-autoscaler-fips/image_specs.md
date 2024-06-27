---
title: "cluster-autoscaler-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public cluster-autoscaler-fips Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-06-27 00:41:27
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/cluster-autoscaler-fips/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/cluster-autoscaler-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/cluster-autoscaler-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cluster-autoscaler-fips/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **cluster-autoscaler-fips** Image.

|              | latest-dev                    | latest                        |
|--------------|-------------------------------|-------------------------------|
| Default User | `cluster-autoscaler`          | `cluster-autoscaler`          |
| Entrypoint   | `/usr/bin/cluster-autoscaler` | `/usr/bin/cluster-autoscaler` |
| CMD          | not specified                 | not specified                 |
| Workdir      | `/`                           | `/`                           |
| Has apk?     | yes                           | no                            |
| Has a shell? | yes                           | no                            |

Check the [tags history page](/chainguard/chainguard-images/reference/cluster-autoscaler-fips/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                       | latest-dev | latest |
|---------------------------------------|------------|--------|
| `apk-tools`                           | X          |        |
| `bash`                                | X          |        |
| `busybox`                             | X          |        |
| `ca-certificates-bundle`              | X          | X      |
| `chainguard-baselayout`               | X          | X      |
| `cluster-autoscaler-fips-1.30`        | X          | X      |
| `cluster-autoscaler-fips-1.30-compat` | X          | X      |
| `git`                                 | X          |        |
| `glibc`                               | X          | X      |
| `glibc-locale-posix`                  | X          | X      |
| `ld-linux`                            | X          | X      |
| `libbrotlicommon1`                    | X          |        |
| `libbrotlidec1`                       | X          |        |
| `libcrypt1`                           | X          |        |
| `libcrypto3`                          | X          | X      |
| `libcurl-openssl4`                    | X          |        |
| `libexpat1`                           | X          |        |
| `libidn2`                             | X          |        |
| `libnghttp2-14`                       | X          |        |
| `libpcre2-8-0`                        | X          |        |
| `libpsl`                              | X          |        |
| `libssl3`                             | X          | X      |
| `libunistring`                        | X          |        |
| `libxcrypt`                           | X          |        |
| `ncurses`                             | X          |        |
| `ncurses-terminfo-base`               | X          |        |
| `openssl-config-fipshardened`         | X          | X      |
| `openssl-provider-fips`               | X          | X      |
| `wget`                                | X          |        |
| `wolfi-baselayout`                    | X          | X      |
| `zlib`                                | X          |        |

