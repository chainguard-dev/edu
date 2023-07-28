---
title: "Busybox Image Variants"
type: "article"
description: "Detailed information about the Busybox Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Busybox"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Busybox** Image.

## Variants Compared
The **busybox** Chainguard Image currently has 4 public variants: 

- `latest.wolfi`
- `latest.wolfi-dev`
- `latest.alpine`
- `latest.alpine-dev`

## Default Image Settings
`USER`:		`nonroot`

`WORKDIR`:	not specified

`ENTRYPOINT`:	not specified

`CMD`:		not specified

The following table has additional information about each of these variants.

|              | latest.wolfi | latest.wolfi-dev | latest.alpine | latest.alpine-dev |
|--------------|--------------|------------------|---------------|-------------------|
| Has apk?     | no           | yes              | no            | yes               |
| Has a shell? | yes          | yes              | yes           | yes               |

Check the [tags history page](/chainguard/chainguard-images/reference/busybox/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|              | latest.wolfi | latest.wolfi-dev | latest.alpine | latest.alpine-dev |
|--------------|--------------|------------------|---------------|-------------------|
| `busybox`    | X            | X                | X             | X                 |
| `ssl_client` |              |                  | X             | X                 |
