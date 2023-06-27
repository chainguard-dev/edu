---
title: "Clang Image Variants"
type: "article"
description: "Detailed information about the ClangChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Clang"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Clang** Image.

## Variants Compared
The **clang** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest           |
|--------------|------------------|
| Default User | `root`           |
| Entrypoint   | `/usr/bin/clang` |
| CMD          | `--help`         |
| Workdir      | `/work`          |
| Has apk?     | no               |
| Has a shell? | yes              |

Check the [tags history page](/chainguard/chainguard-images/reference/clang/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | latest |
|--------------------------|--------|
| `ca-certificates-bundle` | X      |
| `build-base`             | X      |
| `busybox`                | X      |
| `clang-15`               | X      |
