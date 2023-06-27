---
title: "Paranoia Image Variants"
type: "article"
description: "Detailed information about the ParanoiaChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Paranoia"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Paranoia** Image.

## Variants Compared
The **paranoia** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest              | latest-dev          |
|--------------|---------------------|---------------------|
| Default User | `nonroot`           | `nonroot`           |
| Entrypoint   | `/usr/bin/paranoia` | `/usr/bin/paranoia` |
| CMD          | not specified       | not specified       |
| Workdir      | not specified       | not specified       |
| Has apk?     | no                  | no                  |
| Has a shell? | no                  | no                  |

Check the [tags history page](/chainguard/chainguard-images/reference/paranoia/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `ca-certificates-bundle` | X      | X          |
| `wolfi-baselayout`       | X      | X          |
| `paranoia`               | X      | X          |
