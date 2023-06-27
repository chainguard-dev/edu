---
title: "Skaffold Image Variants"
type: "article"
description: "Detailed information about the SkaffoldChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Skaffold"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Skaffold** Image.

## Variants Compared
The **skaffold** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest              | latest-dev          |
|--------------|---------------------|---------------------|
| Default User | `skaffold`          | `skaffold`          |
| Entrypoint   | `/usr/bin/skaffold` | `/usr/bin/skaffold` |
| CMD          | `--help`            | `--help`            |
| Workdir      | `/app`              | `/app`              |
| Has apk?     | no                  | no                  |
| Has a shell? | no                  | no                  |

Check the [tags history page](/chainguard/chainguard-images/reference/skaffold/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                    | latest | latest-dev |
|--------------------|--------|------------|
| `skaffold`         | X      | X          |
| `google-cloud-sdk` | X      | X          |
| `wolfi-baselayout` | X      | X          |
| `helm`             | X      | X          |
| `kustomize`        | X      | X          |
| `kpt`              | X      | X          |
