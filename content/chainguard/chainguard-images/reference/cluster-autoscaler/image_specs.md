---
title: "Cluster-autoscaler Image Variants"
type: "article"
description: "Detailed information about the Cluster-autoscalerChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Cluster-autoscaler"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Cluster-autoscaler** Image.

## Variants Compared
The **cluster-autoscaler** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                        | latest-dev                    |
|--------------|-------------------------------|-------------------------------|
| Default User | `cluster-autoscaler`          | `cluster-autoscaler`          |
| Entrypoint   | `/usr/bin/cluster-autoscaler` | `/usr/bin/cluster-autoscaler` |
| CMD          | not specified                 | not specified                 |
| Workdir      | `/`                           | `/`                           |
| Has apk?     | no                            | no                            |
| Has a shell? | no                            | no                            |

Check the [tags history page](/chainguard/chainguard-images/reference/cluster-autoscaler/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                             | latest | latest-dev |
|-----------------------------|--------|------------|
| `cluster-autoscaler`        | X      | X          |
| `cluster-autoscaler-compat` | X      | X          |
| `wolfi-baselayout`          | X      | X          |
| `ca-certificates-bundle`    | X      | X          |
