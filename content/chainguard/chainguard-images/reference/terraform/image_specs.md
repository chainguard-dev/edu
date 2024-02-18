---
title: "terraform Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public terraform Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-02-18 00:27:40
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/terraform/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/terraform/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/terraform/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/terraform/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **terraform** Image.

## Variants Compared
The **terraform** Chainguard Image currently has 4 public variants: 

- `latest-dev`
- `latest-mpl-dev`
- `latest-mpl`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev           | latest-mpl-dev       | latest-mpl           | latest               |
|--------------|----------------------|----------------------|----------------------|----------------------|
| Default User | `nonroot`            | `nonroot`            | `nonroot`            | `nonroot`            |
| Entrypoint   | `/usr/bin/terraform` | `/usr/bin/terraform` | `/usr/bin/terraform` | `/usr/bin/terraform` |
| CMD          | `--help`             | `--help`             | `--help`             | `--help`             |
| Workdir      | not specified        | not specified        | not specified        | not specified        |
| Has apk?     | yes                  | yes                  | no                   | no                   |
| Has a shell? | yes                  | yes                  | no                   | no                   |

Check the [tags history page](/chainguard/chainguard-images/reference/terraform/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest-mpl-dev | latest-mpl | latest |
|--------------------------|------------|----------------|------------|--------|
| `apk-tools`              | X          | X              |            |        |
| `bash`                   | X          | X              |            |        |
| `busybox`                | X          | X              |            |        |
| `ca-certificates-bundle` | X          | X              | X          | X      |
| `git`                    | X          | X              |            |        |
| `glibc`                  | X          | X              |            |        |
| `glibc-locale-posix`     | X          | X              |            |        |
| `ld-linux`               | X          | X              |            | X      |
| `libbrotlicommon1`       | X          | X              |            |        |
| `libbrotlidec1`          | X          | X              |            |        |
| `libcrypt1`              | X          | X              |            |        |
| `libcrypto3`             | X          | X              |            |        |
| `libcurl-openssl4`       | X          | X              |            |        |
| `libexpat1`              | X          | X              |            |        |
| `libidn2`                | X          | X              |            |        |
| `libnghttp2-14`          | X          | X              |            |        |
| `libpcre2-8-0`           | X          | X              |            |        |
| `libpsl`                 | X          | X              |            |        |
| `libssl3`                | X          | X              |            |        |
| `libunistring`           | X          | X              |            |        |
| `ncurses`                | X          | X              |            |        |
| `ncurses-terminfo-base`  | X          | X              |            |        |
| `openssl-config`         | X          | X              |            |        |
| `terraform-1.7`          | X          |                |            | X      |
| `wget`                   | X          | X              |            |        |
| `wolfi-baselayout`       | X          | X              | X          | X      |
| `zlib`                   | X          | X              |            |        |
| `terraform`              |            | X              | X          |        |

