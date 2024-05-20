---
title: "apache-nifi Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public apache-nifi Chainguard Image."
date: 2024-05-20 00:48:18
lastmod: 2024-05-20 00:48:18
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/apache-nifi/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/apache-nifi/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/apache-nifi/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/apache-nifi/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **apache-nifi** Image.

|              | latest-dev                     | latest                         |
|--------------|--------------------------------|--------------------------------|
| Default User | `nonroot`                      | `nonroot`                      |
| Entrypoint   | `../scripts/start.sh`          | `../scripts/start.sh`          |
| CMD          | not specified                  | not specified                  |
| Workdir      | `/usr/share/nifi/nifi-current` | `/usr/share/nifi/nifi-current` |
| Has apk?     | yes                            | no                             |
| Has a shell? | yes                            | yes                            |

Check the [tags history page](/chainguard/chainguard-images/reference/apache-nifi/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apache-nifi`            | X          | X      |
| `apache-nifi-compat`     | X          | X      |
| `apache-nifi-toolkit`    | X          | X      |
| `apk-tools`              | X          |        |
| `bash`                   | X          | X      |
| `busybox`                | X          | X      |
| `ca-certificates`        | X          | X      |
| `ca-certificates-bundle` | X          | X      |
| `chainguard-baselayout`  | X          | X      |
| `coreutils`              | X          | X      |
| `fontconfig-config`      | X          | X      |
| `freetype`               | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-en`        | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `java-cacerts`           | X          | X      |
| `java-common`            | X          | X      |
| `ld-linux`               | X          | X      |
| `libacl1`                | X          | X      |
| `libattr1`               | X          | X      |
| `libbrotlicommon1`       | X          | X      |
| `libbrotlidec1`          | X          | X      |
| `libbz2-1`               | X          | X      |
| `libcrypt1`              | X          | X      |
| `libcrypto3`             | X          | X      |
| `libcurl-openssl4`       | X          |        |
| `libexpat1`              | X          | X      |
| `libffi`                 | X          | X      |
| `libfontconfig1`         | X          | X      |
| `libgcrypt`              | X          | X      |
| `libgpg-error`           | X          | X      |
| `libidn2`                | X          |        |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libpng`                 | X          | X      |
| `libpsl`                 | X          |        |
| `libssl3`                | X          |        |
| `libtasn1`               | X          | X      |
| `libunistring`           | X          |        |
| `libxcrypt`              | X          | X      |
| `libxml2`                | X          | X      |
| `libxslt`                | X          | X      |
| `ncurses`                | X          | X      |
| `ncurses-terminfo-base`  | X          | X      |
| `openjdk-11-default-jvm` | X          | X      |
| `openjdk-11-jre`         | X          | X      |
| `openjdk-11-jre-base`    | X          | X      |
| `p11-kit`                | X          | X      |
| `p11-kit-trust`          | X          | X      |
| `wget`                   | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `xmlstarlet`             | X          | X      |
| `xz`                     | X          | X      |
| `zlib`                   | X          | X      |

