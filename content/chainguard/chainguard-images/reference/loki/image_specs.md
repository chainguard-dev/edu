---
title: "loki Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public loki Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-06-01 00:50:07
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/loki/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/loki/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/loki/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/loki/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **loki** Image.

|              | latest-dev                                 | latest                                     |
|--------------|--------------------------------------------|--------------------------------------------|
| Default User | `loki`                                     | `loki`                                     |
| Entrypoint   | `/usr/bin/loki`                            | `/usr/bin/loki`                            |
| CMD          | `-config.file=/etc/loki/local-config.yaml` | `-config.file=/etc/loki/local-config.yaml` |
| Workdir      | not specified                              | not specified                              |
| Has apk?     | yes                                        | no                                         |
| Has a shell? | yes                                        | no                                         |

Check the [tags history page](/chainguard/chainguard-images/reference/loki/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          |        |
| `busybox`                | X          |        |
| `ca-certificates-bundle` | X          | X      |
| `chainguard-baselayout`  | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          |        |
| `glibc-locale-posix`     | X          | X      |
| `ld-linux`               | X          |        |
| `libbrotlicommon1`       | X          |        |
| `libbrotlidec1`          | X          |        |
| `libcrypt1`              | X          |        |
| `libcrypto3`             | X          |        |
| `libcurl-openssl4`       | X          |        |
| `libexpat1`              | X          |        |
| `libidn2`                | X          |        |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libpsl`                 | X          |        |
| `libssl3`                | X          |        |
| `libunistring`           | X          |        |
| `libxcrypt`              | X          |        |
| `loki-3.0`               | X          | X      |
| `ncurses`                | X          |        |
| `ncurses-terminfo-base`  | X          |        |
| `wget`                   | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `zlib`                   | X          |        |

