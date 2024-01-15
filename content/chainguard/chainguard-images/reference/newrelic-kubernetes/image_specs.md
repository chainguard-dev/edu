---
title: "newrelic-kubernetes Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public newrelic-kubernetes Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-01-15 00:20:04
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/newrelic-kubernetes/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/newrelic-kubernetes/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/newrelic-kubernetes/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/newrelic-kubernetes/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **newrelic-kubernetes** Image.

## Variants Compared
The **newrelic-kubernetes** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                              | latest                                  |
|--------------|-----------------------------------------|-----------------------------------------|
| Default User | `nri`                                   | `nri`                                   |
| Entrypoint   | `/sbin/tini -- /usr/bin/nri-kubernetes` | `/sbin/tini -- /usr/bin/nri-kubernetes` |
| CMD          | not specified                           | not specified                           |
| Workdir      | not specified                           | not specified                           |
| Has apk?     | yes                                     | no                                      |
| Has a shell? | yes                                     | yes                                     |

Check the [tags history page](/chainguard/chainguard-images/reference/newrelic-kubernetes/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          |        |
| `bind-libs`              | X          | X      |
| `bind-tools`             | X          | X      |
| `busybox`                | X          | X      |
| `c-ares`                 | X          | X      |
| `ca-certificates-bundle` | X          | X      |
| `fstrm`                  | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `keyutils-libs`          | X          | X      |
| `krb5-conf`              | X          | X      |
| `krb5-libs`              | X          | X      |
| `ld-linux`               | X          | X      |
| `libbrotlicommon1`       | X          |        |
| `libbrotlidec1`          | X          |        |
| `libcom_err`             | X          | X      |
| `libcrypt1`              | X          | X      |
| `libcrypto3`             | X          | X      |
| `libcurl-openssl4`       | X          |        |
| `libev`                  | X          | X      |
| `libexpat1`              | X          |        |
| `libgcc`                 | X          | X      |
| `libidn2`                | X          |        |
| `libnghttp2-14`          | X          | X      |
| `libpcre2-8-0`           | X          |        |
| `libpsl`                 | X          |        |
| `libssl3`                | X          | X      |
| `libstdc++`              | X          | X      |
| `libunistring`           | X          |        |
| `libuv`                  | X          | X      |
| `libverto`               | X          | X      |
| `libxml2`                | X          | X      |
| `ncurses`                | X          |        |
| `ncurses-terminfo-base`  | X          |        |
| `nghttp2`                | X          | X      |
| `nghttp2-dev`            | X          | X      |
| `nri-kubernetes`         | X          | X      |
| `openssl-config`         | X          | X      |
| `protobuf-c`             | X          | X      |
| `tini`                   | X          | X      |
| `wolfi-baselayout`       | X          | X      |
| `xz`                     | X          | X      |
| `zlib`                   | X          | X      |

