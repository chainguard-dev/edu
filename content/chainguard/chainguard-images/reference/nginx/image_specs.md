---
title: "nginx Image Variants"
type: "article"
unlisted: true
description: "Detailed information about the public nginx Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2024-01-12 00:39:30
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
weight: 550
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=false url="/chainguard/chainguard-images/reference/nginx/" >}}
{{< tab title="Variants" active=true url="/chainguard/chainguard-images/reference/nginx/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/nginx/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/nginx/provenance_info/" >}}
{{</ tabs >}}

This page shows detailed information about all public variants of the Chainguard **nginx** Image.

## Variants Compared
The **nginx** Chainguard Image currently has 2 public variants: 

- `latest-dev`
- `latest`

The table has detailed information about each of these variants.

|              | latest-dev                                                 | latest                                                     |
|--------------|------------------------------------------------------------|------------------------------------------------------------|
| Default User | `nginx`                                                    | `nginx`                                                    |
| Entrypoint   | `/usr/sbin/nginx`                                          | `/usr/sbin/nginx`                                          |
| CMD          | `-c /etc/nginx/nginx.conf -e /dev/stderr -g "daemon off;"` | `-c /etc/nginx/nginx.conf -e /dev/stderr -g "daemon off;"` |
| Workdir      | not specified                                              | not specified                                              |
| Has apk?     | yes                                                        | no                                                         |
| Has a shell? | yes                                                        | no                                                         |

Check the [tags history page](/chainguard/chainguard-images/reference/nginx/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                 | latest-dev | latest |
|---------------------------------|------------|--------|
| `apk-tools`                     | X          |        |
| `bash`                          | X          |        |
| `busybox`                       | X          |        |
| `ca-certificates-bundle`        | X          | X      |
| `git`                           | X          |        |
| `glibc`                         | X          | X      |
| `glibc-locale-posix`            | X          | X      |
| `ld-linux`                      | X          | X      |
| `libbrotlicommon1`              | X          |        |
| `libbrotlidec1`                 | X          |        |
| `libcrypt1`                     | X          | X      |
| `libcrypto3`                    | X          | X      |
| `libcurl-openssl4`              | X          |        |
| `libexpat1`                     | X          |        |
| `libgcc`                        | X          | X      |
| `libidn2`                       | X          |        |
| `libnghttp2-14`                 | X          |        |
| `libpcre2-8-0`                  | X          |        |
| `libpsl`                        | X          |        |
| `libssl3`                       | X          | X      |
| `libstdc++`                     | X          | X      |
| `libunistring`                  | X          |        |
| `ncurses`                       | X          |        |
| `ncurses-terminfo-base`         | X          |        |
| `nginx-mainline`                | X          | X      |
| `nginx-mainline-config`         | X          | X      |
| `nginx-mainline-package-config` | X          | X      |
| `openssl-config`                | X          | X      |
| `pcre`                          | X          | X      |
| `wolfi-baselayout`              | X          | X      |
| `zlib`                          | X          | X      |

