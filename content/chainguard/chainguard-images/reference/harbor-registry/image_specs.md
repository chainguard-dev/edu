---
title: "harbor-registry Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public harbor-registry Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-04-03 00:49:16
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/harbor-registry/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/harbor-registry/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/harbor-registry/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/harbor-registry/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **harbor-registry** Image.

|              | latest-dev                                                       | latest                                                           |
|--------------|------------------------------------------------------------------|------------------------------------------------------------------|
| Default User | `harbor`                                                         | `harbor`                                                         |
| Entrypoint   | `/usr/bin/registry_DO_NOT_USE_GC serve /etc/registry/config.yml` | `/usr/bin/registry_DO_NOT_USE_GC serve /etc/registry/config.yml` |
| CMD          | not specified                                                    | not specified                                                    |
| Workdir      | `/`                                                              | `/`                                                              |
| Has apk?     | yes                                                              | no                                                               |
| Has a shell? | yes                                                              | yes                                                              |

Check the [tags history page](/chainguard/chainguard-images/reference/harbor-registry/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          |        |
| `busybox`                | X          | X      |
| `ca-certificates-bundle` | X          | X      |
| `chainguard-baselayout`  | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `harbor-registry`        | X          | X      |
| `ld-linux`               | X          | X      |
| `libbrotlicommon1`       | X          |        |
| `libbrotlidec1`          | X          |        |
| `libcrypt1`              | X          | X      |
| `libcrypto3`             | X          |        |
| `libcurl-openssl4`       | X          |        |
| `libexpat1`              | X          |        |
| `libidn2`                | X          |        |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libpsl`                 | X          |        |
| `libssl3`                | X          |        |
| `libunistring`           | X          |        |
| `libxcrypt`              | X          | X      |
| `ncurses`                | X          |        |
| `ncurses-terminfo-base`  | X          |        |
| `openssl-config`         | X          |        |
| `wget`                   | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `zlib`                   | X          |        |

