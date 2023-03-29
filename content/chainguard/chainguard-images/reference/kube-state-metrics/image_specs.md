---
title: "kube-state-metrics Image Variants"
type: "article"
description: "Detailed specs for kube-state-metrics Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "kube-state-metrics"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **kube-state-metrics** Image.

## Variants Compared
The **kube-state-metrics** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                        | latest-dev                    |
|--------------|-------------------------------|-------------------------------|
| Default User | `kube-state-metrics`          | `kube-state-metrics`          |
| Entrypoint   | `/usr/bin/kube-state-metrics` | `/usr/bin/kube-state-metrics` |
| CMD          | not specified                 | not specified                 |
| Workdir      | not specified                 | not specified                 |
| Has apk?     | no                            | yes                           |
| Has a shell? | yes                           | yes                           |

## Image Dependencies
The table shows package distribution across all variants.

|                      | latest | latest-dev |
|----------------------|--------|------------|
| `kube-state-metrics` | X      | X          |
| `wolfi-baselayout`   | X      | X          |
| `busybox`            | X      | X          |
| `apk-tools`          |        | X          |
| `bash`               |        | X          |
| `git`                |        | X          |
