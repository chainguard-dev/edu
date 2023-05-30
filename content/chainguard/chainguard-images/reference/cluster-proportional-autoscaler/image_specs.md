---
title: "cluster-proportional-autoscaler Image Variants"
type: "article"
description: "Detailed specs for cluster-proportional-autoscaler Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "cluster-proportional-autoscaler"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **cluster-proportional-autoscaler** Image.

## Variants Compared
The **cluster-proportional-autoscaler** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                                     | latest-dev                                 |
|--------------|--------------------------------------------|--------------------------------------------|
| Default User | `cluster-proportional-autoscaler`          | `cluster-proportional-autoscaler`          |
| Entrypoint   | `/usr/bin/cluster-proportional-autoscaler` | `/usr/bin/cluster-proportional-autoscaler` |
| CMD          | not specified                              | not specified                              |
| Workdir      | not specified                              | not specified                              |
| Has apk?     | no                                         | yes                                        |
| Has a shell? | no                                         | yes                                        |

## Image Dependencies
The table shows package distribution across all variants.

|                                   | latest | latest-dev |
|-----------------------------------|--------|------------|
| `wolfi-baselayout`                | X      | X          |
| `cluster-proportional-autoscaler` | X      | X          |
| `ca-certificates-bundle`          | X      | X          |
| `apk-tools`                       |        | X          |
| `bash`                            |        | X          |
| `busybox`                         |        | X          |
| `git`                             |        | X          |

