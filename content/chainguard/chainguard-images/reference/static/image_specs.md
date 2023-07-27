---
title: "Static Image Variants"
type: "article"
description: "Detailed information about the StaticChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Static"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Static** Image.

## Variants Compared
The **static** Chainguard Image currently has 6 public variants: 

- `latest`
- `latest-dev`
- `wolfi`
- `wolfi-dev`
- `alpine`
- `alpine-dev`

The table has detailed information about each of these variants.

|              | latest        | latest-dev    | wolfi         | wolfi-dev     | alpine        | alpine-dev    |
|--------------|---------------|---------------|---------------|---------------|---------------|---------------|
| Default User | `nonroot`     | `nonroot`     | `nonroot`     | `nonroot`     | `nonroot`     | `nonroot`     |
| Entrypoint   | not specified | not specified | not specified | not specified | not specified | not specified |
| CMD          | not specified | not specified | not specified | not specified | not specified | not specified |
| Workdir      | not specified | not specified | not specified | not specified | not specified | not specified |
| Has apk?     | no            | yes           | no            | yes           | no            | yes           |
| Has a shell? | no            | yes           | no            | yes           | no            | yes           |

Check the [tags history page](/chainguard/chainguard-images/reference/static/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|          | latest | latest-dev | wolfi | wolfi-dev | alpine | alpine-dev |
|----------|--------|------------|-------|-----------|--------|------------|
| `tzdata` | X      | X          | X     | X         | X      | X          |
