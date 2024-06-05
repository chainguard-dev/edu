---
title: "jenkins Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public jenkins Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-06-05 00:36:13
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/jenkins/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/jenkins/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/jenkins/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jenkins/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **jenkins** Image.

|              | latest-dev                          | latest                              |
|--------------|-------------------------------------|-------------------------------------|
| Default User | `jenkins`                           | `jenkins`                           |
| Entrypoint   | `tini -- /usr/local/bin/jenkins.sh` | `tini -- /usr/local/bin/jenkins.sh` |
| CMD          | not specified                       | not specified                       |
| Workdir      | not specified                       | not specified                       |
| Has apk?     | yes                                 | no                                  |
| Has a shell? | yes                                 | yes                                 |

Check the [tags history page](/chainguard/chainguard-images/reference/jenkins/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                 | latest-dev | latest |
|---------------------------------|------------|--------|
| `apk-tools`                     | X          |        |
| `bash`                          | X          | X      |
| `busybox`                       | X          | X      |
| `ca-certificates`               | X          | X      |
| `ca-certificates-bundle`        | X          | X      |
| `chainguard-baselayout`         | X          | X      |
| `coreutils`                     | X          | X      |
| `curl`                          | X          | X      |
| `fontconfig-config`             | X          | X      |
| `freetype`                      | X          | X      |
| `git`                           | X          | X      |
| `git-lfs`                       | X          | X      |
| `glibc`                         | X          | X      |
| `glibc-locale-en`               | X          | X      |
| `glibc-locale-posix`            | X          | X      |
| `gnupg`                         | X          | X      |
| `java-cacerts`                  | X          | X      |
| `java-common`                   | X          | X      |
| `jenkins`                       | X          | X      |
| `jenkins-compat`                | X          | X      |
| `jenkins-docker`                | X          | X      |
| `jenkins-entrypoint`            | X          | X      |
| `jenkins-plugin-manager`        | X          | X      |
| `jenkins-plugin-manager-compat` | X          | X      |
| `ld-linux`                      | X          | X      |
| `libacl1`                       | X          | X      |
| `libattr1`                      | X          | X      |
| `libbrotlicommon1`              | X          | X      |
| `libbrotlidec1`                 | X          | X      |
| `libbz2-1`                      | X          | X      |
| `libcrypt1`                     | X          | X      |
| `libcrypto3`                    | X          | X      |
| `libcurl-openssl4`              | X          | X      |
| `libedit`                       | X          | X      |
| `libexpat1`                     | X          | X      |
| `libffi`                        | X          | X      |
| `libfontconfig1`                | X          | X      |
| `libidn2`                       | X          | X      |
| `libnghttp2-14`                 | X          | X      |
| `libpcre2-8-0`                  | X          | X      |
| `libpng`                        | X          | X      |
| `libpsl`                        | X          | X      |
| `libssl3`                       | X          | X      |
| `libtasn1`                      | X          | X      |
| `libunistring`                  | X          | X      |
| `libxcrypt`                     | X          | X      |
| `ncurses`                       | X          | X      |
| `ncurses-terminfo-base`         | X          | X      |
| `openjdk-17-default-jvm`        | X          | X      |
| `openjdk-17-jre`                | X          | X      |
| `openjdk-17-jre-base`           | X          | X      |
| `openssh-client`                | X          | X      |
| `p11-kit`                       | X          | X      |
| `p11-kit-trust`                 | X          | X      |
| `tini`                          | X          | X      |
| `ttf-dejavu`                    | X          | X      |
| `tzdata`                        | X          | X      |
| `unzip`                         | X          | X      |
| `wget`                          | X          |        |
| `wolfi-baselayout`              | X          | X      |
| `zlib`                          | X          | X      |

