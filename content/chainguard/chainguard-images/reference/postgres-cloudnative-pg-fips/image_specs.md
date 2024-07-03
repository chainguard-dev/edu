---
title: "postgres-cloudnative-pg-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public postgres-cloudnative-pg-fips Chainguard Image."
date: 2024-07-01 00:36:20
lastmod: 2024-07-01 00:36:20
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/postgres-cloudnative-pg-fips/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/postgres-cloudnative-pg-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/postgres-cloudnative-pg-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/postgres-cloudnative-pg-fips/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **postgres-cloudnative-pg-fips** Image.

|              | latest-dev                               | latest                                   |
|--------------|------------------------------------------|------------------------------------------|
| Default User | `postgres`                               | `postgres`                               |
| Entrypoint   | `/usr/bin/docker-entrypoint.sh postgres` | `/usr/bin/docker-entrypoint.sh postgres` |
| CMD          | not specified                            | not specified                            |
| Workdir      | `/home/postgres`                         | `/home/postgres`                         |
| Has apk?     | yes                                      | no                                       |
| Has a shell? | yes                                      | yes                                      |

Check the [tags history page](/chainguard/chainguard-images/reference/postgres-cloudnative-pg-fips/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                     | latest-dev | latest |
|-------------------------------------|------------|--------|
| `apk-tools`                         | X          |        |
| `barman-cloudnative-pg`             | X          | X      |
| `bash`                              | X          | X      |
| `busybox`                           | X          | X      |
| `ca-certificates-bundle`            | X          | X      |
| `chainguard-baselayout`             | X          | X      |
| `gdbm`                              | X          | X      |
| `git`                               | X          |        |
| `glibc`                             | X          | X      |
| `glibc-locale-en`                   | X          | X      |
| `glibc-locale-posix`                | X          | X      |
| `gosu-fips`                         | X          | X      |
| `icu`                               | X          | X      |
| `ld-linux`                          | X          | X      |
| `libbrotlicommon1`                  | X          |        |
| `libbrotlidec1`                     | X          |        |
| `libbz2-1`                          | X          | X      |
| `libcrypt1`                         | X          | X      |
| `libcrypto3`                        | X          | X      |
| `libcurl-openssl4`                  | X          |        |
| `libedit`                           | X          | X      |
| `libexpat1`                         | X          | X      |
| `libffi`                            | X          | X      |
| `libgcc`                            | X          | X      |
| `libidn2`                           | X          |        |
| `libnghttp2-14`                     | X          |        |
| `libpcre2-8-0`                      | X          |        |
| `libpq-16`                          | X          | X      |
| `libpsl`                            | X          |        |
| `libssl3`                           | X          | X      |
| `libstdc++`                         | X          | X      |
| `libunistring`                      | X          |        |
| `libuuid`                           | X          | X      |
| `libxcrypt`                         | X          | X      |
| `mpdecimal`                         | X          | X      |
| `ncurses`                           | X          | X      |
| `ncurses-terminfo-base`             | X          | X      |
| `openssl-config-fipshardened`       | X          | X      |
| `openssl-provider-fips`             | X          | X      |
| `pg-failover-slots-16`              | X          | X      |
| `pgaudit-16`                        | X          | X      |
| `pgvector-16`                       | X          | X      |
| `posix-libc-utils`                  | X          | X      |
| `postgresql-16`                     | X          | X      |
| `postgresql-16-base`                | X          | X      |
| `postgresql-16-client`              | X          | X      |
| `postgresql-16-client-base`         | X          | X      |
| `postgresql-16-contrib`             | X          | X      |
| `postgresql-16-oci-entrypoint`      | X          | X      |
| `postgresql-16-oci-entrypoint-base` | X          | X      |
| `py3-psycopg2`                      | X          | X      |
| `py3.12-setuptools`                 | X          | X      |
| `python-3.12`                       | X          | X      |
| `python-3.12-base`                  | X          | X      |
| `readline`                          | X          | X      |
| `sqlite-libs`                       | X          | X      |
| `wget`                              | X          |        |
| `wolfi-baselayout`                  | X          | X      |
| `xz`                                | X          | X      |
| `zlib`                              | X          | X      |

