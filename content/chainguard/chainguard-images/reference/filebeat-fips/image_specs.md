---
title: "filebeat-fips Image Details"
type: "article"
unlisted: true
description: "Detailed information about the public filebeat-fips Chainguard Image."
date: 2024-02-29 16:25:55
lastmod: 2024-02-29 16:25:55
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/filebeat-fips/" >}}
{{< tab title="Details" active=true url="/chainguard/chainguard-images/reference/filebeat-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/filebeat-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/filebeat-fips/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about the Chainguard **filebeat-fips** Image.

|              | latest-dev                                       | latest                                           |
|--------------|--------------------------------------------------|--------------------------------------------------|
| Default User | `nonroot`                                        | `nonroot`                                        |
| Entrypoint   | `/sbin/tini -- /usr/local/bin/docker-entrypoint` | `/sbin/tini -- /usr/local/bin/docker-entrypoint` |
| CMD          | `-environment container`                         | `-environment container`                         |
| Workdir      | `/usr/share/filebeat`                            | `/usr/share/filebeat`                            |
| Has apk?     | yes                                              | no                                               |
| Has a shell? | yes                                              | yes                                              |

Check the [tags history page](/chainguard/chainguard-images/reference/filebeat-fips/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                               | latest-dev | latest |
|-------------------------------|------------|--------|
| `apk-tools`                   | X          |        |
| `bash`                        | X          | X      |
| `busybox`                     | X          | X      |
| `ca-certificates-bundle`      | X          | X      |
| `chainguard-baselayout`       | X          | X      |
| `curl`                        | X          | X      |
| `filebeat-fips`               | X          | X      |
| `git`                         | X          |        |
| `glibc`                       | X          | X      |
| `glibc-locale-posix`          | X          | X      |
| `ld-linux`                    | X          | X      |
| `libbrotlicommon1`            | X          | X      |
| `libbrotlidec1`               | X          | X      |
| `libcrypt1`                   | X          | X      |
| `libcrypto3`                  | X          | X      |
| `libcurl-openssl4`            | X          | X      |
| `libexpat1`                   | X          |        |
| `libidn2`                     | X          | X      |
| `libnghttp2-14`               | X          | X      |
| `libpcre2-8-0`                | X          |        |
| `libpsl`                      | X          | X      |
| `libssl3`                     | X          | X      |
| `libunistring`                | X          | X      |
| `ncurses`                     | X          | X      |
| `ncurses-terminfo-base`       | X          | X      |
| `openssl-config-fipshardened` | X          | X      |
| `openssl-provider-fips`       | X          | X      |
| `tini`                        | X          | X      |
| `wget`                        | X          |        |
| `wolfi-baselayout`            | X          | X      |
| `zlib`                        | X          | X      |

