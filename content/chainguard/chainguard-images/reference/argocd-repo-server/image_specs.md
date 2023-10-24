---
title: "argocd-repo-server Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public argocd-repo-server Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/argocd-repo-server/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/argocd-repo-server/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/argocd-repo-server/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/argocd-repo-server/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **argocd-repo-server** Image.

## Variants Compared
The **argocd-repo-server** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev     | latest         |
|--------------|----------------|----------------|
| Default User | `argocd`       | `argocd`       |
| Entrypoint   | not specified  | not specified  |
| CMD          | not specified  | not specified  |
| Workdir      | `/home/argocd` | `/home/argocd` |
| Has apk?     | yes            | no             |
| Has a shell? | yes            | yes            |

Check the [tags history page](/chainguard/chainguard-images/reference/argocd-repo-server/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `argo-cd-2.8`            | X          | X      |
| `argo-cd-2.8-compat`     | X          | X      |
| `bash`                   | X          |        |
| `busybox`                | X          | X      |
| `ca-certificates-bundle` | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `ld-linux`               | X          | X      |
| `libbrotlicommon1`       | X          |        |
| `libbrotlidec1`          | X          |        |
| `libcrypt1`              | X          | X      |
| `libcrypto3`             | X          |        |
| `libcurl-openssl4`       | X          |        |
| `libexpat1`              | X          |        |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libssl3`                | X          |        |
| `ncurses`                | X          |        |
| `ncurses-terminfo-base`  | X          |        |
| `openssl-config`         | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `zlib`                   | X          |        |

