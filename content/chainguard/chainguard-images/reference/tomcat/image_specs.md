---
title: "tomcat Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public tomcat Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/tomcat/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/tomcat/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/tomcat/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/tomcat/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **tomcat** Image.

## Variants Compared
The **tomcat** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                              |
|--------------|-------------------------------------|
| Default User | `nonroot`                           |
| Entrypoint   | `/usr/local/tomcat/bin/catalina.sh` |
| CMD          | `run`                               |
| Workdir      | `/usr/local/tomcat`                 |
| Has apk?     | no                                  |
| Has a shell? | yes                                 |

Check the [tags history page](/chainguard/chainguard-images/reference/tomcat/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest |
|--------------------------|--------|
| `bash`                   | X      |
| `busybox`                | X      |
| `ca-certificates`        | X      |
| `ca-certificates-bundle` | X      |
| `fontconfig-config`      | X      |
| `freetype`               | X      |
| `glibc`                  | X      |
| `glibc-locale-posix`     | X      |
| `java-cacerts`           | X      |
| `java-common`            | X      |
| `ld-linux`               | X      |
| `libapr`                 | X      |
| `libbrotlicommon1`       | X      |
| `libbrotlidec1`          | X      |
| `libbz2-1`               | X      |
| `libcrypt1`              | X      |
| `libcrypto3`             | X      |
| `libexpat1`              | X      |
| `libffi`                 | X      |
| `libfontconfig1`         | X      |
| `libpng`                 | X      |
| `libssl3`                | X      |
| `libtasn1`               | X      |
| `ncurses`                | X      |
| `ncurses-terminfo-base`  | X      |
| `openjdk-17`             | X      |
| `openjdk-17-default-jvm` | X      |
| `openjdk-17-jre`         | X      |
| `openjdk-17-jre-base`    | X      |
| `openssl-config`         | X      |
| `p11-kit`                | X      |
| `p11-kit-trust`          | X      |
| `tomcat-10`              | X      |
| `tomcat-native`          | X      |
| `wolfi-baselayout`       | X      |
| `zlib`                   | X      |

