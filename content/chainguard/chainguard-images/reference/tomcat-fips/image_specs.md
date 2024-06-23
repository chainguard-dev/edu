---
title: "tomcat-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public tomcat-fips Chainguard Image."
date: 2024-06-23 00:43:06
lastmod: 2024-06-23 00:43:06
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/tomcat-fips/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/tomcat-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/tomcat-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/tomcat-fips/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **tomcat-fips** Image.

|              | latest-dev                          | latest                              |
|--------------|-------------------------------------|-------------------------------------|
| Default User | `nonroot`                           | `nonroot`                           |
| Entrypoint   | `/usr/local/tomcat/bin/catalina.sh` | `/usr/local/tomcat/bin/catalina.sh` |
| CMD          | `run`                               | `run`                               |
| Workdir      | `/usr/local/tomcat`                 | `/usr/local/tomcat`                 |
| Has apk?     | yes                                 | no                                  |
| Has a shell? | yes                                 | yes                                 |

Check the [tags history page](/chainguard/chainguard-images/reference/tomcat-fips/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                 | latest-dev | latest |
|---------------------------------|------------|--------|
| `apk-tools`                     | X          |        |
| `bash`                          | X          | X      |
| `bouncycastle-fips`             | X          | X      |
| `bouncycastle-pkix-fips`        | X          | X      |
| `bouncycastle-tls-fips`         | X          | X      |
| `busybox`                       | X          | X      |
| `ca-certificates`               | X          | X      |
| `ca-certificates-bundle`        | X          | X      |
| `chainguard-baselayout`         | X          | X      |
| `fontconfig-config`             | X          | X      |
| `freetype`                      | X          | X      |
| `git`                           | X          |        |
| `glibc`                         | X          | X      |
| `glibc-locale-posix`            | X          | X      |
| `java-cacerts`                  | X          | X      |
| `java-common`                   | X          | X      |
| `ld-linux`                      | X          | X      |
| `libapr`                        | X          | X      |
| `libbrotlicommon1`              | X          | X      |
| `libbrotlidec1`                 | X          | X      |
| `libbz2-1`                      | X          | X      |
| `libcrypt1`                     | X          | X      |
| `libcrypto3`                    | X          | X      |
| `libcurl-openssl4`              | X          |        |
| `libexpat1`                     | X          | X      |
| `libffi`                        | X          | X      |
| `libfontconfig1`                | X          | X      |
| `libidn2`                       | X          |        |
| `libnghttp2-14`                 | X          |        |
| `libpcre2-8-0`                  | X          |        |
| `libpng`                        | X          | X      |
| `libpsl`                        | X          |        |
| `libssl3`                       | X          | X      |
| `libtasn1`                      | X          | X      |
| `libunistring`                  | X          |        |
| `libxcrypt`                     | X          | X      |
| `ncurses`                       | X          | X      |
| `ncurses-terminfo-base`         | X          | X      |
| `openjdk-17-default-jvm-bcfips` | X          | X      |
| `openjdk-17-jre-base-bcfips`    | X          | X      |
| `openjdk-17-jre-bcfips`         | X          | X      |
| `openssl-config-fipshardened`   | X          | X      |
| `openssl-provider-fips`         | X          | X      |
| `p11-kit`                       | X          | X      |
| `p11-kit-trust`                 | X          | X      |
| `tomcat-10.1-fips`              | X          | X      |
| `tomcat-10.1-fips-webapps`      | X          | X      |
| `tomcat-native`                 | X          | X      |
| `wget`                          | X          |        |
| `wolfi-baselayout`              | X          | X      |
| `zlib`                          | X          | X      |

