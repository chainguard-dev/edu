---
title: "K3s Image Variants"
type: "article"
description: "Detailed information about the K3s Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "K3s"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **K3s** Image.

## Variants Compared
The **k3s** Chainguard Image currently has 6 public variants: 

- `latest.images`
- `latest.images-dev`
- `latest.embedded`
- `latest.embedded-dev`
- `latest`
- `latest-dev`

## Default Image Settings
`USER`:		`root`

`WORKDIR`:	not specified

`ENTRYPOINT`:	`/bin/k3s`

`CMD`:		`agent`

The following table has additional information about each of these variants.

|              | latest.images | latest.images-dev | latest.embedded | latest.embedded-dev | latest | latest-dev |
|--------------|---------------|-------------------|-----------------|---------------------|--------|------------|
| Has apk?     | no            | yes               | no              | yes                 | no     | yes        |
| Has a shell? | no            | yes               | no              | yes                 | no     | yes        |

Check the [tags history page](/chainguard/chainguard-images/reference/k3s/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                              | latest.images | latest.images-dev | latest.embedded | latest.embedded-dev | latest | latest-dev |
|------------------------------|---------------|-------------------|-----------------|---------------------|--------|------------|
| `mount`                      | X             | X                 | X               | X                   | X      | X          |
| `umount`                     | X             | X                 | X               | X                   | X      | X          |
| `kmod`                       | X             | X                 | X               | X                   | X      | X          |
| `k3s`                        | X             | X                 |                 |                     | X      | X          |
| `k3s-images`                 | X             | X                 |                 |                     |        |            |
| `k3s-embedded`               |               |                   | X               | X                   |        |            |
| `fuse-overlayfs`             |               |                   |                 |                     | X      | X          |
| `fuse-overlayfs-snapshotter` |               |                   |                 |                     | X      | X          |
