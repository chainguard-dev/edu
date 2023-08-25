---
title: "mariadb Image Variants"
type: "article"
description: "Detailed information about the public mariadb Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "mariadb"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **mariadb** Image.

## Variants Compared
The **mariadb** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                                         |
|--------------|------------------------------------------------|
| Default User | `mysql`                                        |
| Entrypoint   | `/usr/local/bin/docker-entrypoint.sh mariadbd` |
| CMD          | not specified                                  |
| Workdir      | not specified                                  |
| Has apk?     | no                                             |
| Has a shell? | yes                                            |

Check the [tags history page](/chainguard/chainguard-images/reference/mariadb/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                                | latest |
|--------------------------------|--------|
| `bash`                         | X      |
| `busybox`                      | X      |
| `ca-certificates-bundle`       | X      |
| `glibc`                        | X      |
| `glibc-locale-posix`           | X      |
| `ld-linux`                     | X      |
| `libaio`                       | X      |
| `libcrypt1`                    | X      |
| `libcrypto3`                   | X      |
| `libgcc`                       | X      |
| `libpcre2-8-0`                 | X      |
| `libssl3`                      | X      |
| `libstdc++`                    | X      |
| `linux-pam`                    | X      |
| `mariadb-10.11`                | X      |
| `mariadb-10.11-oci-entrypoint` | X      |
| `ncurses`                      | X      |
| `ncurses-terminfo-base`        | X      |
| `openssl-config`               | X      |
| `pwgen`                        | X      |
| `tzdata`                       | X      |
| `wolfi-baselayout`             | X      |
| `xz`                           | X      |
| `zlib`                         | X      |

