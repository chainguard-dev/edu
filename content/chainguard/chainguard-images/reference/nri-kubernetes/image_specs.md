---
title: "Nri-kubernetes Image Variants"
type: "article"
description: "Detailed information about the Nri-kubernetesChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Nri-kubernetes"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Nri-kubernetes** Image.

## Variants Compared
The **nri-kubernetes** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                                  | latest-dev                              |
|--------------|-----------------------------------------|-----------------------------------------|
| Default User | `nri`                                   | `nri`                                   |
| Entrypoint   | `/sbin/tini -- /usr/bin/nri-kubernetes` | `/sbin/tini -- /usr/bin/nri-kubernetes` |
| CMD          | not specified                           | not specified                           |
| Workdir      | not specified                           | not specified                           |
| Has apk?     | no                                      | no                                      |
| Has a shell? | yes                                     | yes                                     |

Check the [tags history page](/chainguard/chainguard-images/reference/nri-kubernetes/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `ca-certificates-bundle` | X      | X          |
| `busybox`                | X      | X          |
| `nri-kubernetes`         | X      | X          |
| `wolfi-baselayout`       | X      | X          |
| `bind-tools`             | X      | X          |
| `tini`                   | X      | X          |
