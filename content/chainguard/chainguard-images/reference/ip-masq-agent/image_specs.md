---
title: "ip-masq-agent Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public ip-masq-agent Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-02-08 00:18:32
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/ip-masq-agent/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/ip-masq-agent/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/ip-masq-agent/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/ip-masq-agent/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **ip-masq-agent** Image.

## Variants Compared
The **ip-masq-agent** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev               | latest                   |
|--------------|--------------------------|--------------------------|
| Default User | `root`                   | `root`                   |
| Entrypoint   | `/usr/bin/ip-masq-agent` | `/usr/bin/ip-masq-agent` |
| CMD          | not specified            | not specified            |
| Workdir      | not specified            | not specified            |
| Has apk?     | yes                      | no                       |
| Has a shell? | yes                      | no                       |

Check the [tags history page](/chainguard/chainguard-images/reference/ip-masq-agent/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          |        |
| `busybox`                | X          |        |
| `ca-certificates-bundle` | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `ip-masq-agent`          | X          | X      |
| `ip6tables`              | X          | X      |
| `iptables`               | X          | X      |
| `ld-linux`               | X          | X      |
| `libbrotlicommon1`       | X          |        |
| `libbrotlidec1`          | X          |        |
| `libcrypt1`              | X          |        |
| `libcrypto3`             | X          |        |
| `libcurl-openssl4`       | X          |        |
| `libexpat1`              | X          |        |
| `libidn2`                | X          |        |
| `libmnl`                 | X          | X      |
| `libnftnl`               | X          | X      |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libpsl`                 | X          |        |
| `libssl3`                | X          |        |
| `libunistring`           | X          |        |
| `ncurses`                | X          |        |
| `ncurses-terminfo-base`  | X          |        |
| `openssl-config`         | X          |        |
| `wget`                   | X          |        |
| `wolfi-baselayout`       | X          | X      |
| `zlib`                   | X          |        |

