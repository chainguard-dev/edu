---
title: "kubernetes-ingress-defaultbackend Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public kubernetes-ingress-defaultbackend Chainguard Image variants"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kubernetes-ingress-defaultbackend/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/kubernetes-ingress-defaultbackend/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kubernetes-ingress-defaultbackend/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubernetes-ingress-defaultbackend/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **kubernetes-ingress-defaultbackend** Image.

## Variants Compared
The **kubernetes-ingress-defaultbackend** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                | latest                    |
|--------------|---------------------------|---------------------------|
| Default User | `nonroot`                 | `nonroot`                 |
| Entrypoint   | `/usr/bin/defaultbackend` | `/usr/bin/defaultbackend` |
| CMD          | not specified             | not specified             |
| Workdir      | not specified             | not specified             |
| Has apk?     | yes                       | no                        |
| Has a shell? | yes                       | no                        |

Check the [tags history page](/chainguard/chainguard-images/reference/kubernetes-ingress-defaultbackend/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                     | latest-dev | latest |
|-------------------------------------|------------|--------|
| `apk-tools`                         | X          |        |
| `bash`                              | X          |        |
| `busybox`                           | X          |        |
| `ca-certificates-bundle`            | X          | X      |
| `git`                               | X          |        |
| `glibc`                             | X          |        |
| `glibc-locale-posix`                | X          |        |
| `kubernetes-ingress-defaultbackend` | X          | X      |
| `ld-linux`                          | X          |        |
| `libbrotlicommon1`                  | X          |        |
| `libbrotlidec1`                     | X          |        |
| `libcrypt1`                         | X          |        |
| `libcrypto3`                        | X          |        |
| `libcurl-openssl4`                  | X          |        |
| `libexpat1`                         | X          |        |
| `libnghttp2-14`                     | X          |        |
| `libpcre2-8-0`                      | X          |        |
| `libssl3`                           | X          |        |
| `ncurses`                           | X          |        |
| `ncurses-terminfo-base`             | X          |        |
| `openssl-config`                    | X          |        |
| `wolfi-baselayout`                  | X          | X      |
| `zlib`                              | X          |        |

