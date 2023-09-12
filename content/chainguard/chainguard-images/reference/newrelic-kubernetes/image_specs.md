---
title: "newrelic-kubernetes Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public newrelic-kubernetes Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
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
The **newrelic-kubernetes** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                                  |
|--------------|-----------------------------------------|
| Default User | `nri`                                   |
| Entrypoint   | `/sbin/tini -- /usr/bin/nri-kubernetes` |
| CMD          | not specified                           |
| Workdir      | not specified                           |
| Has apk?     | no                                      |
| Has a shell? | yes                                     |

Check the [tags history page](/chainguard/chainguard-images/reference/newrelic-kubernetes/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest |
|--------------------------|--------|
| `bind-libs`              | X      |
| `bind-tools`             | X      |
| `busybox`                | X      |
| `c-ares`                 | X      |
| `ca-certificates-bundle` | X      |
| `fstrm`                  | X      |
| `glibc`                  | X      |
| `glibc-locale-posix`     | X      |
| `keyutils-libs`          | X      |
| `krb5-conf`              | X      |
| `krb5-libs`              | X      |
| `ld-linux`               | X      |
| `libcom_err`             | X      |
| `libcrypt1`              | X      |
| `libcrypto3`             | X      |
| `libev`                  | X      |
| `libgcc`                 | X      |
| `libnghttp2-14`          | X      |
| `libssl3`                | X      |
| `libstdc++`              | X      |
| `libuv`                  | X      |
| `libverto`               | X      |
| `libxml2`                | X      |
| `nghttp2`                | X      |
| `nghttp2-dev`            | X      |
| `nri-kubernetes`         | X      |
| `openssl-config`         | X      |
| `protobuf-c`             | X      |
| `tini`                   | X      |
| `wolfi-baselayout`       | X      |
| `xz`                     | X      |
| `zlib`                   | X      |

