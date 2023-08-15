---
title: "mdbook Image Variants"
type: "article"
description: "Detailed information about the public mdbook Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "mdbook"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **mdbook** Image.

## Variants Compared
The **mdbook** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest            |
|--------------|-------------------|
| Default User | `nonroot`         |
| Entrypoint   | `/usr/bin/mdbook` |
| CMD          | `--help`          |
| Workdir      | not specified     |
| Has apk?     | no                |
| Has a shell? | no                |

Check the [tags history page](/chainguard/chainguard-images/reference/mdbook/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest |
|--------------------------|--------|
| `ca-certificates-bundle` | X      |
| `glibc`                  | X      |
| `glibc-locale-posix`     | X      |
| `ld-linux`               | X      |
| `libgcc`                 | X      |
| `mdbook`                 | X      |
| `wolfi-baselayout`       | X      |
