---
title: "Vertical-pod-autoscaler-recommender Image Variants"
type: "article"
description: "Detailed information about the Vertical-pod-autoscaler-recommenderChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Vertical-pod-autoscaler-recommender"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Vertical-pod-autoscaler-recommender** Image.

## Variants Compared
The **vertical-pod-autoscaler-recommender** Chainguard Image currently has one public variant: 

- `latest`

The table has detailed information about each of these variants.

|              | latest                         |
|--------------|--------------------------------|
| Default User | `nonroot`                      |
| Entrypoint   | `/usr/bin/recommender`         |
| CMD          | `--v=4 --stderrthreshold=info` |
| Workdir      | not specified                  |
| Has apk?     | no                             |
| Has a shell? | no                             |

Check the [tags history page](/chainguard/chainguard-images/reference/vertical-pod-autoscaler-recommender/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                                       | latest |
|---------------------------------------|--------|
| `ca-certificates-bundle`              | X      |
| `vertical-pod-autoscaler-recommender` | X      |
