---
title: "Powershell Image Variants"
type: "article"
description: "Detailed information about the Powershell Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Powershell"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Powershell** Image.

## Variants Compared
The **powershell** Chainguard Image currently has 4 public variants: 

- `latest`
- `latest-dev`
- `latest-root`
- `latest-root-dev`

## Default Image Settings
`USER`:		`root`

`WORKDIR`:	not specified

`ENTRYPOINT`:	`/usr/bin/pwsh`

`CMD`:		not specified

The following table has additional information about each of these variants.

|              | latest | latest-dev | latest-root | latest-root-dev |
|--------------|--------|------------|-------------|-----------------|
| Has apk?     | no     | yes        | no          | yes             |
| Has a shell? | yes    | yes        | yes         | yes             |

Check the [tags history page](/chainguard/chainguard-images/reference/powershell/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|              | latest | latest-dev | latest-root | latest-root-dev |
|--------------|--------|------------|-------------|-----------------|
| `busybox`    | X      | X          | X           | X               |
| `powershell` | X      | X          | X           | X               |
