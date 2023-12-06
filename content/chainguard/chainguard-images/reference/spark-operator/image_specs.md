---
title: "spark-operator Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public spark-operator Chainguard Image variants"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/spark-operator/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/spark-operator/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/spark-operator/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/spark-operator/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **spark-operator** Image.

## Variants Compared
The **spark-operator** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev               | latest                   |
|--------------|--------------------------|--------------------------|
| Default User | `nonroot`                | `nonroot`                |
| Entrypoint   | `/usr/bin/entrypoint.sh` | `/usr/bin/entrypoint.sh` |
| CMD          | not specified            | not specified            |
| Workdir      | not specified            | not specified            |
| Has apk?     | yes                      | no                       |
| Has a shell? | yes                      | yes                      |

Check the [tags history page](/chainguard/chainguard-images/reference/spark-operator/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                 | latest-dev | latest |
|---------------------------------|------------|--------|
| `apk-tools`                     | X          |        |
| `bash`                          | X          | X      |
| `busybox`                       | X          |        |
| `ca-certificates-bundle`        | X          | X      |
| `coreutils`                     | X          | X      |
| `git`                           | X          |        |
| `glibc`                         | X          | X      |
| `glibc-locale-posix`            | X          | X      |
| `ld-linux`                      | X          | X      |
| `libacl1`                       | X          | X      |
| `libattr1`                      | X          | X      |
| `libbrotlicommon1`              | X          |        |
| `libbrotlidec1`                 | X          |        |
| `libcrypt1`                     | X          |        |
| `libcrypto3`                    | X          | X      |
| `libcurl-openssl4`              | X          |        |
| `libexpat1`                     | X          |        |
| `libnghttp2-14`                 | X          |        |
| `libpcre2-8-0`                  | X          |        |
| `libssl3`                       | X          | X      |
| `ncurses`                       | X          | X      |
| `ncurses-terminfo-base`         | X          | X      |
| `openssl`                       | X          | X      |
| `openssl-config`                | X          | X      |
| `openssl-provider-legacy`       | X          | X      |
| `posix-libc-utils`              | X          | X      |
| `spark-operator`                | X          | X      |
| `spark-operator-oci-entrypoint` | X          | X      |
| `tini`                          | X          | X      |
| `wolfi-baselayout`              | X          | X      |
| `zlib`                          | X          |        |

