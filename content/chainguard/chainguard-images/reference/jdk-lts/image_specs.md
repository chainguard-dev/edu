---
title: "jdk-lts Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public jdk-lts Chainguard Image variants"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jdk-lts/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/jdk-lts/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/jdk-lts/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jdk-lts/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **jdk-lts** Image.

## Variants Compared
The **jdk-lts** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev    | latest        |
|--------------|---------------|---------------|
| Default User | `java`        | `java`        |
| Entrypoint   | not specified | not specified |
| CMD          | not specified | not specified |
| Workdir      | `/home/build` | `/home/build` |
| Has apk?     | yes           | no            |
| Has a shell? | yes           | yes           |

Check the [tags history page](/chainguard/chainguard-images/reference/jdk-lts/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          |        |
| `busybox`                | X          | X      |
| `ca-certificates`        | X          | X      |
| `ca-certificates-bundle` | X          | X      |
| `fontconfig-config`      | X          | X      |
| `freetype`               | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-en`        | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `java-cacerts`           | X          | X      |
| `java-common`            | X          | X      |
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
| `libgcc`                 | X          | X      |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libpng`                 | X          | X      |
| `libssl3`                | X          |        |
| `libstdc++`              | X          | X      |
| `libtasn1`               | X          | X      |
| `ncurses`                | X          |        |
| `ncurses-terminfo-base`  | X          |        |
| `openjdk-21`             | X          | X      |
| `openjdk-21-default-jdk` | X          | X      |
| `openjdk-21-default-jvm` | X          | X      |
| `openjdk-21-jre`         | X          | X      |
| `openjdk-21-jre-base`    | X          | X      |
| `openssl-config`         | X          | X      |
| `p11-kit`                | X          | X      |
| `p11-kit-trust`          | X          | X      |
| `wolfi-baselayout`       | X          | X      |
| `zlib`                   | X          | X      |

