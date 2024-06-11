---
title: "dependency-track Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public dependency-track Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-06-11 00:42:18
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

|              | latest-dev                                                                                                                                                                                                                                                                                                   |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Default User | `dtrack`                                                                                                                                                                                                                                                                                                     |
| Entrypoint   | not specified                                                                                                                                                                                                                                                                                                |
| CMD          | `sh -c "exec java ${JAVA_OPTIONS} ${EXTRA_JAVA_OPTIONS} --add-opens java.base/java.util.concurrent=ALL-UNNAMED -Dlogback.configurationFile=${LOGGING_CONFIG_PATH} -DdependencyTrack.logging.level=${LOGGING_LEVEL} -jar /usr/share/java/dependency-track/dependency-track-bundled.jar -context ${CONTEXT}"
` |
| Workdir      | `/usr/share/java/dependency-track`                                                                                                                                                                                                                                                                           |
| Has apk?     | yes                                                                                                                                                                                                                                                                                                          |
| Has a shell? | yes                                                                                                                                                                                                                                                                                                          |

Check the [tags history page](/chainguard/chainguard-images/reference/dependency-track/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                            | latest-dev |
|----------------------------|------------|
| `apk-tools`                | X          |
| `bash`                     | X          |
| `busybox`                  | X          |
| `ca-certificates`          | X          |
| `ca-certificates-bundle`   | X          |
| `chainguard-baselayout`    | X          |
| `dependency-track-bundled` | X          |
| `fontconfig-config`        | X          |
| `freetype`                 | X          |
| `git`                      | X          |
| `glibc`                    | X          |
| `glibc-locale-posix`       | X          |
| `java-cacerts`             | X          |
| `java-common`              | X          |
| `ld-linux`                 | X          |
| `libbrotlicommon1`         | X          |
| `libbrotlidec1`            | X          |
| `libbz2-1`                 | X          |
| `libcrypt1`                | X          |
| `libcrypto3`               | X          |
| `libcurl-openssl4`         | X          |
| `libexpat1`                | X          |
| `libffi`                   | X          |
| `libfontconfig1`           | X          |
| `libidn2`                  | X          |
| `libnghttp2-14`            | X          |
| `libpcre2-8-0`             | X          |
| `libpng`                   | X          |
| `libpsl`                   | X          |
| `libssl3`                  | X          |
| `libtasn1`                 | X          |
| `libunistring`             | X          |
| `libxcrypt`                | X          |
| `ncurses`                  | X          |
| `ncurses-terminfo-base`    | X          |
| `openjdk-17-default-jvm`   | X          |
| `openjdk-17-jre`           | X          |
| `openjdk-17-jre-base`      | X          |
| `p11-kit`                  | X          |
| `p11-kit-trust`            | X          |
| `wget`                     | X          |
| `wolfi-baselayout`         | X          |
| `zlib`                     | X          |

