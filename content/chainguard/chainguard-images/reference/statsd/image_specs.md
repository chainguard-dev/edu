---
title: "statsd Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public statsd Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-02-09 00:19:29
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/statsd/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/statsd/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/statsd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/statsd/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **statsd** Image.

## Variants Compared
The **statsd** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                | latest                    |
|--------------|---------------------------|---------------------------|
| Default User | `nonroot`                 | `nonroot`                 |
| Entrypoint   | `node stats.js config.js` | `node stats.js config.js` |
| CMD          | not specified             | not specified             |
| Workdir      | `/usr/src/app`            | `/usr/src/app`            |
| Has apk?     | yes                       | no                        |
| Has a shell? | yes                       | no                        |

Check the [tags history page](/chainguard/chainguard-images/reference/statsd/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          |        |
| `busybox`                | X          |        |
| `c-ares`                 | X          | X      |
| `ca-certificates-bundle` | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `icu`                    | X          | X      |
| `ld-linux`               | X          | X      |
| `libbrotlicommon1`       | X          | X      |
| `libbrotlidec1`          | X          | X      |
| `libbrotlienc1`          | X          | X      |
| `libcrypt1`              | X          |        |
| `libcrypto3`             | X          | X      |
| `libcurl-openssl4`       | X          |        |
| `libexpat1`              | X          |        |
| `libgcc`                 | X          | X      |
| `libidn2`                | X          |        |
| `libnghttp2-14`          | X          | X      |
| `libpcre2-8-0`           | X          |        |
| `libproc-2-0`            | X          | X      |
| `libpsl`                 | X          |        |
| `libssl3`                | X          | X      |
| `libstdc++`              | X          | X      |
| `libunistring`           | X          |        |
| `ncurses`                | X          | X      |
| `ncurses-terminfo-base`  | X          | X      |
| `nodejs-18`              | X          | X      |
| `npm`                    | X          | X      |
| `openssl-config`         | X          | X      |
| `procps`                 | X          | X      |
| `statsd`                 | X          | X      |
| `wget`                   | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `zlib`                   | X          | X      |

