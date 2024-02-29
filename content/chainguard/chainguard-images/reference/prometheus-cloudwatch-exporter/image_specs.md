---
title: "prometheus-cloudwatch-exporter Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public prometheus-cloudwatch-exporter Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-02-29 16:25:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/prometheus-cloudwatch-exporter/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/prometheus-cloudwatch-exporter/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/prometheus-cloudwatch-exporter/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/prometheus-cloudwatch-exporter/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **prometheus-cloudwatch-exporter** Image.

|              | latest-dev                                                                            | latest                                                                                |
|--------------|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| Default User | `nonroot`                                                                             | `nonroot`                                                                             |
| Entrypoint   | `/usr/bin/java -jar /usr/share/java/cloudwatch_exporter/cloudwatch_exporter.jar 9106` | `/usr/bin/java -jar /usr/share/java/cloudwatch_exporter/cloudwatch_exporter.jar 9106` |
| CMD          | `/config/config.yml`                                                                  | `/config/config.yml`                                                                  |
| Workdir      | not specified                                                                         | not specified                                                                         |
| Has apk?     | yes                                                                                   | no                                                                                    |
| Has a shell? | yes                                                                                   | yes                                                                                   |

Check the [tags history page](/chainguard/chainguard-images/reference/prometheus-cloudwatch-exporter/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          |        |
| `busybox`                | X          | X      |
| `ca-certificates`        | X          | X      |
| `ca-certificates-bundle` | X          | X      |
| `chainguard-baselayout`  | X          | X      |
| `cloudwatch-exporter`    | X          | X      |
| `fontconfig-config`      | X          | X      |
| `freetype`               | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
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
| `libidn2`                | X          |        |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libpng`                 | X          | X      |
| `libpsl`                 | X          |        |
| `libssl3`                | X          |        |
| `libtasn1`               | X          | X      |
| `libunistring`           | X          |        |
| `ncurses`                | X          |        |
| `ncurses-terminfo-base`  | X          |        |
| `openjdk-17-default-jvm` | X          | X      |
| `openjdk-17-jre`         | X          | X      |
| `openjdk-17-jre-base`    | X          | X      |
| `openssl-config`         | X          | X      |
| `p11-kit`                | X          | X      |
| `p11-kit-trust`          | X          | X      |
| `wget`                   | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `zlib`                   | X          | X      |

