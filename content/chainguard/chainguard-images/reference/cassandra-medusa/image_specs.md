---
title: "cassandra-medusa Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public cassandra-medusa Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-02-12 00:21:23
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/cassandra-medusa/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/cassandra-medusa/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/cassandra-medusa/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cassandra-medusa/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **cassandra-medusa** Image.

## Variants Compared
The **cassandra-medusa** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                             | latest                                 |
|--------------|----------------------------------------|----------------------------------------|
| Default User | `cassandra`                            | `cassandra`                            |
| Entrypoint   | `/home/cassandra/docker-entrypoint.sh` | `/home/cassandra/docker-entrypoint.sh` |
| CMD          | not specified                          | not specified                          |
| Workdir      | `/home/cassandra/`                     | `/home/cassandra/`                     |
| Has apk?     | yes                                    | no                                     |
| Has a shell? | yes                                    | yes                                    |

Check the [tags history page](/chainguard/chainguard-images/reference/cassandra-medusa/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                               | latest-dev | latest |
|-------------------------------|------------|--------|
| `apk-tools`                   | X          |        |
| `bash`                        | X          | X      |
| `busybox`                     | X          | X      |
| `ca-certificates-bundle`      | X          | X      |
| `git`                         | X          |        |
| `glibc`                       | X          | X      |
| `glibc-locale-posix`          | X          | X      |
| `grpc-health-probe`           | X          | X      |
| `ld-linux`                    | X          | X      |
| `libbrotlicommon1`            | X          |        |
| `libbrotlidec1`               | X          |        |
| `libcrypt1`                   | X          | X      |
| `libcrypto3`                  | X          |        |
| `libcurl-openssl4`            | X          |        |
| `libexpat1`                   | X          |        |
| `libidn2`                     | X          |        |
| `libnghttp2-14`               | X          |        |
| `libpcre2-8-0`                | X          |        |
| `libpsl`                      | X          |        |
| `libssl3`                     | X          |        |
| `libunistring`                | X          |        |
| `ncurses`                     | X          | X      |
| `ncurses-terminfo-base`       | X          | X      |
| `openssl-config`              | X          |        |
| `py3-cassandra-medusa`        | X          | X      |
| `py3-cassandra-medusa-compat` | X          | X      |
| `wget`                        | X          |        |
| `wolfi-baselayout`            | X          | X      |
| `zlib`                        | X          |        |

