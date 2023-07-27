---
title: "Python Image Variants"
type: "article"
description: "Detailed information about the PythonChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Python"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Python** Image.

## Variants Compared
The **python** Chainguard Image currently has 6 public variants: 

- `latest`
- `latest-dev`
- `3.11`
- `3.11-dev`
- `3.10`
- `3.10-dev`

The table has detailed information about each of these variants.

|              | latest            | latest-dev        | 3.11              | 3.11-dev          | 3.10              | 3.10-dev          |
|--------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
| Default User | `nonroot`         | `nonroot`         | `nonroot`         | `nonroot`         | `nonroot`         | `nonroot`         |
| Entrypoint   | `/usr/bin/python` | `/usr/bin/python` | `/usr/bin/python` | `/usr/bin/python` | `/usr/bin/python` | `/usr/bin/python` |
| CMD          | not specified     | not specified     | not specified     | not specified     | not specified     | not specified     |
| Workdir      | not specified     | not specified     | not specified     | not specified     | not specified     | not specified     |
| Has apk?     | no                | yes               | no                | yes               | no                | yes               |
| Has a shell? | no                | yes               | no                | yes               | no                | yes               |

Check the [tags history page](/chainguard/chainguard-images/reference/python/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|               | latest | latest-dev | 3.11 | 3.11-dev | 3.10 | 3.10-dev |
|---------------|--------|------------|------|----------|------|----------|
| `python-3.11` | X      | X          | X    | X        |      |          |
| `python-3.10` |        |            |      |          | X    | X        |
