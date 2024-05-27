---
title: "haproxy-ingress Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public haproxy-ingress Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-05-27 00:43:34
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/haproxy-ingress/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/haproxy-ingress/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/haproxy-ingress/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/haproxy-ingress/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **haproxy-ingress** Image.

|              | latest-dev                                | latest                                    |
|--------------|-------------------------------------------|-------------------------------------------|
| Default User | `haproxy`                                 | `haproxy`                                 |
| Entrypoint   | `/usr/bin/dumb-init -- /usr/bin/start.sh` | `/usr/bin/dumb-init -- /usr/bin/start.sh` |
| CMD          | not specified                             | not specified                             |
| Workdir      | not specified                             | not specified                             |
| Has apk?     | yes                                       | no                                        |
| Has a shell? | yes                                       | yes                                       |

Check the [tags history page](/chainguard/chainguard-images/reference/haproxy-ingress/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          |        |
| `busybox`                | X          | X      |
| `ca-certificates-bundle` | X          | X      |
| `chainguard-baselayout`  | X          | X      |
| `dumb-init`              | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `haproxy-2.9`            | X          | X      |
| `haproxy-ingress`        | X          | X      |
| `haproxy-ingress-compat` | X          | X      |
| `ld-linux`               | X          | X      |
| `libbrotlicommon1`       | X          |        |
| `libbrotlidec1`          | X          |        |
| `libcrypt1`              | X          | X      |
| `libcrypto3`             | X          | X      |
| `libcurl-openssl4`       | X          |        |
| `libexpat1`              | X          |        |
| `libgcc`                 | X          | X      |
| `libidn2`                | X          |        |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          | X      |
| `libpcre2-posix-3`       | X          | X      |
| `libpsl`                 | X          |        |
| `libssl3`                | X          | X      |
| `libunistring`           | X          |        |
| `libxcrypt`              | X          | X      |
| `lua-json4`              | X          | X      |
| `ncurses`                | X          |        |
| `ncurses-terminfo-base`  | X          |        |
| `wget`                   | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `zlib`                   | X          |        |

