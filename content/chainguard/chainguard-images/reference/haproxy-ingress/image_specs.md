---
title: "haproxy-ingress Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public haproxy-ingress Chainguard Image variants"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/haproxy-ingress/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/haproxy-ingress/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/haproxy-ingress/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/haproxy-ingress/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **haproxy-ingress** Image.

## Variants Compared
The **haproxy-ingress** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

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
| `dumb-init`              | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `haproxy`                | X          | X      |
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
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          | X      |
| `libpcre2-posix-3`       | X          | X      |
| `libssl3`                | X          | X      |
| `lua-json4`              | X          | X      |
| `ncurses`                | X          |        |
| `ncurses-terminfo-base`  | X          |        |
| `openssl-config`         | X          | X      |
| `wolfi-baselayout`       | X          | X      |
| `zlib`                   | X          |        |

