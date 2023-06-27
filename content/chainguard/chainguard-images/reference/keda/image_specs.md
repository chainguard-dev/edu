---
title: "Keda Image Variants"
type: "article"
description: "Detailed information about the KedaChainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Keda"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Keda** Image.

## Variants Compared
The **keda** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                                                     | latest-dev                                                 |
|--------------|------------------------------------------------------------|------------------------------------------------------------|
| Default User | `nonroot`                                                  | `nonroot`                                                  |
| Entrypoint   | `/usr/bin/keda --zap-log-level=info --zap-encoder=console` | `/usr/bin/keda --zap-log-level=info --zap-encoder=console` |
| CMD          | not specified                                              | not specified                                              |
| Workdir      | not specified                                              | not specified                                              |
| Has apk?     | no                                                         | no                                                         |
| Has a shell? | yes                                                        | yes                                                        |

Check the [tags history page](/chainguard/chainguard-images/reference/keda/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                          | latest | latest-dev |
|--------------------------|--------|------------|
| `ca-certificates-bundle` | X      | X          |
| `busybox`                | X      | X          |
| `keda`                   | X      | X          |
| `keda-compat`            | X      | X          |
| `wolfi-baselayout`       | X      | X          |
