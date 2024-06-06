---
title: "spire-agent Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public spire-agent Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-06-06 00:48:16
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/spire-agent/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/spire-agent/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/spire-agent/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/spire-agent/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **spire-agent** Image.

|              | latest-dev                 | latest                     |
|--------------|----------------------------|----------------------------|
| Default User | `root`                     | `root`                     |
| Entrypoint   | `/usr/bin/spire-agent run` | `/usr/bin/spire-agent run` |
| CMD          | not specified              | not specified              |
| Workdir      | not specified              | not specified              |
| Has apk?     | yes                        | no                         |
| Has a shell? | yes                        | yes                        |

Check the [tags history page](/chainguard/chainguard-images/reference/spire-agent/tags_history/) for the full list of available tags.

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
| `ld-linux`               | X          | X      |
| `libbrotlicommon1`       | X          |        |
| `libbrotlidec1`          | X          |        |
| `libcap`                 | X          | X      |
| `libcap-utils`           | X          | X      |
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
| `spire-agent`            | X          | X      |
| `wget`                   | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `zlib`                   | X          |        |

