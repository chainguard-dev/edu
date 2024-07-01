---
title: "sonarqube Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public sonarqube Chainguard Image."
date: 2024-07-01 00:36:20
lastmod: 2024-07-01 00:36:20
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/sonarqube/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/sonarqube/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/sonarqube/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/sonarqube/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **sonarqube** Image.

|              | latest-dev                               | latest                                   |
|--------------|------------------------------------------|------------------------------------------|
| Default User | `sonarqube`                              | `sonarqube`                              |
| Entrypoint   | `bash`                                   | `bash`                                   |
| CMD          | `-c /opt/sonarqube/docker/entrypoint.sh` | `-c /opt/sonarqube/docker/entrypoint.sh` |
| Workdir      | `/opt/sonarqube`                         | `/opt/sonarqube`                         |
| Has apk?     | yes                                      | no                                       |
| Has a shell? | yes                                      | yes                                      |

Check the [tags history page](/chainguard/chainguard-images/reference/sonarqube/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                           | latest-dev | latest |
|---------------------------|------------|--------|
| `apk-tools`               | X          |        |
| `bash`                    | X          | X      |
| `bash-binsh`              | X          | X      |
| `busybox`                 | X          |        |
| `ca-certificates`         | X          | X      |
| `ca-certificates-bundle`  | X          | X      |
| `chainguard-baselayout`   | X          | X      |
| `fontconfig-config`       | X          | X      |
| `freetype`                | X          | X      |
| `git`                     | X          |        |
| `glibc`                   | X          | X      |
| `glibc-locale-posix`      | X          | X      |
| `grep`                    | X          | X      |
| `java-cacerts`            | X          | X      |
| `java-common`             | X          | X      |
| `ld-linux`                | X          | X      |
| `libbrotlicommon1`        | X          | X      |
| `libbrotlidec1`           | X          | X      |
| `libbz2-1`                | X          | X      |
| `libcrypt1`               | X          |        |
| `libcrypto3`              | X          | X      |
| `libcurl-openssl4`        | X          |        |
| `libexpat1`               | X          | X      |
| `libffi`                  | X          | X      |
| `libfontconfig1`          | X          | X      |
| `libidn2`                 | X          |        |
| `libnghttp2-14`           | X          |        |
| `libpcre2-8-0`            | X          | X      |
| `libpng`                  | X          | X      |
| `libproc-2-0`             | X          | X      |
| `libpsl`                  | X          |        |
| `libssl3`                 | X          | X      |
| `libtasn1`                | X          | X      |
| `libunistring`            | X          |        |
| `libxcrypt`               | X          |        |
| `ncurses`                 | X          | X      |
| `ncurses-terminfo-base`   | X          | X      |
| `openjdk-17-default-jvm`  | X          | X      |
| `openjdk-17-jre`          | X          | X      |
| `openjdk-17-jre-base`     | X          | X      |
| `p11-kit`                 | X          | X      |
| `p11-kit-trust`           | X          | X      |
| `procps`                  | X          | X      |
| `sonarqube`               | X          | X      |
| `sonarqube-docker-compat` | X          | X      |
| `wget`                    | X          | X      |
| `wolfi-baselayout`        | X          | X      |
| `zlib`                    | X          | X      |

