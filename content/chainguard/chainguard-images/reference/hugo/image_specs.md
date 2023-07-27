---
title: "Hugo Image Variants"
type: "article"
description: "Detailed information about the HugoChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Hugo"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Hugo** Image.

## Variants Compared
The **hugo** Chainguard Image currently has 4 public variants: 

- `latest`
- `latest-dev`
- `12`
- `12-dev`

The table has detailed information about each of these variants.

|              | latest          | latest-dev      | 12              | 12-dev          |
|--------------|-----------------|-----------------|-----------------|-----------------|
| Default User | `nonroot`       | `nonroot`       | `nonroot`       | `nonroot`       |
| Entrypoint   | `/usr/bin/hugo` | `/usr/bin/hugo` | `/usr/bin/hugo` | `/usr/bin/hugo` |
| CMD          | not specified   | not specified   | not specified   | not specified   |
| Workdir      | `/hugo`         | `/hugo`         | `/hugo`         | `/hugo`         |
| Has apk?     | no              | yes             | no              | yes             |
| Has a shell? | no              | yes             | no              | yes             |

Check the [tags history page](/chainguard/chainguard-images/reference/hugo/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|        | latest | latest-dev | 12 | 12-dev |
|--------|--------|------------|----|--------|
| `hugo` | X      | X          | X  | X      |
