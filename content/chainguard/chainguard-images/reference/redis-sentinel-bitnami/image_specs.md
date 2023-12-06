---
title: "redis-sentinel-bitnami Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public redis-sentinel-bitnami Chainguard Image variants"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/redis-sentinel-bitnami/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/redis-sentinel-bitnami/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/redis-sentinel-bitnami/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/redis-sentinel-bitnami/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **redis-sentinel-bitnami** Image.

## Variants Compared
The **redis-sentinel-bitnami** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                                                                                     | latest                                                                                         |
|--------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Default User | `redis`                                                                                        | `redis`                                                                                        |
| Entrypoint   | `/opt/bitnami/scripts/redis-sentinel/entrypoint.sh /opt/bitnami/scripts/redis-sentinel/run.sh` | `/opt/bitnami/scripts/redis-sentinel/entrypoint.sh /opt/bitnami/scripts/redis-sentinel/run.sh` |
| CMD          | not specified                                                                                  | not specified                                                                                  |
| Workdir      | not specified                                                                                  | not specified                                                                                  |
| Has apk?     | yes                                                                                            | no                                                                                             |
| Has a shell? | yes                                                                                            | yes                                                                                            |

Check the [tags history page](/chainguard/chainguard-images/reference/redis-sentinel-bitnami/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                     | latest-dev | latest |
|-------------------------------------|------------|--------|
| `apk-tools`                         | X          |        |
| `bash`                              | X          | X      |
| `busybox`                           | X          | X      |
| `ca-certificates-bundle`            | X          | X      |
| `coreutils`                         | X          | X      |
| `git`                               | X          |        |
| `glibc`                             | X          | X      |
| `glibc-locale-posix`                | X          | X      |
| `ld-linux`                          | X          | X      |
| `libacl1`                           | X          | X      |
| `libattr1`                          | X          | X      |
| `libbrotlicommon1`                  | X          |        |
| `libbrotlidec1`                     | X          |        |
| `libcrypt1`                         | X          | X      |
| `libcrypto3`                        | X          | X      |
| `libcurl-openssl4`                  | X          |        |
| `libexpat1`                         | X          |        |
| `libnghttp2-14`                     | X          |        |
| `libpcre2-8-0`                      | X          |        |
| `libssl3`                           | X          | X      |
| `libxcrypt`                         | X          | X      |
| `ncurses`                           | X          | X      |
| `ncurses-terminfo-base`             | X          | X      |
| `openssl`                           | X          | X      |
| `openssl-config`                    | X          | X      |
| `openssl-provider-legacy`           | X          | X      |
| `posix-libc-utils`                  | X          | X      |
| `redis-7.2`                         | X          | X      |
| `redis-cli-7.2`                     | X          | X      |
| `redis-sentinel-7.2-bitnami-compat` | X          | X      |
| `wait-for-port`                     | X          | X      |
| `wolfi-baselayout`                  | X          | X      |
| `zlib`                              | X          |        |

