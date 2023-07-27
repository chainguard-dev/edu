---
title: "Secrets-store-csi-driver Image Variants"
type: "article"
description: "Detailed information about the Secrets-store-csi-driverChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Secrets-store-csi-driver"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Secrets-store-csi-driver** Image.

## Variants Compared
The **secrets-store-csi-driver** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                       | latest-dev                   |
|--------------|------------------------------|------------------------------|
| Default User | `root`                       | `root`                       |
| Entrypoint   | `/usr/bin/secrets-store-csi` | `/usr/bin/secrets-store-csi` |
| CMD          | not specified                | not specified                |
| Workdir      | not specified                | not specified                |
| Has apk?     | no                           | yes                          |
| Has a shell? | no                           | yes                          |

Check the [tags history page](/chainguard/chainguard-images/reference/secrets-store-csi-driver/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                            | latest | latest-dev |
|----------------------------|--------|------------|
| `secrets-store-csi-driver` | X      | X          |
| `mount`                    | X      | X          |
