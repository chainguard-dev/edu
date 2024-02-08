---
title: "redis-cluster-bitnami Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public redis-cluster-bitnami Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-02-08 00:18:32
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/redis-cluster-bitnami/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/redis-cluster-bitnami/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/redis-cluster-bitnami/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/redis-cluster-bitnami/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **redis-cluster-bitnami** Image.

## Variants Compared
The **redis-cluster-bitnami** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                                                                                   | latest                                                                                       |
|--------------|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| Default User | `redis`                                                                                      | `redis`                                                                                      |
| Entrypoint   | `/opt/bitnami/scripts/redis-cluster/entrypoint.sh /opt/bitnami/scripts/redis-cluster/run.sh` | `/opt/bitnami/scripts/redis-cluster/entrypoint.sh /opt/bitnami/scripts/redis-cluster/run.sh` |
| CMD          | not specified                                                                                | not specified                                                                                |
| Workdir      | not specified                                                                                | not specified                                                                                |
| Has apk?     | yes                                                                                          | no                                                                                           |
| Has a shell? | yes                                                                                          | yes                                                                                          |

Check the [tags history page](/chainguard/chainguard-images/reference/redis-cluster-bitnami/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                    | latest-dev | latest |
|------------------------------------|------------|--------|
| `apk-tools`                        | X          |        |
| `bash`                             | X          | X      |
| `busybox`                          | X          | X      |
| `ca-certificates-bundle`           | X          | X      |
| `coreutils`                        | X          | X      |
| `git`                              | X          |        |
| `glibc`                            | X          | X      |
| `glibc-locale-posix`               | X          | X      |
| `ld-linux`                         | X          | X      |
| `libacl1`                          | X          | X      |
| `libattr1`                         | X          | X      |
| `libbrotlicommon1`                 | X          |        |
| `libbrotlidec1`                    | X          |        |
| `libcrypto3`                       | X          | X      |
| `libcurl-openssl4`                 | X          |        |
| `libexpat1`                        | X          |        |
| `libidn2`                          | X          |        |
| `libnghttp2-14`                    | X          |        |
| `libpcre2-8-0`                     | X          |        |
| `libpsl`                           | X          |        |
| `libssl3`                          | X          | X      |
| `libunistring`                     | X          |        |
| `libxcrypt`                        | X          | X      |
| `ncurses`                          | X          | X      |
| `ncurses-terminfo-base`            | X          | X      |
| `openssl`                          | X          | X      |
| `openssl-config`                   | X          | X      |
| `openssl-provider-legacy`          | X          | X      |
| `posix-libc-utils`                 | X          | X      |
| `redis-7.2`                        | X          | X      |
| `redis-cli-7.2`                    | X          | X      |
| `redis-cluster-7.2-bitnami-compat` | X          | X      |
| `wait-for-port`                    | X          | X      |
| `wget`                             | X          |        |
| `wolfi-baselayout`                 | X          | X      |
| `zlib`                             | X          |        |

