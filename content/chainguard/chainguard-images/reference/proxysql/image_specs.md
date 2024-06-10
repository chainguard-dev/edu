---
title: "proxysql Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public proxysql Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-06-10 00:50:47
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

|              | latest-dev                                         |
|--------------|----------------------------------------------------|
| Default User | `root`                                             |
| Entrypoint   | `/usr/bin/proxysql`                                |
| CMD          | `--initial --idle-threads -f -c /etc/proxysql.cnf` |
| Workdir      | not specified                                      |
| Has apk?     | yes                                                |
| Has a shell? | yes                                                |

Check the [tags history page](/chainguard/chainguard-images/reference/proxysql/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev |
|--------------------------|------------|
| `apk-tools`              | X          |
| `bash`                   | X          |
| `busybox`                | X          |
| `ca-certificates-bundle` | X          |
| `chainguard-baselayout`  | X          |
| `git`                    | X          |
| `glibc`                  | X          |
| `glibc-locale-posix`     | X          |
| `gmp`                    | X          |
| `gmp-dev`                | X          |
| `gnutls`                 | X          |
| `ld-linux`               | X          |
| `libbrotlicommon1`       | X          |
| `libbrotlidec1`          | X          |
| `libcrypt1`              | X          |
| `libcrypto3`             | X          |
| `libcurl-openssl4`       | X          |
| `libexpat1`              | X          |
| `libffi`                 | X          |
| `libgcc`                 | X          |
| `libidn2`                | X          |
| `libnghttp2-14`          | X          |
| `libpcre2-8-0`           | X          |
| `libpsl`                 | X          |
| `libssl3`                | X          |
| `libstdc++`              | X          |
| `libtasn1`               | X          |
| `libunistring`           | X          |
| `libuuid`                | X          |
| `libxcrypt`              | X          |
| `ncurses`                | X          |
| `ncurses-terminfo-base`  | X          |
| `nettle`                 | X          |
| `p11-kit`                | X          |
| `proxysql`               | X          |
| `wget`                   | X          |
| `wolfi-baselayout`       | X          |
| `zlib`                   | X          |

