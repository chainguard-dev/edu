---
title: "keda Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public keda Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-03-28 00:50:32
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/keda/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/keda/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/keda/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/keda/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **keda** Image.

|              | latest-dev                                                 | latest                                                     |
|--------------|------------------------------------------------------------|------------------------------------------------------------|
| Default User | `nonroot`                                                  | `nonroot`                                                  |
| Entrypoint   | `/usr/bin/keda --zap-log-level=info --zap-encoder=console` | `/usr/bin/keda --zap-log-level=info --zap-encoder=console` |
| CMD          | not specified                                              | not specified                                              |
| Workdir      | not specified                                              | not specified                                              |
| Has apk?     | yes                                                        | no                                                         |
| Has a shell? | yes                                                        | yes                                                        |

Check the [tags history page](/chainguard/chainguard-images/reference/keda/tags_history/) for the full list of available tags.

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
| `keda`                   | X          | X      |
| `keda-compat`            | X          | X      |
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
| `tzdata`                 | X          | X      |
| `wget`                   | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `zlib`                   | X          |        |

