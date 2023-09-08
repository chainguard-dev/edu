---
title: "kube-bench Image Variants"
type: "article"
description: "Detailed information about the public kube-bench Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "kube-bench"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **kube-bench** Image.

## Variants Compared
The **kube-bench** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                |
|--------------|-----------------------|
| Default User | `0`                   |
| Entrypoint   | `/usr/bin/kube-bench` |
| CMD          | `help`                |
| Workdir      | `/etc/kube-bench`     |
| Has apk?     | no                    |
| Has a shell? | no                    |

Check the [tags history page](/chainguard/chainguard-images/reference/kube-bench/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest |
|--------------------------|--------|
| `ca-certificates-bundle` | X      |
| `glibc`                  | X      |
| `glibc-locale-posix`     | X      |
| `kube-bench`             | X      |
| `kube-bench-configs`     | X      |
| `kubectl-1.28`           | X      |
| `ld-linux`               | X      |
| `libproc-2-0`            | X      |
| `ncurses`                | X      |
| `ncurses-terminfo-base`  | X      |
| `procps`                 | X      |
| `wolfi-baselayout`       | X      |
