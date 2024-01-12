---
title: "kafka Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public kafka Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-01-12 00:39:30
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/kafka/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/kafka/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kafka/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kafka/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **kafka** Image.

## Variants Compared
The **kafka** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                                                                   | latest                                                                       |
|--------------|------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| Default User | `kafka`                                                                      | `kafka`                                                                      |
| Entrypoint   | `/opt/bitnami/scripts/kafka/entrypoint.sh /opt/bitnami/scripts/kafka/run.sh` | `/opt/bitnami/scripts/kafka/entrypoint.sh /opt/bitnami/scripts/kafka/run.sh` |
| CMD          | not specified                                                                | not specified                                                                |
| Workdir      | not specified                                                                | not specified                                                                |
| Has apk?     | yes                                                                          | no                                                                           |
| Has a shell? | yes                                                                          | yes                                                                          |

Check the [tags history page](/chainguard/chainguard-images/reference/kafka/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          | X      |
| `busybox`                | X          | X      |
| `ca-certificates`        | X          | X      |
| `ca-certificates-bundle` | X          | X      |
| `fontconfig-config`      | X          | X      |
| `freetype`               | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `java-cacerts`           | X          | X      |
| `java-common`            | X          | X      |
| `kafka`                  | X          | X      |
| `kafka-bitnami-compat`   | X          | X      |
| `ld-linux`               | X          | X      |
| `libbrotlicommon1`       | X          | X      |
| `libbrotlidec1`          | X          | X      |
| `libbz2-1`               | X          | X      |
| `libcrypt1`              | X          | X      |
| `libcrypto3`             | X          | X      |
| `libcurl-openssl4`       | X          |        |
| `libexpat1`              | X          | X      |
| `libffi`                 | X          | X      |
| `libfontconfig1`         | X          | X      |
| `libidn2`                | X          |        |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libpng`                 | X          | X      |
| `libpsl`                 | X          |        |
| `libssl3`                | X          |        |
| `libtasn1`               | X          | X      |
| `libunistring`           | X          |        |
| `ncurses`                | X          | X      |
| `ncurses-terminfo-base`  | X          | X      |
| `openjdk-11-default-jvm` | X          | X      |
| `openjdk-11-jre`         | X          | X      |
| `openjdk-11-jre-base`    | X          | X      |
| `openssl-config`         | X          | X      |
| `p11-kit`                | X          | X      |
| `p11-kit-trust`          | X          | X      |
| `wolfi-baselayout`       | X          | X      |
| `zlib`                   | X          | X      |

