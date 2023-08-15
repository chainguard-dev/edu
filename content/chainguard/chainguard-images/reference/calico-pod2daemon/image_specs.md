---
title: "Calico-pod2daemon Public Image Variants"
type: "article"
description: "Detailed information about the public Calico-pod2daemon Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Calico-pod2daemon"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **Calico-pod2daemon** Image.

## Variants Compared
The **calico-pod2daemon** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                |
|--------------|-----------------------|
| Default User | `root`                |
| Entrypoint   | `/usr/bin/flexvol.sh` |
| CMD          | not specified         |
| Workdir      | not specified         |
| Has apk?     | no                    |
| Has a shell? | yes                   |

Check the [tags history page](/chainguard/chainguard-images/reference/calico-pod2daemon/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest |
|--------------------------|--------|
| `busybox`                | X      |
| `ca-certificates-bundle` | X      |
| `calico-pod2daemon`      | X      |
| `glibc`                  | X      |
| `glibc-locale-posix`     | X      |
| `ld-linux`               | X      |
| `libcrypt1`              | X      |
| `wolfi-baselayout`       | X      |
