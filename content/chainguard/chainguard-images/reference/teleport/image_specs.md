---
title: "teleport Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public teleport Chainguard Image."
date: 2024-06-10 00:50:47
lastmod: 2024-06-10 00:50:47
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/teleport/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/teleport/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/teleport/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/teleport/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **teleport** Image.

|              | latest-dev                                                                        | latest                                                                            |
|--------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| Default User | `root`                                                                            | `root`                                                                            |
| Entrypoint   | `/usr/bin/dumb-init /usr/local/bin/teleport start -c /etc/teleport/teleport.yaml` | `/usr/bin/dumb-init /usr/local/bin/teleport start -c /etc/teleport/teleport.yaml` |
| CMD          | not specified                                                                     | not specified                                                                     |
| Workdir      | not specified                                                                     | not specified                                                                     |
| Has apk?     | yes                                                                               | no                                                                                |
| Has a shell? | yes                                                                               | yes                                                                               |

Check the [tags history page](/chainguard/chainguard-images/reference/teleport/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `audit`                  | X          | X      |
| `bash`                   | X          | X      |
| `busybox`                | X          |        |
| `ca-certificates-bundle` | X          | X      |
| `chainguard-baselayout`  | X          | X      |
| `dumb-init`              | X          | X      |
| `gdbm`                   | X          | X      |
| `gettext`                | X          | X      |
| `gettext-dev`            | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-iconv`            | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `ld-linux`               | X          | X      |
| `libbrotlicommon1`       | X          |        |
| `libbrotlidec1`          | X          |        |
| `libbz2-1`               | X          | X      |
| `libcap-ng`              | X          | X      |
| `libcrypt1`              | X          | X      |
| `libcrypto3`             | X          | X      |
| `libcurl-openssl4`       | X          |        |
| `libexpat1`              | X          | X      |
| `libffi`                 | X          | X      |
| `libgcc`                 | X          | X      |
| `libgomp`                | X          | X      |
| `libidn2`                | X          |        |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libpsl`                 | X          |        |
| `libssl3`                | X          | X      |
| `libstdc++`              | X          | X      |
| `libunistring`           | X          | X      |
| `libxcrypt`              | X          | X      |
| `libxml2`                | X          | X      |
| `linux-pam`              | X          | X      |
| `linux-pam-dev`          | X          | X      |
| `mpdecimal`              | X          | X      |
| `ncurses`                | X          | X      |
| `ncurses-terminfo-base`  | X          | X      |
| `net-tools`              | X          | X      |
| `posix-libc-utils`       | X          | X      |
| `python-3.12-base`       | X          | X      |
| `readline`               | X          | X      |
| `sqlite-libs`            | X          | X      |
| `teleport`               | X          | X      |
| `wget`                   | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `xz`                     | X          | X      |
| `zlib`                   | X          | X      |

