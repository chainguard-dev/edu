---
title: "Melange Image Variants"
type: "article"
description: "Detailed information about the Melange Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Melange"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Melange** Image.

## Variants Compared
The **melange** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

## Default Image Settings
`USER`:		`root`

`WORKDIR`:	`/work`

`ENTRYPOINT`:	`/usr/bin/melange`

`CMD`:		`--help`

The following table has additional information about each of these variants.

|              | latest | latest-dev |
|--------------|--------|------------|
| Has apk?     | yes    | yes        |
| Has a shell? | yes    | yes        |

Check the [tags history page](/chainguard/chainguard-images/reference/melange/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|               | latest | latest-dev |
|---------------|--------|------------|
| `alpine-keys` | X      | X          |
| `wolfi-base`  | X      | X          |
| `bubblewrap`  | X      | X          |
| `melange`     | X      | X          |
