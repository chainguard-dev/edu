---
title: "netcat Image Variants"
type: "article"
description: "Detailed information about the public netcat Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "netcat"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **netcat** Image.

## Variants Compared
The **netcat** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest        |
|--------------|---------------|
| Default User | `nonroot`     |
| Entrypoint   | `/usr/bin/nc` |
| CMD          | `-h`          |
| Workdir      | `/home/nc`    |
| Has apk?     | no            |
| Has a shell? | yes           |

Check the [tags history page](/chainguard/chainguard-images/reference/netcat/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest |
|--------------------------|--------|
| `busybox`                | X      |
| `ca-certificates-bundle` | X      |
| `glibc`                  | X      |
| `glibc-locale-posix`     | X      |
| `ld-linux`               | X      |
| `libbsd`                 | X      |
| `libcrypt1`              | X      |
| `libmd`                  | X      |
| `netcat-openbsd`         | X      |
| `wolfi-baselayout`       | X      |

