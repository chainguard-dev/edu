---
title: "grafana Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public grafana Chainguard Image variants"
date: 2023-12-15 00:37:05
lastmod: 2023-12-15 00:37:05
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/grafana/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/grafana/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/grafana/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/grafana/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **grafana** Image.

## Variants Compared
The **grafana** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev            | latest                |
|--------------|-----------------------|-----------------------|
| Default User | `grafana`             | `grafana`             |
| Entrypoint   | `/opt/grafana/run.sh` | `/opt/grafana/run.sh` |
| CMD          | not specified         | not specified         |
| Workdir      | `/usr/share/grafana`  | `/usr/share/grafana`  |
| Has apk?     | yes                   | no                    |
| Has a shell? | yes                   | yes                   |

Check the [tags history page](/chainguard/chainguard-images/reference/grafana/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          | X      |
| `busybox`                | X          | X      |
| `ca-certificates-bundle` | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `grafana`                | X          | X      |
| `grafana-oci-compat`     | X          | X      |
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
| `ncurses`                | X          | X      |
| `ncurses-terminfo-base`  | X          | X      |
| `openssl-config`         | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `zlib`                   | X          |        |

