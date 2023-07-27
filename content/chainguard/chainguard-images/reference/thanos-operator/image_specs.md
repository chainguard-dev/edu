---
title: "Thanos-operator Image Variants"
type: "article"
description: "Detailed information about the Thanos-operatorChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Thanos-operator"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Thanos-operator** Image.

## Variants Compared
The **thanos-operator** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest             | latest-dev         |
|--------------|--------------------|--------------------|
| Default User | `nonroot`          | `nonroot`          |
| Entrypoint   | `/usr/bin/manager` | `/usr/bin/manager` |
| CMD          | not specified      | not specified      |
| Workdir      | not specified      | not specified      |
| Has apk?     | no                 | yes                |
| Has a shell? | no                 | yes                |

Check the [tags history page](/chainguard/chainguard-images/reference/thanos-operator/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `thanos-operator`        | X      | X          |
| `thanos-operator-compat` | X      | X          |