---
title: "haproxy Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public haproxy Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/haproxy/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/haproxy/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/haproxy/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/haproxy/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **haproxy** Image.

## Variants Compared
The **haproxy** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                                |
|--------------|---------------------------------------|
| Default User | `haproxy`                             |
| Entrypoint   | `/usr/local/bin/docker-entrypoint.sh` |
| CMD          | not specified                         |
| Workdir      | not specified                         |
| Has apk?     | no                                    |
| Has a shell? | yes                                   |

Check the [tags history page](/chainguard/chainguard-images/reference/haproxy/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest |
|--------------------------|--------|
| `bash`                   | X      |
| `busybox`                | X      |
| `ca-certificates-bundle` | X      |
| `dataplaneapi`           | X      |
| `glibc`                  | X      |
| `glibc-locale-posix`     | X      |
| `haproxy`                | X      |
| `haproxy-oci-entrypoint` | X      |
| `ld-linux`               | X      |
| `libcrypt1`              | X      |
| `libcrypto3`             | X      |
| `libgcc`                 | X      |
| `libpcre2-8-0`           | X      |
| `libpcre2-posix-3`       | X      |
| `libssl3`                | X      |
| `ncurses`                | X      |
| `ncurses-terminfo-base`  | X      |
| `openssl-config`         | X      |
| `posix-libc-utils`       | X      |
| `wolfi-baselayout`       | X      |

