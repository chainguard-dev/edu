---
title: "harbor-db Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public harbor-db Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-06-23 00:43:06
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/harbor-db/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/harbor-db/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/harbor-db/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/harbor-db/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **harbor-db** Image.

|              | latest-dev                            | latest                                |
|--------------|---------------------------------------|---------------------------------------|
| Default User | `postgres`                            | `postgres`                            |
| Entrypoint   | `/usr/bin/docker-entrypoint.sh 14 15` | `/usr/bin/docker-entrypoint.sh 14 15` |
| CMD          | not specified                         | not specified                         |
| Workdir      | `/`                                   | `/`                                   |
| Has apk?     | yes                                   | no                                    |
| Has a shell? | yes                                   | yes                                   |

Check the [tags history page](/chainguard/chainguard-images/reference/harbor-db/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                             | latest-dev | latest |
|-----------------------------|------------|--------|
| `apk-tools`                 | X          |        |
| `bash`                      | X          | X      |
| `bc`                        | X          | X      |
| `busybox`                   | X          | X      |
| `ca-certificates-bundle`    | X          | X      |
| `chainguard-baselayout`     | X          | X      |
| `findutils`                 | X          | X      |
| `git`                       | X          |        |
| `glibc`                     | X          | X      |
| `glibc-locale-en`           | X          | X      |
| `glibc-locale-posix`        | X          | X      |
| `gzip`                      | X          | X      |
| `harbor-2.11-db`            | X          | X      |
| `ld-linux`                  | X          | X      |
| `libbrotlicommon1`          | X          |        |
| `libbrotlidec1`             | X          |        |
| `libcrypt1`                 | X          | X      |
| `libcrypto3`                | X          | X      |
| `libcurl-openssl4`          | X          |        |
| `libedit`                   | X          | X      |
| `libexpat1`                 | X          |        |
| `libidn2`                   | X          |        |
| `libnghttp2-14`             | X          |        |
| `libpcre2-8-0`              | X          |        |
| `libpq-16`                  | X          | X      |
| `libpsl`                    | X          |        |
| `libssl3`                   | X          | X      |
| `libunistring`              | X          |        |
| `libuuid`                   | X          | X      |
| `libxcrypt`                 | X          | X      |
| `ncurses`                   | X          | X      |
| `ncurses-terminfo-base`     | X          | X      |
| `net-tools`                 | X          | X      |
| `posix-libc-utils`          | X          | X      |
| `postgresql-14-base`        | X          | X      |
| `postgresql-14-client-base` | X          | X      |
| `postgresql-15`             | X          | X      |
| `postgresql-15-base`        | X          | X      |
| `postgresql-15-client`      | X          | X      |
| `postgresql-15-client-base` | X          | X      |
| `postgresql-15-contrib`     | X          | X      |
| `sqlite-libs`               | X          | X      |
| `util-linux`                | X          | X      |
| `wget`                      | X          |        |
| `wolfi-baselayout`          | X          | X      |
| `zlib`                      | X          | X      |

