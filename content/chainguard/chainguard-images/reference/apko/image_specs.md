---
title: "Apko Image Variants"
type: "article"
description: "Detailed information about the ApkoChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Apko"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Apko** Image.

## Variants Compared
The **apko** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest          | latest-dev      |
|--------------|-----------------|-----------------|
| Default User | `root`          | `root`          |
| Entrypoint   | `/usr/bin/apko` | `/usr/bin/apko` |
| CMD          | `--help`        | `--help`        |
| Workdir      | `/work`         | `/work`         |
| Has apk?     | yes             | yes             |
| Has a shell? | yes             | yes             |

Check the [tags history page](/chainguard/chainguard-images/reference/apko/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|               | latest | latest-dev |
|---------------|--------|------------|
| `wolfi-base`  | X      | X          |
| `alpine-keys` | X      | X          |
| `apko`        | X      | X          |
