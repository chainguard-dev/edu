---
title: "dependency-track Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public dependency-track Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-05-01 00:46:56
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/dependency-track/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/dependency-track/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/dependency-track/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/dependency-track/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **dependency-track** Image.

|              | latest-dev                                                                                                                                                                                                                                                                                                   | latest                                                                                                                                                                                                                                                                                                       |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Default User | `dtrack`                                                                                                                                                                                                                                                                                                     | `dtrack`                                                                                                                                                                                                                                                                                                     |
| Entrypoint   | not specified                                                                                                                                                                                                                                                                                                | not specified                                                                                                                                                                                                                                                                                                |
| CMD          | `sh -c "exec java ${JAVA_OPTIONS} ${EXTRA_JAVA_OPTIONS} --add-opens java.base/java.util.concurrent=ALL-UNNAMED -Dlogback.configurationFile=${LOGGING_CONFIG_PATH} -DdependencyTrack.logging.level=${LOGGING_LEVEL} -jar /usr/share/java/dependency-track/dependency-track-bundled.jar -context ${CONTEXT}"
` | `sh -c "exec java ${JAVA_OPTIONS} ${EXTRA_JAVA_OPTIONS} --add-opens java.base/java.util.concurrent=ALL-UNNAMED -Dlogback.configurationFile=${LOGGING_CONFIG_PATH} -DdependencyTrack.logging.level=${LOGGING_LEVEL} -jar /usr/share/java/dependency-track/dependency-track-bundled.jar -context ${CONTEXT}"
` |
| Workdir      | `/usr/share/java/dependency-track`                                                                                                                                                                                                                                                                           | `/usr/share/java/dependency-track`                                                                                                                                                                                                                                                                           |
| Has apk?     | yes                                                                                                                                                                                                                                                                                                          | no                                                                                                                                                                                                                                                                                                           |
| Has a shell? | yes                                                                                                                                                                                                                                                                                                          | yes                                                                                                                                                                                                                                                                                                          |

Check the [tags history page](/chainguard/chainguard-images/reference/dependency-track/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                            | latest-dev | latest |
|----------------------------|------------|--------|
| `apk-tools`                | X          |        |
| `bash`                     | X          |        |
| `busybox`                  | X          | X      |
| `ca-certificates`          | X          | X      |
| `ca-certificates-bundle`   | X          | X      |
| `chainguard-baselayout`    | X          | X      |
| `dependency-track-bundled` | X          | X      |
| `fontconfig-config`        | X          | X      |
| `freetype`                 | X          | X      |
| `git`                      | X          |        |
| `glibc`                    | X          | X      |
| `glibc-locale-posix`       | X          | X      |
| `java-cacerts`             | X          | X      |
| `java-common`              | X          | X      |
| `ld-linux`                 | X          | X      |
| `libbrotlicommon1`         | X          | X      |
| `libbrotlidec1`            | X          | X      |
| `libbz2-1`                 | X          | X      |
| `libcrypt1`                | X          | X      |
| `libcrypto3`               | X          | X      |
| `libcurl-openssl4`         | X          |        |
| `libexpat1`                | X          | X      |
| `libffi`                   | X          | X      |
| `libfontconfig1`           | X          | X      |
| `libidn2`                  | X          |        |
| `libnghttp2-14`            | X          |        |
| `libpcre2-8-0`             | X          |        |
| `libpng`                   | X          | X      |
| `libpsl`                   | X          |        |
| `libssl3`                  | X          |        |
| `libtasn1`                 | X          | X      |
| `libunistring`             | X          |        |
| `libxcrypt`                | X          | X      |
| `ncurses`                  | X          |        |
| `ncurses-terminfo-base`    | X          |        |
| `openjdk-17-default-jvm`   | X          | X      |
| `openjdk-17-jre`           | X          | X      |
| `openjdk-17-jre-base`      | X          | X      |
| `p11-kit`                  | X          | X      |
| `p11-kit-trust`            | X          | X      |
| `wget`                     | X          |        |
| `wolfi-baselayout`         | X          | X      |
| `zlib`                     | X          | X      |

