---
title: "datadog-agent-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public datadog-agent-fips Chainguard Image."
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-03-08 00:56:03
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/datadog-agent-fips/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/datadog-agent-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/datadog-agent-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/datadog-agent-fips/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **datadog-agent-fips** Image.

|              | latest-dev                           | latest                               |
|--------------|--------------------------------------|--------------------------------------|
| Default User | `nonroot`                            | `nonroot`                            |
| Entrypoint   | `/opt/datadog-agent/bin/agent/agent` | `/opt/datadog-agent/bin/agent/agent` |
| CMD          | not specified                        | not specified                        |
| Workdir      | not specified                        | not specified                        |
| Has apk?     | yes                                  | no                                   |
| Has a shell? | yes                                  | no                                   |

Check the [tags history page](/chainguard/chainguard-images/reference/datadog-agent-fips/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                               | latest-dev | latest |
|-------------------------------|------------|--------|
| `apk-tools`                   | X          |        |
| `bash`                        | X          |        |
| `busybox`                     | X          |        |
| `ca-certificates`             | X          | X      |
| `ca-certificates-bundle`      | X          | X      |
| `chainguard-baselayout`       | X          | X      |
| `datadog-agent`               | X          | X      |
| `fontconfig-config`           | X          | X      |
| `freetype`                    | X          | X      |
| `gdbm`                        | X          | X      |
| `git`                         | X          |        |
| `glibc`                       | X          | X      |
| `glibc-locale-posix`          | X          | X      |
| `java-cacerts`                | X          | X      |
| `java-common`                 | X          | X      |
| `ld-linux`                    | X          | X      |
| `libbrotlicommon1`            | X          | X      |
| `libbrotlidec1`               | X          | X      |
| `libbz2-1`                    | X          | X      |
| `libcrypt1`                   | X          | X      |
| `libcrypto3`                  | X          | X      |
| `libcurl-openssl4`            | X          |        |
| `libexpat1`                   | X          | X      |
| `libffi`                      | X          | X      |
| `libfontconfig1`              | X          | X      |
| `libgcc`                      | X          | X      |
| `libidn2`                     | X          |        |
| `libnghttp2-14`               | X          |        |
| `libpcre2-8-0`                | X          |        |
| `libpng`                      | X          | X      |
| `libpsl`                      | X          |        |
| `libssl3`                     | X          | X      |
| `libstdc++`                   | X          | X      |
| `libtasn1`                    | X          | X      |
| `libunistring`                | X          |        |
| `mpdecimal`                   | X          | X      |
| `ncurses`                     | X          | X      |
| `ncurses-terminfo-base`       | X          | X      |
| `openjdk-11`                  | X          | X      |
| `openjdk-11-jre`              | X          | X      |
| `openjdk-11-jre-base`         | X          | X      |
| `openssl-config-fipshardened` | X          | X      |
| `openssl-provider-fips`       | X          | X      |
| `p11-kit`                     | X          | X      |
| `p11-kit-trust`               | X          | X      |
| `python-3.12`                 | X          | X      |
| `python-3.12-default`         | X          | X      |
| `readline`                    | X          | X      |
| `sqlite-libs`                 | X          | X      |
| `wget`                        | X          |        |
| `wolfi-baselayout`            | X          | X      |
| `xz`                          | X          | X      |
| `zlib`                        | X          | X      |

