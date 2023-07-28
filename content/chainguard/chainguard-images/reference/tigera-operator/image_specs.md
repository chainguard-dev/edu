---
title: "Tigera-operator Image Variants"
type: "article"
description: "Detailed information about the Tigera-operator Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Tigera-operator"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Tigera-operator** Image.

## Variants Compared
The **tigera-operator** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

## Default Image Settings
`USER`:		`tigera-operator`

`WORKDIR`:	not specified

`ENTRYPOINT`:	`/usr/bin/operator`

`CMD`:		`--help`

The following table has additional information about each of these variants.

|              | latest | latest-dev |
|--------------|--------|------------|
| Has apk?     | no     | yes        |
| Has a shell? | no     | yes        |

Check the [tags history page](/chainguard/chainguard-images/reference/tigera-operator/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                   | latest | latest-dev |
|-------------------|--------|------------|
| `tigera-operator` | X      | X          |
| `glibc`           | X      | X          |
