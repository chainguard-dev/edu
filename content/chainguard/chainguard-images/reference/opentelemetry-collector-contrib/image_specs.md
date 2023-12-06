---
title: "opentelemetry-collector-contrib Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public opentelemetry-collector-contrib Chainguard Image variants"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector-contrib/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/opentelemetry-collector-contrib/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector-contrib/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/opentelemetry-collector-contrib/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **opentelemetry-collector-contrib** Image.

## Variants Compared
The **opentelemetry-collector-contrib** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

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
| `libnghttp2-14`                          | X          |        |
| `libpcre2-8-0`                           | X          |        |
| `libssl3`                                | X          |        |
| `ncurses`                                | X          |        |
| `ncurses-terminfo-base`                  | X          |        |
| `openssl-config`                         | X          |        |
| `opentelemetry-collector-contrib`        | X          | X      |
| `opentelemetry-collector-contrib-compat` | X          | X      |
| `wolfi-baselayout`                       | X          | X      |
| `zlib`                                   | X          |        |

