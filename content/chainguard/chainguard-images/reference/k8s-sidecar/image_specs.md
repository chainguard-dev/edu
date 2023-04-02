---
title: "k8s-sidecar Image Variants"
type: "article"
description: "Detailed specs for k8s-sidecar Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "k8s-sidecar"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **k8s-sidecar** Image.

## Variants Compared
The **k8s-sidecar** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                                                         | latest-dev                                                     |
|--------------|----------------------------------------------------------------|----------------------------------------------------------------|
| Default User | `k8s-sidecar`                                                  | `k8s-sidecar`                                                  |
| Entrypoint   | `/usr/share/app/.venv/bin/python -u /usr/share/app/sidecar.py` | `/usr/share/app/.venv/bin/python -u /usr/share/app/sidecar.py` |
| CMD          | not specified                                                  | not specified                                                  |
| Workdir      | not specified                                                  | not specified                                                  |
| Has apk?     | no                                                             | yes                                                            |
| Has a shell? | yes                                                            | yes                                                            |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `ca-certificates-bundle` | X      | X          |
| `wolfi-baselayout`       | X      | X          |
| `k8s-sidecar`            | X      | X          |
| `busybox`                | X      | X          |
| `apk-tools`              |        | X          |
| `bash`                   |        | X          |
| `git`                    |        | X          |

