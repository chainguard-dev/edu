---
title: "busybox Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public busybox Chainguard Image variants"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/busybox/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/busybox/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/busybox/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/busybox/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **busybox** Image.

## Variants Compared
The **busybox** Chainguard Image currently has 2 public variants: 

- `latest-glibc`
- `latest`

The table has detailed information about each of these variants.

|              | latest-glibc  | latest        |
|--------------|---------------|---------------|
| Default User | `nonroot`     | `nonroot`     |
| Entrypoint   | not specified | not specified |
| CMD          | not specified | not specified |
| Workdir      | not specified | not specified |
| Has apk?     | no            | no            |
| Has a shell? | yes           | yes           |

Check the [tags history page](/chainguard/chainguard-images/reference/busybox/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-glibc | latest |
|--------------------------|--------------|--------|
| `busybox`                | X            | X      |
| `ca-certificates-bundle` | X            | X      |
| `glibc`                  | X            |        |
| `glibc-locale-posix`     | X            |        |
| `ld-linux`               | X            |        |
| `libcrypt1`              | X            |        |
| `wolfi-baselayout`       | X            |        |
| `alpine-baselayout-data` |              | X      |
| `alpine-keys`            |              | X      |
| `alpine-release`         |              | X      |
| `libcrypto3`             |              | X      |
| `libssl3`                |              | X      |
| `musl`                   |              | X      |
| `ssl_client`             |              | X      |

