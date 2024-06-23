---
title: "neuvector-manager Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public neuvector-manager Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-06-23 00:43:06
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/neuvector-manager/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/neuvector-manager/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/neuvector-manager/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/neuvector-manager/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **neuvector-manager** Image.

|              | latest-dev                                                                                                             | latest                                                                                                                 |
|--------------|------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Default User | `manager`                                                                                                              | `manager`                                                                                                              |
| Entrypoint   | `java -Xms256m -Xmx2048m -Djdk.tls.rejectClientInitiatedRenegotiation=true -jar /usr/local/bin/admin-assembly-1.0.jar` | `java -Xms256m -Xmx2048m -Djdk.tls.rejectClientInitiatedRenegotiation=true -jar /usr/local/bin/admin-assembly-1.0.jar` |
| CMD          | not specified                                                                                                          | not specified                                                                                                          |
| Workdir      | not specified                                                                                                          | not specified                                                                                                          |
| Has apk?     | yes                                                                                                                    | no                                                                                                                     |
| Has a shell? | yes                                                                                                                    | yes                                                                                                                    |

Check the [tags history page](/chainguard/chainguard-images/reference/neuvector-manager/tags_history/) for the full list of available tags.

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
| `fontconfig-config`      | X          | X      |
| `freetype`               | X          | X      |
| `gdbm`                   | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `iproute2`               | X          | X      |
| `iptables`               | X          | X      |
| `java-cacerts`           | X          | X      |
| `java-common`            | X          | X      |
| `ld-linux`               | X          | X      |
| `libbrotlicommon1`       | X          | X      |
| `libbrotlidec1`          | X          | X      |
| `libbz2-1`               | X          | X      |
| `libcrypt1`              | X          | X      |
| `libcrypto3`             | X          | X      |
| `libcurl-openssl4`       | X          |        |
| `libelf`                 | X          | X      |
| `libexpat1`              | X          | X      |
| `libffi`                 | X          | X      |
| `libfontconfig1`         | X          | X      |
| `libgcc`                 | X          | X      |
| `libidn2`                | X          |        |
| `libmnl`                 | X          | X      |
| `libnftnl`               | X          | X      |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libpng`                 | X          | X      |
| `libproc-2-0`            | X          | X      |
| `libpsl`                 | X          |        |
| `libssl3`                | X          | X      |
| `libstdc++`              | X          | X      |
| `libtasn1`               | X          | X      |
| `libunistring`           | X          |        |
| `libxcrypt`              | X          | X      |
| `libzstd1`               | X          | X      |
| `mpdecimal`              | X          | X      |
| `ncurses`                | X          | X      |
| `ncurses-terminfo-base`  | X          | X      |
| `neuvector-manager`      | X          | X      |
| `neuvector-manager-cli`  | X          | X      |
| `openjdk-11-default-jvm` | X          | X      |
| `openjdk-11-jre`         | X          | X      |
| `openjdk-11-jre-base`    | X          | X      |
| `p11-kit`                | X          | X      |
| `p11-kit-trust`          | X          | X      |
| `procps`                 | X          | X      |
| `py3-certifi`            | X          | X      |
| `py3-charset-normalizer` | X          | X      |
| `py3-click`              | X          | X      |
| `py3-colorama`           | X          | X      |
| `py3-idna`               | X          | X      |
| `py3-importlib-metadata` | X          | X      |
| `py3-requests`           | X          | X      |
| `py3-typing-extensions`  | X          | X      |
| `py3-urllib3`            | X          | X      |
| `py3-zipp`               | X          | X      |
| `py3.12-setuptools`      | X          | X      |
| `py3.12-six`             | X          | X      |
| `python-3.12`            | X          | X      |
| `python-3.12-base`       | X          | X      |
| `readline`               | X          | X      |
| `sqlite-libs`            | X          | X      |
| `supervisor`             | X          | X      |
| `supervisor-config`      | X          |        |
| `wget`                   | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `xz`                     | X          | X      |
| `zlib`                   | X          | X      |

