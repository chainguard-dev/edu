---
title: "argocd-extension-installer-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public argocd-extension-installer-fips Chainguard Image."
date: 2024-04-10 00:53:55
lastmod: 2024-04-10 00:53:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/argocd-extension-installer-fips/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/argocd-extension-installer-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/argocd-extension-installer-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/argocd-extension-installer-fips/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **argocd-extension-installer-fips** Image.

|              | latest-dev            | latest                |
|--------------|-----------------------|-----------------------|
| Default User | `ext-installer`       | `ext-installer`       |
| Entrypoint   | `./install.sh`        | `./install.sh`        |
| CMD          | not specified         | not specified         |
| Workdir      | `/home/ext-installer` | `/home/ext-installer` |
| Has apk?     | yes                   | no                    |
| Has a shell? | yes                   | yes                   |

Check the [tags history page](/chainguard/chainguard-images/reference/argocd-extension-installer-fips/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                               | latest-dev | latest |
|-------------------------------|------------|--------|
| `apk-tools`                   | X          |        |
| `argocd-extension-installer`  | X          | X      |
| `bash`                        | X          |        |
| `busybox`                     | X          | X      |
| `ca-certificates-bundle`      | X          | X      |
| `chainguard-baselayout`       | X          | X      |
| `curl`                        | X          | X      |
| `file`                        | X          | X      |
| `git`                         | X          |        |
| `glibc`                       | X          | X      |
| `glibc-locale-posix`          | X          | X      |
| `ld-linux`                    | X          | X      |
| `libbrotlicommon1`            | X          | X      |
| `libbrotlidec1`               | X          | X      |
| `libcrypt1`                   | X          | X      |
| `libcrypto3`                  | X          | X      |
| `libcurl-openssl4`            | X          | X      |
| `libexpat1`                   | X          |        |
| `libidn2`                     | X          | X      |
| `libmagic`                    | X          | X      |
| `libnghttp2-14`               | X          | X      |
| `libpcre2-8-0`                | X          |        |
| `libpsl`                      | X          | X      |
| `libssl3`                     | X          | X      |
| `libunistring`                | X          | X      |
| `libxcrypt`                   | X          | X      |
| `ncurses`                     | X          |        |
| `ncurses-terminfo-base`       | X          |        |
| `openssl-config-fipshardened` | X          | X      |
| `openssl-provider-fips`       | X          | X      |
| `wget`                        | X          |        |
| `wolfi-baselayout`            | X          | X      |
| `zlib`                        | X          | X      |

