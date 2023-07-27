---
title: "Kube-bench Image Variants"
type: "article"
description: "Detailed information about the Kube-benchChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Kube-bench"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Kube-bench** Image.

## Variants Compared
The **kube-bench** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                | latest-dev            |
|--------------|-----------------------|-----------------------|
| Default User | `root`                | `root`                |
| Entrypoint   | `/usr/bin/kube-bench` | `/usr/bin/kube-bench` |
| CMD          | `help`                | `help`                |
| Workdir      | `/etc/kube-bench`     | `/etc/kube-bench`     |
| Has apk?     | no                    | yes                   |
| Has a shell? | no                    | yes                   |

Check the [tags history page](/chainguard/chainguard-images/reference/kube-bench/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                      | latest | latest-dev |
|----------------------|--------|------------|
| `procps`             | X      | X          |
| `kube-bench`         | X      | X          |
| `kube-bench-configs` | X      | X          |
