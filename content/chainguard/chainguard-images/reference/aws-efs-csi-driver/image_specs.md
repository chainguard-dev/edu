---
title: "Aws-efs-csi-driver Image Variants"
type: "article"
description: "Detailed information about the Aws-efs-csi-driverChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Aws-efs-csi-driver"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Aws-efs-csi-driver** Image.

## Variants Compared
The **aws-efs-csi-driver** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest               | latest-dev           |
|--------------|----------------------|----------------------|
| Default User | `nonroot`            | `nonroot`            |
| Entrypoint   | `aws-efs-csi-driver` | `aws-efs-csi-driver` |
| CMD          | not specified        | not specified        |
| Workdir      | not specified        | not specified        |
| Has apk?     | no                   | no                   |
| Has a shell? | no                   | no                   |

Check the [tags history page](/chainguard/chainguard-images/reference/aws-efs-csi-driver/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `ca-certificates-bundle` | X      | X          |
| `aws-efs-csi-driver`     | X      | X          |
| `wolfi-baselayout`       | X      | X          |
