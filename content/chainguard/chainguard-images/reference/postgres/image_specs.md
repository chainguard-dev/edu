---
title: "postgres Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public postgres Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/postgres/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/postgres/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/postgres/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/postgres/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **postgres** Image.

## Variants Compared
The **postgres** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                                                   | latest                                                       |
|--------------|--------------------------------------------------------------|--------------------------------------------------------------|
| Default User | `root`                                                       | `root`                                                       |
| Entrypoint   | `/var/lib/postgres/initdb/postgresql-entrypoint.sh postgres` | `/var/lib/postgres/initdb/postgresql-entrypoint.sh postgres` |
| CMD          | not specified                                                | not specified                                                |
| Workdir      | `/home/postgres`                                             | `/home/postgres`                                             |
| Has apk?     | yes                                                          | no                                                           |
| Has a shell? | yes                                                          | yes                                                          |

Check the [tags history page](/chainguard/chainguard-images/reference/postgres/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                | latest-dev | latest |
|--------------------------------|------------|--------|
| `apk-tools`                    | X          |        |
| `bash`                         | X          | X      |
| `busybox`                      | X          | X      |
| `ca-certificates-bundle`       | X          | X      |
| `git`                          | X          |        |
| `glibc`                        | X          | X      |
| `glibc-locale-en`              | X          | X      |
| `glibc-locale-posix`           | X          | X      |
| `ld-linux`                     | X          | X      |
| `libbrotlicommon1`             | X          |        |
| `libbrotlidec1`                | X          |        |
| `libcrypt1`                    | X          | X      |
| `libcrypto3`                   | X          | X      |
| `libcurl-rustls4`              | X          |        |
| `libedit`                      | X          | X      |
| `libexpat1`                    | X          |        |
| `libgcc`                       | X          |        |
| `libnghttp2-14`                | X          |        |
| `libpcre2-8-0`                 | X          |        |
| `libpq-15`                     | X          | X      |
| `libssl3`                      | X          | X      |
| `libuuid`                      | X          | X      |
| `ncurses`                      | X          | X      |
| `ncurses-terminfo-base`        | X          | X      |
| `openssl-config`               | X          | X      |
| `postgresql-15`                | X          | X      |
| `postgresql-15-client`         | X          | X      |
| `postgresql-15-contrib`        | X          | X      |
| `postgresql-15-oci-entrypoint` | X          | X      |
| `su-exec`                      | X          | X      |
| `wolfi-baselayout`             | X          | X      |
| `zlib`                         | X          | X      |

