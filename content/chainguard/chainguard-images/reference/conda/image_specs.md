---
title: "Conda Image Variants"
type: "article"
description: "Detailed information about the Conda Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Conda"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Conda** Image.

## Variants Compared
The **conda** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                 | latest-dev             |
|--------------|------------------------|------------------------|
| Default User | `nonroot`              | `nonroot`              |
| Entrypoint   | `/opt/conda/bin/conda` | `/opt/conda/bin/conda` |
| CMD          | `--help`               | `--help`               |
| Workdir      | not specified          | not specified          |
| Has apk?     | no                     | yes                    |
| Has a shell? | yes                    | yes                    |

Check the [tags history page](/chainguard/chainguard-images/reference/conda/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|           | latest | latest-dev |
|-----------|--------|------------|
| `conda`   | X      | X          |
| `busybox` | X      | X          |
