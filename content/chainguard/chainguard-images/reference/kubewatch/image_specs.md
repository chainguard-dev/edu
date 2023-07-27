---
title: "Kubewatch Image Variants"
type: "article"
description: "Detailed information about the KubewatchChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Kubewatch"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Kubewatch** Image.

## Variants Compared
The **kubewatch** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest               | latest-dev           |
|--------------|----------------------|----------------------|
| Default User | `nonroot`            | `nonroot`            |
| Entrypoint   | `/usr/bin/kubewatch` | `/usr/bin/kubewatch` |
| CMD          | not specified        | not specified        |
| Workdir      | not specified        | not specified        |
| Has apk?     | no                   | yes                  |
| Has a shell? | no                   | yes                  |

Check the [tags history page](/chainguard/chainguard-images/reference/kubewatch/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|             | latest | latest-dev |
|-------------|--------|------------|
| `kubewatch` | X      | X          |
