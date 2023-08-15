---
title: "Calico-typha Public Image Variants"
type: "article"
description: "Detailed information about the public Calico-typha Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Calico-typha"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **Calico-typha** Image.

## Variants Compared
The **calico-typha** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                  |
|--------------|-------------------------|
| Default User | `nonroot`               |
| Entrypoint   | `/sbin/tini --`         |
| CMD          | `/usr/bin/calico-typha` |
| Workdir      | not specified           |
| Has apk?     | no                      |
| Has a shell? | no                      |

Check the [tags history page](/chainguard/chainguard-images/reference/calico-typha/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest |
|--------------------------|--------|
| `ca-certificates-bundle` | X      |
| `calico-typhad`          | X      |
| `glibc`                  | X      |
| `glibc-locale-posix`     | X      |
| `ld-linux`               | X      |
| `tini`                   | X      |
| `wolfi-baselayout`       | X      |
