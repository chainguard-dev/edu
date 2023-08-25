---
title: "melange Image Variants"
type: "article"
description: "Detailed information about the public melange Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "melange"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **melange** Image.

## Variants Compared
The **melange** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest             |
|--------------|--------------------|
| Default User | `root`             |
| Entrypoint   | `/usr/bin/melange` |
| CMD          | `--help`           |
| Workdir      | `/work`            |
| Has apk?     | no                 |
| Has a shell? | yes                |

Check the [tags history page](/chainguard/chainguard-images/reference/melange/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest |
|--------------------------|--------|
| `alpine-keys`            | X      |
| `bubblewrap`             | X      |
| `busybox`                | X      |
| `ca-certificates-bundle` | X      |
| `glibc`                  | X      |
| `glibc-locale-posix`     | X      |
| `ld-linux`               | X      |
| `libcap`                 | X      |
| `libcrypt1`              | X      |
| `melange`                | X      |
| `wolfi-baselayout`       | X      |
| `wolfi-keys`             | X      |

