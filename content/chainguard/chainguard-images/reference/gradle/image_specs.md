---
title: "Gradle Public Image Variants"
type: "article"
description: "Detailed information about the public Gradle Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Gradle"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **Gradle** Image.

## Variants Compared
The **gradle** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest            |
|--------------|-------------------|
| Default User | `gradle`          |
| Entrypoint   | `/usr/bin/gradle` |
| CMD          | not specified     |
| Workdir      | `/home/build`     |
| Has apk?     | no                |
| Has a shell? | yes               |

Check the [tags history page](/chainguard/chainguard-images/reference/gradle/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest |
|--------------------------|--------|
| `busybox`                | X      |
| `ca-certificates-bundle` | X      |
| `fontconfig-config`      | X      |
| `freetype`               | X      |
| `glibc`                  | X      |
| `glibc-locale-en`        | X      |
| `glibc-locale-posix`     | X      |
| `gradle-8`               | X      |
| `java-cacerts`           | X      |
| `java-common`            | X      |
| `ld-linux`               | X      |
| `libbrotlicommon1`       | X      |
| `libbrotlidec1`          | X      |
| `libbz2-1`               | X      |
| `libcrypt1`              | X      |
| `libexpat1`              | X      |
| `libfontconfig1`         | X      |
| `libpng`                 | X      |
| `openjdk-17`             | X      |
| `openjdk-17-default-jvm` | X      |
| `openjdk-17-jre`         | X      |
| `openjdk-17-jre-base`    | X      |
| `wolfi-baselayout`       | X      |
| `zlib`                   | X      |
