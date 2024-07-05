---
title: "kibana Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public kibana Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-07-05 00:42:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kibana/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/kibana/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kibana/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kibana/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **kibana** Image.

|              | latest-dev                     | latest                         |
|--------------|--------------------------------|--------------------------------|
| Default User | `kibana`                       | `kibana`                       |
| Entrypoint   | `/sbin/tini -g --`             | `/sbin/tini -g --`             |
| CMD          | `/usr/share/kibana/bin/kibana` | `/usr/share/kibana/bin/kibana` |
| Workdir      | not specified                  | not specified                  |
| Has apk?     | yes                            | no                             |
| Has a shell? | yes                            | yes                            |

Check the [tags history page](/chainguard/chainguard-images/reference/kibana/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          | X      |
| `busybox`                | X          | X      |
| `ca-certificates-bundle` | X          | X      |
| `chainguard-baselayout`  | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `kibana-8.13`            | X          | X      |
| `ld-linux`               | X          | X      |
| `libbrotlicommon1`       | X          |        |
| `libbrotlidec1`          | X          |        |
| `libcrypt1`              | X          | X      |
| `libcrypto3`             | X          |        |
| `libcurl-openssl4`       | X          |        |
| `libexpat1`              | X          | X      |
| `libgcc`                 | X          | X      |
| `libidn2`                | X          |        |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libpsl`                 | X          |        |
| `libssl3`                | X          |        |
| `libstdc++`              | X          | X      |
| `libunistring`           | X          |        |
| `libxcrypt`              | X          | X      |
| `ncurses`                | X          | X      |
| `ncurses-terminfo-base`  | X          | X      |
| `tini`                   | X          | X      |
| `wget`                   | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `zlib`                   | X          |        |

