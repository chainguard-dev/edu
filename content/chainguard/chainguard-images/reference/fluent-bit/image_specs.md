---
title: "fluent-bit Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public fluent-bit Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/fluent-bit/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/fluent-bit/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/fluent-bit/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/fluent-bit/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **fluent-bit** Image.

## Variants Compared
The **fluent-bit** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                                 | latest                                     |
|--------------|--------------------------------------------|--------------------------------------------|
| Default User | `root`                                     | `root`                                     |
| Entrypoint   | `/usr/bin/fluent-bit`                      | `/usr/bin/fluent-bit`                      |
| CMD          | `--config=/fluent-bit/etc/fluent-bit.conf` | `--config=/fluent-bit/etc/fluent-bit.conf` |
| Workdir      | not specified                              | not specified                              |
| Has apk?     | yes                                        | no                                         |
| Has a shell? | yes                                        | no                                         |

Check the [tags history page](/chainguard/chainguard-images/reference/fluent-bit/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          |        |
| `busybox`                | X          |        |
| `ca-certificates-bundle` | X          | X      |
| `fluent-bit`             | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `ld-linux`               | X          | X      |
| `libbrotlicommon1`       | X          |        |
| `libbrotlidec1`          | X          |        |
| `libcap`                 | X          | X      |
| `libcrypt1`              | X          |        |
| `libcrypto3`             | X          | X      |
| `libcurl-openssl4`       | X          |        |
| `libexpat1`              | X          |        |
| `libgcc`                 | X          | X      |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libpq-11`               | X          | X      |
| `libssl3`                | X          | X      |
| `libsystemd`             | X          | X      |
| `ncurses`                | X          |        |
| `ncurses-terminfo-base`  | X          |        |
| `openssl-config`         | X          | X      |
| `wolfi-baselayout`       | X          | X      |
| `yaml`                   | X          | X      |
| `zlib`                   | X          | X      |

