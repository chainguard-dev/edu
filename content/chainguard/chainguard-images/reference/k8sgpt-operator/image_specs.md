---
title: "k8sgpt-operator Image Variants"
type: "article"
description: "Detailed specs for k8sgpt-operator Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "k8sgpt-operator"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **k8sgpt-operator** Image.

## Variants Compared
The **k8sgpt-operator** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest        | latest-dev    |
|--------------|---------------|---------------|
| Default User | `nonroot`     | `nonroot`     |
| Entrypoint   | `manager`     | `manager`     |
| CMD          | not specified | not specified |
| Workdir      | not specified | not specified |
| Has apk?     | no            | yes           |
| Has a shell? | no            | yes           |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `ca-certificates-bundle` | X      | X          |
| `wolfi-baselayout`       | X      | X          |
| `k8sgpt-operator`        | X      | X          |
| `apk-tools`              |        | X          |
| `bash`                   |        | X          |
| `busybox`                |        | X          |
| `git`                    |        | X          |

