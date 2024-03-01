---
title: "opentelemetry-collector-contrib Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public opentelemetry-collector-contrib Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-03-01 12:14:22
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector-contrib/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/opentelemetry-collector-contrib/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector-contrib/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector-contrib/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **opentelemetry-collector-contrib** Image.

|              | latest-dev                 | latest                     |
|--------------|----------------------------|----------------------------|
| Default User | `nonroot`                  | `nonroot`                  |
| Entrypoint   | `/usr/bin/otelcol-contrib` | `/usr/bin/otelcol-contrib` |
| CMD          | not specified              | not specified              |
| Workdir      | not specified              | not specified              |
| Has apk?     | yes                        | no                         |
| Has a shell? | yes                        | yes                        |

Check the [tags history page](/chainguard/chainguard-images/reference/opentelemetry-collector-contrib/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                          | latest-dev | latest |
|------------------------------------------|------------|--------|
| `apk-tools`                              | X          |        |
| `bash`                                   | X          |        |
| `busybox`                                | X          | X      |
| `ca-certificates-bundle`                 | X          | X      |
| `chainguard-baselayout`                  | X          | X      |
| `git`                                    | X          |        |
| `glibc`                                  | X          | X      |
| `glibc-locale-posix`                     | X          | X      |
| `ld-linux`                               | X          | X      |
| `libbrotlicommon1`                       | X          |        |
| `libbrotlidec1`                          | X          |        |
| `libcrypt1`                              | X          | X      |
| `libcrypto3`                             | X          |        |
| `libcurl-openssl4`                       | X          |        |
| `libexpat1`                              | X          |        |
| `libidn2`                                | X          |        |
| `libnghttp2-14`                          | X          |        |
| `libpcre2-8-0`                           | X          |        |
| `libpsl`                                 | X          |        |
| `libssl3`                                | X          |        |
| `libunistring`                           | X          |        |
| `ncurses`                                | X          |        |
| `ncurses-terminfo-base`                  | X          |        |
| `openssl-config`                         | X          |        |
| `opentelemetry-collector-contrib`        | X          | X      |
| `opentelemetry-collector-contrib-compat` | X          | X      |
| `wget`                                   | X          |        |
| `wolfi-baselayout`                       | X          | X      |
| `zlib`                                   | X          |        |

