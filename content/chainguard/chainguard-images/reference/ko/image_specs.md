---
title: "Ko Image Variants"
type: "article"
description: "Detailed information about the Ko Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Ko"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Ko** Image.

## Variants Compared
The **ko** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

## Default Image Settings
`USER`:		`nonroot`

`WORKDIR`:	not specified

`ENTRYPOINT`:	`/usr/bin/ko`

`CMD`:		not specified

The following table has additional information about each of these variants.

|              | latest | latest-dev |
|--------------|--------|------------|
| Has apk?     | no     | yes        |
| Has a shell? | yes    | yes        |

Check the [tags history page](/chainguard/chainguard-images/reference/ko/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|              | latest | latest-dev |
|--------------|--------|------------|
| `busybox`    | X      | X          |
| `build-base` | X      | X          |
| `go`         | X      | X          |
| `ko`         | X      | X          |
