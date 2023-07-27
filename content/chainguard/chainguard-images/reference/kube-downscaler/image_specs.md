---
title: "Kube-downscaler Image Variants"
type: "article"
description: "Detailed information about the Kube-downscalerChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Kube-downscaler"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Kube-downscaler** Image.

## Variants Compared
The **kube-downscaler** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                       | latest-dev                   |
|--------------|------------------------------|------------------------------|
| Default User | `nonroot`                    | `nonroot`                    |
| Entrypoint   | `python3 -m kube_downscaler` | `python3 -m kube_downscaler` |
| CMD          | not specified                | not specified                |
| Workdir      | not specified                | not specified                |
| Has apk?     | no                           | yes                          |
| Has a shell? | no                           | yes                          |

Check the [tags history page](/chainguard/chainguard-images/reference/kube-downscaler/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                   | latest | latest-dev |
|-------------------|--------|------------|
| `python3`         | X      | X          |
| `kube-downscaler` | X      | X          |
