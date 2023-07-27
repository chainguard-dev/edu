---
title: "Clang Image Variants"
type: "article"
description: "Detailed information about the Clang Chainguard Image variants"
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
The **clang** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest           | latest-dev       |
|--------------|------------------|------------------|
| Default User | `root`           | `root`           |
| Entrypoint   | `/usr/bin/clang` | `/usr/bin/clang` |
| CMD          | `--help`         | `--help`         |
| Workdir      | `/work`          | `/work`          |
| Has apk?     | no               | yes              |
| Has a shell? | yes              | yes              |

Check the [tags history page](/chainguard/chainguard-images/reference/clang/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|              | latest | latest-dev |
|--------------|--------|------------|
| `build-base` | X      | X          |
| `busybox`    | X      | X          |
| `clang-15`   | X      | X          |
