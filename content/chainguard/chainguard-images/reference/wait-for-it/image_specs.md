---
title: "Wait-for-it Image Variants"
type: "article"
description: "Detailed information about the Wait-for-itChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Wait-for-it"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Wait-for-it** Image.

## Variants Compared
The **wait-for-it** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                 | latest-dev             |
|--------------|------------------------|------------------------|
| Default User | `nonroot`              | `nonroot`              |
| Entrypoint   | `/usr/bin/wait-for-it` | `/usr/bin/wait-for-it` |
| CMD          | not specified          | not specified          |
| Workdir      | not specified          | not specified          |
| Has apk?     | no                     | yes                    |
| Has a shell? | no                     | yes                    |

Check the [tags history page](/chainguard/chainguard-images/reference/wait-for-it/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|               | latest | latest-dev |
|---------------|--------|------------|
| `wait-for-it` | X      | X          |
