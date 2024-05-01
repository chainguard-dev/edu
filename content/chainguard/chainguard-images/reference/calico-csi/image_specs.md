---
title: "calico-csi Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public calico-csi Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-05-01 00:46:56
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/calico-csi/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/calico-csi/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/calico-csi/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/calico-csi/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **calico-csi** Image.

|              | latest-dev                             | latest                                 |
|--------------|----------------------------------------|----------------------------------------|
| Default User | `root`                                 | `root`                                 |
| Entrypoint   | `/usr/bin/calico-pod2daemon-csidriver` | `/usr/bin/calico-pod2daemon-csidriver` |
| CMD          | not specified                          | not specified                          |
| Workdir      | not specified                          | not specified                          |
| Has apk?     | yes                                    | no                                     |
| Has a shell? | yes                                    | no                                     |

Check the [tags history page](/chainguard/chainguard-images/reference/calico-csi/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          |        |
| `busybox`                | X          |        |
| `ca-certificates-bundle` | X          | X      |
| `calico-pod2daemon`      | X          | X      |
| `chainguard-baselayout`  | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `ld-linux`               | X          | X      |
| `libbrotlicommon1`       | X          |        |
| `libbrotlidec1`          | X          |        |
| `libcrypt1`              | X          |        |
| `libcrypto3`             | X          |        |
| `libcurl-openssl4`       | X          |        |
| `libexpat1`              | X          |        |
| `libidn2`                | X          |        |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libpsl`                 | X          |        |
| `libssl3`                | X          |        |
| `libunistring`           | X          |        |
| `libxcrypt`              | X          |        |
| `ncurses`                | X          |        |
| `ncurses-terminfo-base`  | X          |        |
| `wget`                   | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `zlib`                   | X          |        |

