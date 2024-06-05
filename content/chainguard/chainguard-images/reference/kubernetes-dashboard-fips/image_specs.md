---
title: "kubernetes-dashboard-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public kubernetes-dashboard-fips Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-06-05 00:36:13
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kubernetes-dashboard-fips/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/kubernetes-dashboard-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kubernetes-dashboard-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubernetes-dashboard-fips/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **kubernetes-dashboard-fips** Image.

|              | latest-dev                                                                                         | latest                     |
|--------------|----------------------------------------------------------------------------------------------------|----------------------------|
| Default User | `nonroot`                                                                                          | `nonroot`                  |
| Entrypoint   | `/usr/share/kubernetes-dashboard/dashboard --insecure-bind-address=0.0.0.0 --bind-address=0.0.0.0` | `/usr/bin/metrics-sidecar` |
| CMD          | not specified                                                                                      | not specified              |
| Workdir      | not specified                                                                                      | not specified              |
| Has apk?     | yes                                                                                                | no                         |
| Has a shell? | yes                                                                                                | no                         |

Check the [tags history page](/chainguard/chainguard-images/reference/kubernetes-dashboard-fips/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                             | latest-dev | latest |
|---------------------------------------------|------------|--------|
| `apk-tools`                                 | X          |        |
| `bash`                                      | X          |        |
| `busybox`                                   | X          |        |
| `ca-certificates-bundle`                    | X          | X      |
| `chainguard-baselayout`                     | X          | X      |
| `git`                                       | X          |        |
| `glibc`                                     | X          | X      |
| `glibc-locale-posix`                        | X          | X      |
| `kubernetes-dashboard-fips`                 | X          |        |
| `ld-linux`                                  | X          | X      |
| `libbrotlicommon1`                          | X          |        |
| `libbrotlidec1`                             | X          |        |
| `libcrypt1`                                 | X          |        |
| `libcrypto3`                                | X          | X      |
| `libcurl-openssl4`                          | X          |        |
| `libexpat1`                                 | X          |        |
| `libidn2`                                   | X          |        |
| `libnghttp2-14`                             | X          |        |
| `libpcre2-8-0`                              | X          |        |
| `libpsl`                                    | X          |        |
| `libssl3`                                   | X          | X      |
| `libunistring`                              | X          |        |
| `libxcrypt`                                 | X          |        |
| `ncurses`                                   | X          |        |
| `ncurses-terminfo-base`                     | X          |        |
| `openssl-config-fipshardened`               | X          | X      |
| `openssl-provider-fips`                     | X          | X      |
| `wget`                                      | X          |        |
| `wolfi-baselayout`                          | X          | X      |
| `zlib`                                      | X          |        |
| `kubernetes-dashboard-metrics-scraper-fips` |            | X      |

