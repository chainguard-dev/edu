---
title: "smarter-device-manager Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public smarter-device-manager Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-06-28 00:31:38
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/smarter-device-manager/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/smarter-device-manager/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/smarter-device-manager/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/smarter-device-manager/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **smarter-device-manager** Image.

|              | latest-dev                                                             |
|--------------|------------------------------------------------------------------------|
| Default User | `root`                                                                 |
| Entrypoint   | `/usr/bin/smarter-device-management`                                   |
| CMD          | `-config=/etc/smarter-device-manager/conf.yaml -logtostderr=true -v=2` |
| Workdir      | not specified                                                          |
| Has apk?     | yes                                                                    |
| Has a shell? | yes                                                                    |

Check the [tags history page](/chainguard/chainguard-images/reference/smarter-device-manager/tags_history/) for the full list of available tags.

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
| `smarter-device-manager` | X          |
| `wget`                   | X          |
| `wolfi-baselayout`       | X          |
| `zlib`                   | X          |

