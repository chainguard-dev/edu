---
title: "proxysql Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public proxysql Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-03-01 12:14:22
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/proxysql/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/proxysql/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/proxysql/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/proxysql/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **proxysql** Image.

|              | latest-dev                                         | latest                                             |
|--------------|----------------------------------------------------|----------------------------------------------------|
| Default User | `root`                                             | `root`                                             |
| Entrypoint   | `/usr/bin/proxysql`                                | `/usr/bin/proxysql`                                |
| CMD          | `--initial --idle-threads -f -c /etc/proxysql.cnf` | `--initial --idle-threads -f -c /etc/proxysql.cnf` |
| Workdir      | not specified                                      | not specified                                      |
| Has apk?     | yes                                                | no                                                 |
| Has a shell? | yes                                                | no                                                 |

Check the [tags history page](/chainguard/chainguard-images/reference/proxysql/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          |        |
| `busybox`                | X          |        |
| `ca-certificates-bundle` | X          | X      |
| `chainguard-baselayout`  | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `gmp`                    | X          | X      |
| `gmp-dev`                | X          | X      |
| `gnutls`                 | X          | X      |
| `ld-linux`               | X          | X      |
| `libbrotlicommon1`       | X          |        |
| `libbrotlidec1`          | X          |        |
| `libcrypt1`              | X          |        |
| `libcrypto3`             | X          |        |
| `libcurl-openssl4`       | X          |        |
| `libexpat1`              | X          |        |
| `libffi`                 | X          | X      |
| `libgcc`                 | X          | X      |
| `libidn2`                | X          |        |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libpsl`                 | X          |        |
| `libssl3`                | X          |        |
| `libstdc++`              | X          | X      |
| `libtasn1`               | X          | X      |
| `libunistring`           | X          | X      |
| `libuuid`                | X          | X      |
| `ncurses`                | X          |        |
| `ncurses-terminfo-base`  | X          |        |
| `nettle`                 | X          | X      |
| `openssl-config`         | X          |        |
| `p11-kit`                | X          | X      |
| `proxysql`               | X          | X      |
| `wget`                   | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `zlib`                   | X          | X      |

