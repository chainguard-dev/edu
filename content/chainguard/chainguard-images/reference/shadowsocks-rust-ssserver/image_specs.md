---
title: "shadowsocks-rust-ssserver Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public shadowsocks-rust-ssserver Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-03-30 00:51:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/shadowsocks-rust-ssserver/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/shadowsocks-rust-ssserver/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/shadowsocks-rust-ssserver/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/shadowsocks-rust-ssserver/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **shadowsocks-rust-ssserver** Image.

|              | latest-dev                                                                   | latest                                                                       |
|--------------|------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| Default User | `root`                                                                       | `root`                                                                       |
| Entrypoint   | `/usr/bin/docker-entrypoint.sh`                                              | `/usr/bin/docker-entrypoint.sh`                                              |
| CMD          | `ssserver --log-without-time -a nobody -c /etc/shadowsocks-rust/config.json` | `ssserver --log-without-time -a nobody -c /etc/shadowsocks-rust/config.json` |
| Workdir      | not specified                                                                | not specified                                                                |
| Has apk?     | yes                                                                          | no                                                                           |
| Has a shell? | yes                                                                          | yes                                                                          |

Check the [tags history page](/chainguard/chainguard-images/reference/shadowsocks-rust-ssserver/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                             | latest-dev | latest |
|-----------------------------|------------|--------|
| `apk-tools`                 | X          |        |
| `bash`                      | X          |        |
| `busybox`                   | X          | X      |
| `ca-certificates-bundle`    | X          | X      |
| `chainguard-baselayout`     | X          | X      |
| `git`                       | X          |        |
| `glibc`                     | X          | X      |
| `glibc-locale-posix`        | X          | X      |
| `ld-linux`                  | X          | X      |
| `libbrotlicommon1`          | X          |        |
| `libbrotlidec1`             | X          |        |
| `libcrypt1`                 | X          | X      |
| `libcrypto3`                | X          |        |
| `libcurl-openssl4`          | X          |        |
| `libexpat1`                 | X          |        |
| `libgcc`                    | X          | X      |
| `libidn2`                   | X          |        |
| `libnghttp2-14`             | X          |        |
| `libpcre2-8-0`              | X          |        |
| `libpsl`                    | X          |        |
| `libssl3`                   | X          |        |
| `libunistring`              | X          |        |
| `libxcrypt`                 | X          | X      |
| `ncurses`                   | X          |        |
| `ncurses-terminfo-base`     | X          |        |
| `openssl-config`            | X          |        |
| `shadowsocks-rust`          | X          | X      |
| `shadowsocks-rust-ssserver` | X          | X      |
| `wget`                      | X          |        |
| `wolfi-baselayout`          | X          | X      |
| `zlib`                      | X          |        |

