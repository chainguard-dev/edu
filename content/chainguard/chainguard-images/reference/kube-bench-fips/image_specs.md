---
title: "kube-bench-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public kube-bench-fips Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-06-11 00:42:18
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kube-bench-fips/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/kube-bench-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kube-bench-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kube-bench-fips/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **kube-bench-fips** Image.

|              | latest-dev            | latest                |
|--------------|-----------------------|-----------------------|
| Default User | `root`                | `root`                |
| Entrypoint   | `/usr/bin/kube-bench` | `/usr/bin/kube-bench` |
| CMD          | `help`                | `help`                |
| Workdir      | `/etc/kube-bench`     | `/etc/kube-bench`     |
| Has apk?     | yes                   | no                    |
| Has a shell? | yes                   | no                    |

Check the [tags history page](/chainguard/chainguard-images/reference/kube-bench-fips/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                               | latest-dev | latest |
|-------------------------------|------------|--------|
| `apk-tools`                   | X          |        |
| `bash`                        | X          |        |
| `busybox`                     | X          |        |
| `ca-certificates-bundle`      | X          | X      |
| `chainguard-baselayout`       | X          | X      |
| `git`                         | X          |        |
| `glibc`                       | X          | X      |
| `glibc-locale-posix`          | X          | X      |
| `kube-bench-configs`          | X          | X      |
| `kube-bench-fips`             | X          | X      |
| `kubectl-fips-1.30`           | X          | X      |
| `ld-linux`                    | X          | X      |
| `libbrotlicommon1`            | X          |        |
| `libbrotlidec1`               | X          |        |
| `libcrypt1`                   | X          |        |
| `libcrypto3`                  | X          | X      |
| `libcurl-openssl4`            | X          |        |
| `libexpat1`                   | X          |        |
| `libidn2`                     | X          |        |
| `libnghttp2-14`               | X          |        |
| `libpcre2-8-0`                | X          |        |
| `libproc-2-0`                 | X          | X      |
| `libpsl`                      | X          |        |
| `libssl3`                     | X          | X      |
| `libunistring`                | X          |        |
| `libxcrypt`                   | X          |        |
| `ncurses`                     | X          | X      |
| `ncurses-terminfo-base`       | X          | X      |
| `openssl-config-fipshardened` | X          | X      |
| `openssl-provider-fips`       | X          | X      |
| `procps`                      | X          | X      |
| `wget`                        | X          |        |
| `wolfi-baselayout`            | X          | X      |
| `zlib`                        | X          |        |

