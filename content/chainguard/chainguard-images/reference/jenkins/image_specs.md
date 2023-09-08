---
title: "jenkins Image Variants"
type: "article"
description: "Detailed information about the public jenkins Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "jenkins"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **jenkins** Image.

## Variants Compared
The **jenkins** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                                                                                 |
|--------------|----------------------------------------------------------------------------------------|
| Default User | `65532`                                                                                |
| Entrypoint   | `/usr/bin/java -Duser.home=/var/jenkins_home -jar /usr/share/java/jenkins/jenkins.war` |
| CMD          | not specified                                                                          |
| Workdir      | `/app`                                                                                 |
| Has apk?     | no                                                                                     |
| Has a shell? | yes                                                                                    |

Check the [tags history page](/chainguard/chainguard-images/reference/jenkins/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest |
|--------------------------|--------|
| `bash`                   | X      |
| `busybox`                | X      |
| `ca-certificates-bundle` | X      |
| `coreutils`              | X      |
| `fontconfig-config`      | X      |
| `freetype`               | X      |
| `glibc`                  | X      |
| `glibc-locale-en`        | X      |
| `glibc-locale-posix`     | X      |
| `java-cacerts`           | X      |
| `java-common`            | X      |
| `jenkins`                | X      |
| `ld-linux`               | X      |
| `libacl1`                | X      |
| `libattr1`               | X      |
| `libbrotlicommon1`       | X      |
| `libbrotlidec1`          | X      |
| `libbz2-1`               | X      |
| `libcrypt1`              | X      |
| `libexpat1`              | X      |
| `libfontconfig1`         | X      |
| `libpng`                 | X      |
| `ncurses`                | X      |
| `ncurses-terminfo-base`  | X      |
| `openjdk-17-default-jvm` | X      |
| `openjdk-17-jre`         | X      |
| `openjdk-17-jre-base`    | X      |
| `ttf-dejavu`             | X      |
| `tzdata`                 | X      |
| `wolfi-baselayout`       | X      |
| `zlib`                   | X      |
