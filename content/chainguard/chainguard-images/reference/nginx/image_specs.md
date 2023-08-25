---
title: "nginx Image Variants"
type: "article"
description: "Detailed information about the public nginx Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "nginx"
weight: 550
toc: true
---

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

|                          | latest-dev | latest |
|--------------------------|------------|--------|
| `apk-tools`              | X          |        |
| `bash`                   | X          |        |
| `busybox`                | X          |        |
| `ca-certificates-bundle` | X          | X      |
| `git`                    | X          |        |
| `glibc`                  | X          | X      |
| `glibc-locale-posix`     | X          | X      |
| `ld-linux`               | X          | X      |
| `libbrotlicommon1`       | X          |        |
| `libbrotlidec1`          | X          |        |
| `libcrypt1`              | X          | X      |
| `libcrypto3`             | X          | X      |
| `libcurl-openssl4`       | X          |        |
| `libexpat1`              | X          |        |
| `libgcc`                 | X          | X      |
| `libnghttp2-14`          | X          |        |
| `libpcre2-8-0`           | X          |        |
| `libssl3`                | X          | X      |
| `libstdc++`              | X          | X      |
| `ncurses`                | X          |        |
| `ncurses-terminfo-base`  | X          |        |
| `nginx`                  | X          | X      |
| `nginx-package-config`   | X          | X      |
| `openssl-config`         | X          | X      |
| `pcre`                   | X          | X      |
| `wolfi-baselayout`       | X          | X      |
| `zlib`                   | X          | X      |

