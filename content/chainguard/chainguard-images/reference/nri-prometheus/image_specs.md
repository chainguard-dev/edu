---
title: "nri-prometheus Image Variants"
type: "article"
description: "Detailed specs for nri-prometheus Chainguard Image Variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "nri-prometheus"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **nri-prometheus** Image.

## Variants Compared
The **nri-prometheus** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                                  | latest-dev                              |
|--------------|-----------------------------------------|-----------------------------------------|
| Default User | `nonroot`                               | `nonroot`                               |
| Entrypoint   | `/sbin/tini -- /usr/bin/nri-prometheus` | `/sbin/tini -- /usr/bin/nri-prometheus` |
| CMD          | not specified                           | not specified                           |
| Workdir      | not specified                           | not specified                           |
| Has apk?     | no                                      | yes                                     |
| Has a shell? | yes                                     | yes                                     |

## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `ca-certificates-bundle` | X      | X          |
| `busybox`                | X      | X          |
| `nri-prometheus`         | X      | X          |
| `wolfi-baselayout`       | X      | X          |
| `bind-tools`             | X      | X          |
| `tini`                   | X      | X          |
| `apk-tools`              |        | X          |
| `bash`                   |        | X          |
| `git`                    |        | X          |

