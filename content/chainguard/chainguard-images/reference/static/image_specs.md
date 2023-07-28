---
title: "Static Image Variants"
type: "article"
description: "Detailed information about the Static Chainguard Image variants"
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

## Default Image Settings
`USER`:		`nonroot`

`WORKDIR`:	not specified

`ENTRYPOINT`:	not specified

`CMD`:		not specified

The following table has additional information about each of these variants.

|              | latest | latest-dev | wolfi | wolfi-dev | alpine | alpine-dev |
|--------------|--------|------------|-------|-----------|--------|------------|
| Has apk?     | no     | yes        | no    | yes       | no     | yes        |
| Has a shell? | no     | yes        | no    | yes       | no     | yes        |

Check the [tags history page](/chainguard/chainguard-images/reference/static/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|          | latest | latest-dev | wolfi | wolfi-dev | alpine | alpine-dev |
|----------|--------|------------|-------|-----------|--------|------------|
| `tzdata` | X      | X          | X     | X         | X      | X          |
