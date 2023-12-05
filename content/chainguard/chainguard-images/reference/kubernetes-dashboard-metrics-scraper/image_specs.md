---
title: "kubernetes-dashboard-metrics-scraper Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public kubernetes-dashboard-metrics-scraper Chainguard Image variants"
date: 2023-12-05 00:31:58
lastmod: 2023-12-05 00:31:58
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kubernetes-dashboard-metrics-scraper/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/kubernetes-dashboard-metrics-scraper/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kubernetes-dashboard-metrics-scraper/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubernetes-dashboard-metrics-scraper/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **kubernetes-dashboard-metrics-scraper** Image.

## Variants Compared
The **kubernetes-dashboard-metrics-scraper** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                 | latest                     |
|--------------|----------------------------|----------------------------|
| Default User | `nonroot`                  | `nonroot`                  |
| Entrypoint   | `/usr/bin/metrics-sidecar` | `/usr/bin/metrics-sidecar` |
| CMD          | not specified              | not specified              |
| Workdir      | not specified              | not specified              |
| Has apk?     | yes                        | no                         |
| Has a shell? | yes                        | no                         |

Check the [tags history page](/chainguard/chainguard-images/reference/kubernetes-dashboard-metrics-scraper/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                        | latest-dev | latest |
|----------------------------------------|------------|--------|
| `apk-tools`                            | X          |        |
| `bash`                                 | X          |        |
| `busybox`                              | X          |        |
| `ca-certificates-bundle`               | X          | X      |
| `git`                                  | X          |        |
| `glibc`                                | X          |        |
| `glibc-locale-posix`                   | X          |        |
| `kubernetes-dashboard-metrics-scraper` | X          | X      |
| `ld-linux`                             | X          |        |
| `libbrotlicommon1`                     | X          |        |
| `libbrotlidec1`                        | X          |        |
| `libcrypt1`                            | X          |        |
| `libcrypto3`                           | X          |        |
| `libcurl-openssl4`                     | X          |        |
| `libexpat1`                            | X          |        |
| `libnghttp2-14`                        | X          |        |
| `libpcre2-8-0`                         | X          |        |
| `libssl3`                              | X          |        |
| `ncurses`                              | X          |        |
| `ncurses-terminfo-base`                | X          |        |
| `openssl-config`                       | X          |        |
| `wolfi-baselayout`                     | X          | X      |
| `zlib`                                 | X          |        |

