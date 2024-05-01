---
title: "memcached-bitnami Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public memcached-bitnami Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-05-01 00:46:56
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/memcached-bitnami/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/memcached-bitnami/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/memcached-bitnami/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/memcached-bitnami/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **memcached-bitnami** Image.

|              | latest-dev                                                                           | latest                                                                               |
|--------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Default User | `nonroot`                                                                            | `nonroot`                                                                            |
| Entrypoint   | `/opt/bitnami/scripts/memcached/entrypoint.sh /opt/bitnami/scripts/memcached/run.sh` | `/opt/bitnami/scripts/memcached/entrypoint.sh /opt/bitnami/scripts/memcached/run.sh` |
| CMD          | not specified                                                                        | not specified                                                                        |
| Workdir      | not specified                                                                        | not specified                                                                        |
| Has apk?     | yes                                                                                  | no                                                                                   |
| Has a shell? | yes                                                                                  | yes                                                                                  |

Check the [tags history page](/chainguard/chainguard-images/reference/memcached-bitnami/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                            | latest-dev | latest |
|----------------------------|------------|--------|
| `apk-tools`                | X          |        |
| `bash`                     | X          | X      |
| `busybox`                  | X          | X      |
| `ca-certificates-bundle`   | X          | X      |
| `chainguard-baselayout`    | X          | X      |
| `cyrus-sasl`               | X          | X      |
| `gdbm`                     | X          | X      |
| `git`                      | X          |        |
| `glibc`                    | X          | X      |
| `glibc-locale-posix`       | X          | X      |
| `heimdal`                  | X          | X      |
| `ld-linux`                 | X          | X      |
| `libbrotlicommon1`         | X          |        |
| `libbrotlidec1`            | X          |        |
| `libcrypt1`                | X          | X      |
| `libcrypto3`               | X          | X      |
| `libcurl-openssl4`         | X          |        |
| `libevent`                 | X          | X      |
| `libexpat1`                | X          |        |
| `libidn2`                  | X          |        |
| `libnghttp2-14`            | X          |        |
| `libpcre2-8-0`             | X          |        |
| `libpsl`                   | X          |        |
| `libseccomp`               | X          | X      |
| `libssl3`                  | X          | X      |
| `libunistring`             | X          |        |
| `libxcrypt`                | X          | X      |
| `memcached`                | X          | X      |
| `memcached-bitnami-compat` | X          | X      |
| `ncurses`                  | X          | X      |
| `ncurses-terminfo-base`    | X          | X      |
| `readline`                 | X          | X      |
| `sqlite-libs`              | X          | X      |
| `wget`                     | X          |        |
| `wolfi-baselayout`         | X          | X      |
| `zlib`                     | X          |        |

