---
title: "Kube-fluentd-operator Image Variants"
type: "article"
description: "Detailed information about the Kube-fluentd-operator Chainguard Image variants"
date: 2023-03-07T11:07:52+02:00
lastmod: 2023-03-07T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "Kube-fluentd-operator"
weight: 550
toc: true
---

This page shows detailed information about all available variants of the Chainguard **Kube-fluentd-operator** Image.

## Variants Compared
The **kube-fluentd-operator** Chainguard Image currently has 2 public variants: 

- `latest`
- `latest-dev`

The table has detailed information about each of these variants.

|              | latest                   | latest-dev               |
|--------------|--------------------------|--------------------------|
| Default User | `root`                   | `root`                   |
| Entrypoint   | `/fluentd/entrypoint.sh` | `/fluentd/entrypoint.sh` |
| CMD          | not specified            | not specified            |
| Workdir      | not specified            | not specified            |
| Has apk?     | no                       | yes                      |
| Has a shell? | no                       | yes                      |

Check the [tags history page](/chainguard/chainguard-images/reference/kube-fluentd-operator/tags_history/) for the full list of available tags.
## Image Dependencies
The table shows package distribution across all variants.

|                                        | latest | latest-dev |
|----------------------------------------|--------|------------|
| `kube-fluentd-operator`                | X      | X          |
| `kube-fluentd-operator-oci-entrypoint` | X      | X          |
| `kube-fluentd-operator-default-config` | X      | X          |
| `kube-fluentd-operator-compat`         | X      | X          |
