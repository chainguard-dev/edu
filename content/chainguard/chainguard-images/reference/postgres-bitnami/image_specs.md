---
title: "postgres-bitnami Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public postgres-bitnami Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-04-15 03:08:24
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/postgres-bitnami/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/postgres-bitnami/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/postgres-bitnami/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/postgres-bitnami/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **postgres-bitnami** Image.

|              | latest-dev                                                                             | latest                                                                                 |
|--------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Default User | `postgres`                                                                             | `postgres`                                                                             |
| Entrypoint   | `/opt/bitnami/scripts/postgresql/entrypoint.sh /opt/bitnami/scripts/postgresql/run.sh` | `/opt/bitnami/scripts/postgresql/entrypoint.sh /opt/bitnami/scripts/postgresql/run.sh` |
| CMD          | not specified                                                                          | not specified                                                                          |
| Workdir      | not specified                                                                          | not specified                                                                          |
| Has apk?     | yes                                                                                    | no                                                                                     |
| Has a shell? | yes                                                                                    | yes                                                                                    |

Check the [tags history page](/chainguard/chainguard-images/reference/postgres-bitnami/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                | latest-dev | latest |
|--------------------------------|------------|--------|
| `apk-tools`                    | X          |        |
| `bash`                         | X          | X      |
| `busybox`                      | X          | X      |
| `ca-certificates-bundle`       | X          | X      |
| `chainguard-baselayout`        | X          | X      |
| `git`                          | X          |        |
| `glibc`                        | X          | X      |
| `glibc-locale-en`              | X          | X      |
| `glibc-locale-posix`           | X          | X      |
| `icu`                          | X          | X      |
| `ld-linux`                     | X          | X      |
| `libbrotlicommon1`             | X          |        |
| `libbrotlidec1`                | X          |        |
| `libcrypt1`                    | X          | X      |
| `libcrypto3`                   | X          | X      |
| `libcurl-openssl4`             | X          |        |
| `libedit`                      | X          | X      |
| `libexpat1`                    | X          |        |
| `libgcc`                       | X          | X      |
| `libidn2`                      | X          |        |
| `libnghttp2-14`                | X          |        |
| `libpcre2-8-0`                 | X          |        |
| `libpq-16`                     | X          | X      |
| `libpsl`                       | X          |        |
| `libssl3`                      | X          | X      |
| `libstdc++`                    | X          | X      |
| `libunistring`                 | X          |        |
| `libuuid`                      | X          | X      |
| `libxcrypt`                    | X          | X      |
| `ncurses`                      | X          | X      |
| `ncurses-terminfo-base`        | X          | X      |
| `net-tools`                    | X          | X      |
| `openssl-config`               | X          | X      |
| `pgaudit-16`                   | X          | X      |
| `postgresql-16`                | X          | X      |
| `postgresql-16-bitnami-compat` | X          | X      |
| `postgresql-16-client`         | X          | X      |
| `postgresql-16-contrib`        | X          | X      |
| `postgresql-16-oci-entrypoint` | X          | X      |
| `su-exec`                      | X          | X      |
| `wget`                         | X          |        |
| `wolfi-baselayout`             | X          | X      |
| `zlib`                         | X          | X      |

