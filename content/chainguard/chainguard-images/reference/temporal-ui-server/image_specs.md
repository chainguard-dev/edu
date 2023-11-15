---
title: "temporal-ui-server Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public temporal-ui-server Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/temporal-ui-server/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/temporal-ui-server/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/temporal-ui-server/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/temporal-ui-server/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **temporal-ui-server** Image.

## Variants Compared
The **temporal-ui-server** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                           | latest                               |
|--------------|--------------------------------------|--------------------------------------|
| Default User | `ui-server`                          | `ui-server`                          |
| Entrypoint   | `/home/ui-server/start-ui-server.sh` | `/home/ui-server/start-ui-server.sh` |
| CMD          | not specified                        | not specified                        |
| Workdir      | `/home/ui-server/`                   | `/home/ui-server/`                   |
| Has apk?     | yes                                  | no                                   |
| Has a shell? | yes                                  | yes                                  |

Check the [tags history page](/chainguard/chainguard-images/reference/temporal-ui-server/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                     | latest-dev | latest |
|-------------------------------------|------------|--------|
| `apk-tools`                         | X          |        |
| `bash`                              | X          | X      |
| `busybox`                           | X          |        |
| `ca-certificates-bundle`            | X          | X      |
| `dockerize`                         | X          | X      |
| `git`                               | X          |        |
| `glibc`                             | X          | X      |
| `glibc-locale-posix`                | X          | X      |
| `ld-linux`                          | X          | X      |
| `libbrotlicommon1`                  | X          |        |
| `libbrotlidec1`                     | X          |        |
| `libcrypt1`                         | X          |        |
| `libcrypto3`                        | X          |        |
| `libcurl-openssl4`                  | X          |        |
| `libexpat1`                         | X          |        |
| `libnghttp2-14`                     | X          |        |
| `libpcre2-8-0`                      | X          |        |
| `libssl3`                           | X          |        |
| `ncurses`                           | X          | X      |
| `ncurses-terminfo-base`             | X          | X      |
| `openssl-config`                    | X          |        |
| `temporal-ui-server`                | X          | X      |
| `temporal-ui-server-oci-entrypoint` | X          | X      |
| `wolfi-baselayout`                  | X          | X      |
| `zlib`                              | X          |        |

