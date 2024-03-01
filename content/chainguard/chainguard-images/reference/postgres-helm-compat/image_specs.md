---
title: "postgres-helm-compat Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public postgres-helm-compat Chainguard Image."
date: 2024-02-29 16:25:55
lastmod: 2024-02-29 16:25:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/postgres-helm-compat/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/postgres-helm-compat/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/postgres-helm-compat/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/postgres-helm-compat/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **postgres-helm-compat** Image.

|              | latest-dev                                                                             | latest                                                                                 |
|--------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Default User | `postgres`                                                                             | `postgres`                                                                             |
| Entrypoint   | `/opt/bitnami/scripts/postgresql/entrypoint.sh /opt/bitnami/scripts/postgresql/run.sh` | `/opt/bitnami/scripts/postgresql/entrypoint.sh /opt/bitnami/scripts/postgresql/run.sh` |
| CMD          | not specified                                                                          | not specified                                                                          |
| Workdir      | not specified                                                                          | not specified                                                                          |
| Has apk?     | yes                                                                                    | no                                                                                     |
| Has a shell? | yes                                                                                    | yes                                                                                    |

Check the [tags history page](/chainguard/chainguard-images/reference/postgres-helm-compat/tags_history/) for the full list of available tags.

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
| `ld-linux`                     | X          | X      |
| `libbrotlicommon1`             | X          |        |
| `libbrotlidec1`                | X          |        |
| `libcrypt1`                    | X          | X      |
| `libcrypto3`                   | X          | X      |
| `libcurl-openssl4`             | X          |        |
| `libedit`                      | X          | X      |
| `libexpat1`                    | X          |        |
| `libidn2`                      | X          |        |
| `libnghttp2-14`                | X          |        |
| `libpcre2-8-0`                 | X          |        |
| `libpq-15`                     | X          | X      |
| `libpsl`                       | X          |        |
| `libssl3`                      | X          | X      |
| `libunistring`                 | X          |        |
| `libuuid`                      | X          | X      |
| `ncurses`                      | X          | X      |
| `ncurses-terminfo-base`        | X          | X      |
| `net-tools`                    | X          | X      |
| `openssl-config`               | X          | X      |
| `pgaudit-15`                   | X          | X      |
| `postgresql-15`                | X          | X      |
| `postgresql-15-bitnami-compat` | X          | X      |
| `postgresql-15-client`         | X          | X      |
| `postgresql-15-contrib`        | X          | X      |
| `postgresql-15-oci-entrypoint` | X          | X      |
| `su-exec`                      | X          | X      |
| `wget`                         | X          |        |
| `wolfi-baselayout`             | X          | X      |
| `zlib`                         | X          | X      |

