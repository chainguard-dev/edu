---
title: "Kubernetes-csi-node-driver-registrar Image Variants"
type: "article"
description: "Detailed information about the Kubernetes-csi-node-driver-registrar Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Kubernetes-csi-node-driver-registrar"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Kubernetes-csi-node-driver-registrar** Image.

## Variants Compared
The **kubernetes-csi-node-driver-registrar** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                               | latest-dev                           |
|--------------|--------------------------------------|--------------------------------------|
| Default User | `nonroot`                            | `nonroot`                            |
| Entrypoint   | `/usr/bin/csi-node-driver-registrar` | `/usr/bin/csi-node-driver-registrar` |
| CMD          | not specified                        | not specified                        |
| Workdir      | not specified                        | not specified                        |
| Has apk?     | no                                   | yes                                  |
| Has a shell? | no                                   | yes                                  |

Check the [tags history page](/chainguard/chainguard-images/reference/kubernetes-csi-node-driver-registrar/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                                        | latest | latest-dev |
|----------------------------------------|--------|------------|
| `kubernetes-csi-node-driver-registrar` | X      | X          |
