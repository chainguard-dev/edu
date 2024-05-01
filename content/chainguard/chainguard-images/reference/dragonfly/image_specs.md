---
title: "dragonfly Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public dragonfly Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-05-01 00:46:56
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/dragonfly/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/dragonfly/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/dragonfly/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/dragonfly/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **dragonfly** Image.

|              | latest-dev                | latest                    |
|--------------|---------------------------|---------------------------|
| Default User | `dfly`                    | `dfly`                    |
| Entrypoint   | `/usr/bin/entrypoint.sh`  | `/usr/bin/entrypoint.sh`  |
| CMD          | `dragonfly --logtostderr` | `dragonfly --logtostderr` |
| Workdir      | not specified             | not specified             |
| Has apk?     | yes                       | no                        |
| Has a shell? | yes                       | yes                       |

Check the [tags history page](/chainguard/chainguard-images/reference/dragonfly/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                           | latest-dev | latest |
|---------------------------|------------|--------|
| `apk-tools`               | X          |        |
| `bash`                    | X          |        |
| `boost-context`           | X          | X      |
| `busybox`                 | X          | X      |
| `ca-certificates-bundle`  | X          | X      |
| `chainguard-baselayout`   | X          | X      |
| `dragonfly`               | X          | X      |
| `dragonfly-oci-compat`    | X          | X      |
| `git`                     | X          |        |
| `glibc`                   | X          | X      |
| `glibc-locale-posix`      | X          | X      |
| `ld-linux`                | X          | X      |
| `libbrotlicommon1`        | X          |        |
| `libbrotlidec1`           | X          |        |
| `libbsd`                  | X          | X      |
| `libcrypt1`               | X          | X      |
| `libcrypto3`              | X          | X      |
| `libcurl-openssl4`        | X          |        |
| `libexpat1`               | X          |        |
| `libgcc`                  | X          | X      |
| `libidn2`                 | X          |        |
| `libmd`                   | X          | X      |
| `libnghttp2-14`           | X          |        |
| `libpcre2-8-0`            | X          |        |
| `libpsl`                  | X          |        |
| `libssl3`                 | X          | X      |
| `libstdc++`               | X          | X      |
| `libunistring`            | X          |        |
| `libunwind`               | X          | X      |
| `libxcrypt`               | X          | X      |
| `libzstd1`                | X          | X      |
| `ncurses`                 | X          |        |
| `ncurses-terminfo-base`   | X          |        |
| `net-tools`               | X          | X      |
| `netcat-openbsd`          | X          | X      |
| `openssl`                 | X          | X      |
| `openssl-provider-legacy` | X          | X      |
| `redis-benchmark-7.2`     | X          | X      |
| `redis-cli-7.2`           | X          | X      |
| `su-exec`                 | X          | X      |
| `wget`                    | X          |        |
| `wolfi-baselayout`        | X          | X      |
| `xz`                      | X          | X      |
| `zlib`                    | X          | X      |

