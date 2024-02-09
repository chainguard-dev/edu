---
title: "filebeat Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public filebeat Chainguard Image variants"
date: 2024-02-09 00:19:29
lastmod: 2024-02-09 00:19:29
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/filebeat/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/filebeat/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/filebeat/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/filebeat/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **filebeat** Image.

## Variants Compared
The **filebeat** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                                       | latest                                           |
|--------------|--------------------------------------------------|--------------------------------------------------|
| Default User | `nonroot`                                        | `nonroot`                                        |
| Entrypoint   | `/sbin/tini -- /usr/local/bin/docker-entrypoint` | `/sbin/tini -- /usr/local/bin/docker-entrypoint` |
| CMD          | `-environment container`                         | `-environment container`                         |
| Workdir      | `/usr/share/filebeat`                            | `/usr/share/filebeat`                            |
| Has apk?     | yes                                              | no                                               |
| Has a shell? | yes                                              | yes                                              |

Check the [tags history page](/chainguard/chainguard-images/reference/filebeat/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          | X      |
| `busybox`                | X          | X      |
| `ca-certificates-bundle` | X          | X      |
| `curl`                   | X          | X      |
| `filebeat`               | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `ld-linux`               | X          | X      |
| `libbrotlicommon1`       | X          | X      |
| `libbrotlidec1`          | X          | X      |
| `libcrypt1`              | X          | X      |
| `libcrypto3`             | X          | X      |
| `libcurl-openssl4`       | X          | X      |
| `libexpat1`              | X          |        |
| `libidn2`                | X          | X      |
| `libnghttp2-14`          | X          | X      |
| `libpcre2-8-0`           | X          |        |
| `libpsl`                 | X          | X      |
| `libssl3`                | X          | X      |
| `libunistring`           | X          | X      |
| `ncurses`                | X          | X      |
| `ncurses-terminfo-base`  | X          | X      |
| `openssl-config`         | X          | X      |
| `tini`                   | X          | X      |
| `wget`                   | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `zlib`                   | X          | X      |

