---
title: "k8s-sidecar-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public k8s-sidecar-fips Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-03-08 00:56:03
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/k8s-sidecar-fips/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/k8s-sidecar-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/k8s-sidecar-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/k8s-sidecar-fips/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **k8s-sidecar-fips** Image.

|              | latest-dev                            | latest                                |
|--------------|---------------------------------------|---------------------------------------|
| Default User | `k8s-sidecar`                         | `k8s-sidecar`                         |
| Entrypoint   | `python -u /usr/share/app/sidecar.py` | `python -u /usr/share/app/sidecar.py` |
| CMD          | not specified                         | not specified                         |
| Workdir      | not specified                         | not specified                         |
| Has apk?     | yes                                   | no                                    |
| Has a shell? | yes                                   | no                                    |

Check the [tags history page](/chainguard/chainguard-images/reference/k8s-sidecar-fips/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                               | latest-dev | latest |
|-------------------------------|------------|--------|
| `apk-tools`                   | X          |        |
| `bash`                        | X          |        |
| `busybox`                     | X          |        |
| `ca-certificates-bundle`      | X          | X      |
| `chainguard-baselayout`       | X          | X      |
| `gdbm`                        | X          | X      |
| `git`                         | X          |        |
| `glibc`                       | X          | X      |
| `glibc-locale-posix`          | X          | X      |
| `k8s-sidecar`                 | X          | X      |
| `ld-linux`                    | X          | X      |
| `libbrotlicommon1`            | X          |        |
| `libbrotlidec1`               | X          |        |
| `libbz2-1`                    | X          | X      |
| `libcrypt1`                   | X          | X      |
| `libcrypto3`                  | X          | X      |
| `libcurl-openssl4`            | X          |        |
| `libexpat1`                   | X          | X      |
| `libffi`                      | X          | X      |
| `libgcc`                      | X          | X      |
| `libidn2`                     | X          |        |
| `libnghttp2-14`               | X          |        |
| `libpcre2-8-0`                | X          |        |
| `libpsl`                      | X          |        |
| `libssl3`                     | X          | X      |
| `libstdc++`                   | X          | X      |
| `libunistring`                | X          |        |
| `mpdecimal`                   | X          | X      |
| `ncurses`                     | X          | X      |
| `ncurses-terminfo-base`       | X          | X      |
| `openssl-config-fipshardened` | X          | X      |
| `openssl-provider-fips`       | X          | X      |
| `python-3.12`                 | X          | X      |
| `python-3.12-default`         | X          | X      |
| `readline`                    | X          | X      |
| `sqlite-libs`                 | X          | X      |
| `wget`                        | X          |        |
| `wolfi-baselayout`            | X          | X      |
| `xz`                          | X          | X      |
| `zlib`                        | X          | X      |

