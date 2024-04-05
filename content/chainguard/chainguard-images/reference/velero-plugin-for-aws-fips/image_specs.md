---
title: "velero-plugin-for-aws-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public velero-plugin-for-aws-fips Chainguard Image."
date: 2024-04-05 00:47:12
lastmod: 2024-04-05 00:47:12
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/velero-plugin-for-aws-fips/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/velero-plugin-for-aws-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/velero-plugin-for-aws-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/velero-plugin-for-aws-fips/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **velero-plugin-for-aws-fips** Image.

|              | latest-dev                                                                    | latest                                                                        |
|--------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| Default User | `nonroot`                                                                     | `nonroot`                                                                     |
| Entrypoint   | `/bin/cp-plugin /plugins/velero-plugin-for-aws /target/velero-plugin-for-aws` | `/bin/cp-plugin /plugins/velero-plugin-for-aws /target/velero-plugin-for-aws` |
| CMD          | not specified                                                                 | not specified                                                                 |
| Workdir      | not specified                                                                 | not specified                                                                 |
| Has apk?     | yes                                                                           | no                                                                            |
| Has a shell? | yes                                                                           | no                                                                            |

Check the [tags history page](/chainguard/chainguard-images/reference/velero-plugin-for-aws-fips/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                     | latest-dev | latest |
|-------------------------------------|------------|--------|
| `apk-tools`                         | X          |        |
| `bash`                              | X          |        |
| `busybox`                           | X          |        |
| `ca-certificates-bundle`            | X          | X      |
| `chainguard-baselayout`             | X          | X      |
| `git`                               | X          |        |
| `glibc`                             | X          | X      |
| `glibc-locale-posix`                | X          | X      |
| `ld-linux`                          | X          | X      |
| `libbrotlicommon1`                  | X          |        |
| `libbrotlidec1`                     | X          |        |
| `libcrypt1`                         | X          |        |
| `libcrypto3`                        | X          | X      |
| `libcurl-openssl4`                  | X          |        |
| `libexpat1`                         | X          |        |
| `libidn2`                           | X          |        |
| `libnghttp2-14`                     | X          |        |
| `libpcre2-8-0`                      | X          |        |
| `libpsl`                            | X          |        |
| `libssl3`                           | X          | X      |
| `libunistring`                      | X          |        |
| `libxcrypt`                         | X          |        |
| `ncurses`                           | X          |        |
| `ncurses-terminfo-base`             | X          |        |
| `openssl-config-fipshardened`       | X          | X      |
| `openssl-provider-fips`             | X          | X      |
| `velero-plugin-for-aws-fips`        | X          | X      |
| `velero-plugin-for-aws-fips-compat` | X          | X      |
| `wget`                              | X          |        |
| `wolfi-baselayout`                  | X          | X      |
| `zlib`                              | X          |        |

