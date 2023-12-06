---
title: "jenkins Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public jenkins Chainguard Image variants"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jenkins/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/jenkins/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/jenkins/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jenkins/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **jenkins** Image.

## Variants Compared
The **jenkins** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                                                                                 |
|--------------|----------------------------------------------------------------------------------------|
| Default User | `jenkins`                                                                              |
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
| `ca-certificates`        | X      |
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
| `libcrypto3`             | X      |
| `libexpat1`              | X      |
| `libffi`                 | X      |
| `libfontconfig1`         | X      |
| `libpng`                 | X      |
| `libtasn1`               | X      |
| `ncurses`                | X      |
| `ncurses-terminfo-base`  | X      |
| `openjdk-17-default-jvm` | X      |
| `openjdk-17-jre`         | X      |
| `openjdk-17-jre-base`    | X      |
| `openssl-config`         | X      |
| `p11-kit`                | X      |
| `p11-kit-trust`          | X      |
| `ttf-dejavu`             | X      |
| `tzdata`                 | X      |
| `wolfi-baselayout`       | X      |
| `zlib`                   | X      |

