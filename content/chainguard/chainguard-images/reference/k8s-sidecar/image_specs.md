---
title: "K8s-sidecar Image Variants"
type: "article"
description: "Detailed information about the K8s-sidecar Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "K8s-sidecar"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **K8s-sidecar** Image.

## Variants Compared
The **k8s-sidecar** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

## Default Image Settings
`USER`:		`k8s-sidecar`

`WORKDIR`:	not specified

`ENTRYPOINT`:	`/usr/share/app/.venv/bin/python -u /usr/share/app/sidecar.py`

`CMD`:		not specified

The following table has additional information about each of these variants.

|              | latest | latest-dev |
|--------------|--------|------------|
| Has apk?     | no     | yes        |
| Has a shell? | yes    | yes        |

Check the [tags history page](/chainguard/chainguard-images/reference/k8s-sidecar/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|               | latest | latest-dev |
|---------------|--------|------------|
| `k8s-sidecar` | X      | X          |
| `busybox`     | X      | X          |
