---
title: "Deno Public Image Variants"
type: "article"
description: "Detailed information about the public Deno Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Deno"
weight: 550
toc: true
---

This page shows detailed information about all public variants of the Chainguard **Deno** Image.

## Variants Compared
The **deno** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest          |
|--------------|-----------------|
| Default User | `deno`          |
| Entrypoint   | `/usr/bin/deno` |
| CMD          | `--help`        |
| Workdir      | `/app`          |
| Has apk?     | no              |
| Has a shell? | no              |

Check the [tags history page](/chainguard/chainguard-images/reference/deno/tags_history/) for the full list of available tags.

## Packages Included
The table shows package distribution across variants.

|                          | latest |
|--------------------------|--------|
| `ca-certificates-bundle` | X      |
| `deno`                   | X      |
| `glibc`                  | X      |
| `glibc-locale-posix`     | X      |
| `ld-linux`               | X      |
| `libgcc`                 | X      |
| `wolfi-baselayout`       | X      |
