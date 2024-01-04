---
title: "kubernetes-csi-livenessprobe Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public kubernetes-csi-livenessprobe Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-01-03 00:37:41
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kubernetes-csi-livenessprobe/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/kubernetes-csi-livenessprobe/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kubernetes-csi-livenessprobe/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubernetes-csi-livenessprobe/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **kubernetes-csi-livenessprobe** Image.

## Variants Compared
The **kubernetes-csi-livenessprobe** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev               | latest                   |
|--------------|--------------------------|--------------------------|
| Default User | `nonroot`                | `nonroot`                |
| Entrypoint   | `/usr/bin/livenessprobe` | `/usr/bin/livenessprobe` |
| CMD          | not specified            | not specified            |
| Workdir      | not specified            | not specified            |
| Has apk?     | yes                      | no                       |
| Has a shell? | yes                      | no                       |

Check the [tags history page](/chainguard/chainguard-images/reference/kubernetes-csi-livenessprobe/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                | latest-dev | latest |
|--------------------------------|------------|--------|
| `apk-tools`                    | X          |        |
| `bash`                         | X          |        |
| `busybox`                      | X          |        |
| `ca-certificates-bundle`       | X          | X      |
| `git`                          | X          |        |
| `glibc`                        | X          | X      |
| `glibc-locale-posix`           | X          | X      |
| `kubernetes-csi-livenessprobe` | X          | X      |
| `ld-linux`                     | X          | X      |
| `libbrotlicommon1`             | X          |        |
| `libbrotlidec1`                | X          |        |
| `libcrypt1`                    | X          |        |
| `libcrypto3`                   | X          |        |
| `libcurl-openssl4`             | X          |        |
| `libexpat1`                    | X          |        |
| `libnghttp2-14`                | X          |        |
| `libpcre2-8-0`                 | X          |        |
| `libssl3`                      | X          |        |
| `ncurses`                      | X          |        |
| `ncurses-terminfo-base`        | X          |        |
| `openssl-config`               | X          |        |
| `wolfi-baselayout`             | X          | X      |
| `zlib`                         | X          |        |

