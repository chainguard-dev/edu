---
title: "Gcc-glibc Image Variants"
type: "article"
description: "Detailed information about the Gcc-glibc Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Gcc-glibc"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Gcc-glibc** Image.

## Variants Compared
The **gcc-glibc** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

## Default Image Settings
`USER`:		`root`

`WORKDIR`:	`/work`

`ENTRYPOINT`:	`/usr/bin/gcc`

`CMD`:		`--help`

The following table has additional information about each of these variants.

|              | latest | latest-dev |
|--------------|--------|------------|
| Has apk?     | no     | yes        |
| Has a shell? | yes    | yes        |

Check the [tags history page](/chainguard/chainguard-images/reference/gcc-glibc/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|              | latest | latest-dev |
|--------------|--------|------------|
| `build-base` | X      | X          |
| `busybox`    | X      | X          |
