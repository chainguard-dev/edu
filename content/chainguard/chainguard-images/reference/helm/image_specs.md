---
title: "Helm Image Variants"
type: "article"
description: "Detailed information about the HelmChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Helm"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Helm** Image.

## Variants Compared
The **helm** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest          | latest-dev      |
|--------------|-----------------|-----------------|
| Default User | `nonroot`       | `nonroot`       |
| Entrypoint   | `/usr/bin/helm` | `/usr/bin/helm` |
| CMD          | `help`          | `help`          |
| Workdir      | not specified   | not specified   |
| Has apk?     | no              | no              |
| Has a shell? | no              | no              |

Check the [tags history page](/chainguard/chainguard-images/reference/helm/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `ca-certificates-bundle` | X      | X          |
| `helm`                   | X      | X          |
| `wolfi-baselayout`       | X      | X          |
| `kubectl`                | X      | X          |
