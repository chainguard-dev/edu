---
title: "prometheus-cloudwatch-exporter Image Variants"
type: "article"
description: "Detailed information about the public prometheus-cloudwatch-exporter Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "prometheus-cloudwatch-exporter"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **prometheus-cloudwatch-exporter** Image.

## Variants Compared
The **prometheus-cloudwatch-exporter** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                                                                            | latest                                                                                |
|--------------|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| Default User | `65532`                                                                               | `65532`                                                                               |
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
| `ca-certificates-bundle` | X          | X      |
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
| `libcrypto3`             | X          |        |
| `libcurl-openssl4`       | X          |        |
| `libexpat1`              | X          | X      |
| `libfontconfig1`         | X          | X      |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libpng`                 | X          | X      |
| `libssl3`                | X          |        |
| `ncurses`                | X          |        |
| `ncurses-terminfo-base`  | X          |        |
| `openjdk-17-default-jvm` | X          | X      |
| `openjdk-17-jre`         | X          | X      |
| `openjdk-17-jre-base`    | X          | X      |
| `openssl-config`         | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `zlib`                   | X          | X      |
