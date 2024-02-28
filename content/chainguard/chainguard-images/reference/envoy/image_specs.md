---
title: "envoy Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public envoy Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-02-28 20:17:58
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/envoy/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/envoy/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/envoy/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/envoy/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **envoy** Image.

## Variants Compared
The **envoy** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                                | latest                                    |
|--------------|-------------------------------------------|-------------------------------------------|
| Default User | `envoy`                                   | `envoy`                                   |
| Entrypoint   | `/var/lib/envoy/init/envoy-entrypoint.sh` | `/var/lib/envoy/init/envoy-entrypoint.sh` |
| CMD          | not specified                             | not specified                             |
| Workdir      | not specified                             | not specified                             |
| Has apk?     | yes                                       | no                                        |
| Has a shell? | yes                                       | yes                                       |

Check the [tags history page](/chainguard/chainguard-images/reference/envoy/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                             | latest-dev | latest |
|-----------------------------|------------|--------|
| `apk-tools`                 | X          |        |
| `bash`                      | X          |        |
| `busybox`                   | X          | X      |
| `ca-certificates-bundle`    | X          | X      |
| `envoy-1.29`                | X          | X      |
| `envoy-1.29-config`         | X          | X      |
| `envoy-1.29-oci-entrypoint` | X          | X      |
| `git`                       | X          |        |
| `glibc`                     | X          | X      |
| `glibc-locale-posix`        | X          | X      |
| `ld-linux`                  | X          | X      |
| `libbrotlicommon1`          | X          |        |
| `libbrotlidec1`             | X          |        |
| `libcrypt1`                 | X          | X      |
| `libcrypto3`                | X          |        |
| `libcurl-openssl4`          | X          |        |
| `libexpat1`                 | X          |        |
| `libidn2`                   | X          |        |
| `libnghttp2-14`             | X          |        |
| `libpcre2-8-0`              | X          |        |
| `libpsl`                    | X          |        |
| `libssl3`                   | X          |        |
| `libunistring`              | X          |        |
| `ncurses`                   | X          |        |
| `ncurses-terminfo-base`     | X          |        |
| `openssl-config`            | X          |        |
| `su-exec`                   | X          | X      |
| `wget`                      | X          |        |
| `wolfi-baselayout`          | X          | X      |
| `zlib`                      | X          |        |

