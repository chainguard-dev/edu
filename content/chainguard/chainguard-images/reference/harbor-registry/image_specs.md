---
title: "harbor-registry Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public harbor-registry Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-06-05 00:36:13
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

|              | latest-dev                                                       |
|--------------|------------------------------------------------------------------|
| Default User | `harbor`                                                         |
| Entrypoint   | `/usr/bin/registry_DO_NOT_USE_GC serve /etc/registry/config.yml` |
| CMD          | not specified                                                    |
| Workdir      | `/`                                                              |
| Has apk?     | yes                                                              |
| Has a shell? | yes                                                              |

Check the [tags history page](/chainguard/chainguard-images/reference/harbor-registry/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev |
|--------------------------|------------|
| `apk-tools`              | X          |
| `bash`                   | X          |
| `busybox`                | X          |
| `ca-certificates-bundle` | X          |
| `chainguard-baselayout`  | X          |
| `git`                    | X          |
| `glibc`                  | X          |
| `glibc-locale-posix`     | X          |
| `harbor-registry`        | X          |
| `ld-linux`               | X          |
| `libbrotlicommon1`       | X          |
| `libbrotlidec1`          | X          |
| `libcrypt1`              | X          |
| `libcrypto3`             | X          |
| `libcurl-openssl4`       | X          |
| `libexpat1`              | X          |
| `libidn2`                | X          |
| `libnghttp2-14`          | X          |
| `libpcre2-8-0`           | X          |
| `libpsl`                 | X          |
| `libssl3`                | X          |
| `libunistring`           | X          |
| `libxcrypt`              | X          |
| `ncurses`                | X          |
| `ncurses-terminfo-base`  | X          |
| `wget`                   | X          |
| `wolfi-baselayout`       | X          |
| `zlib`                   | X          |

