---
title: "prometheus-elasticsearch-exporter Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public prometheus-elasticsearch-exporter Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/prometheus-elasticsearch-exporter/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/prometheus-elasticsearch-exporter/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/prometheus-elasticsearch-exporter/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/prometheus-elasticsearch-exporter/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **prometheus-elasticsearch-exporter** Image.

## Variants Compared
The **prometheus-elasticsearch-exporter** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                        | latest                            |
|--------------|-----------------------------------|-----------------------------------|
| Default User | `elasticsearch_exporter`          | `elasticsearch_exporter`          |
| Entrypoint   | `/usr/bin/elasticsearch_exporter` | `/usr/bin/elasticsearch_exporter` |
| CMD          | not specified                     | not specified                     |
| Workdir      | not specified                     | not specified                     |
| Has apk?     | yes                               | no                                |
| Has a shell? | yes                               | yes                               |

Check the [tags history page](/chainguard/chainguard-images/reference/prometheus-elasticsearch-exporter/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                     | latest-dev | latest |
|-------------------------------------|------------|--------|
| `apk-tools`                         | X          |        |
| `bash`                              | X          |        |
| `busybox`                           | X          | X      |
| `ca-certificates-bundle`            | X          | X      |
| `git`                               | X          |        |
| `glibc`                             | X          | X      |
| `glibc-locale-posix`                | X          | X      |
| `ld-linux`                          | X          | X      |
| `libbrotlicommon1`                  | X          |        |
| `libbrotlidec1`                     | X          |        |
| `libcrypt1`                         | X          | X      |
| `libcrypto3`                        | X          |        |
| `libcurl-rustls4`                   | X          |        |
| `libexpat1`                         | X          |        |
| `libgcc`                            | X          |        |
| `libnghttp2-14`                     | X          |        |
| `libpcre2-8-0`                      | X          |        |
| `libssl3`                           | X          |        |
| `ncurses`                           | X          |        |
| `ncurses-terminfo-base`             | X          |        |
| `openssl-config`                    | X          |        |
| `prometheus-elasticsearch-exporter` | X          | X      |
| `wolfi-baselayout`                  | X          | X      |
| `zlib`                              | X          |        |

