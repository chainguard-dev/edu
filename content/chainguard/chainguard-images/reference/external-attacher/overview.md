---
title: "Image Overview: external-attacher"
type: "article"
description: "Overview: external-attacher Chainguard Images"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "images-reference"
weight: 500
toc: true
---

`stable` [cgr.dev/chainguard/external-attacher](https://github.com/chainguard-images/images/tree/main/images/external-attacher)
| Tags         | Aliases                                         |
|--------------|-------------------------------------------------|
| `latest`     | `4`, `4.3`, `4.3.0`, `4.3.0-r0`                 |
| `latest-dev` | `4-dev`, `4.3-dev`, `4.3.0-dev`, `4.3.0-r0-dev` |



Minimal image with [kubernetes-csi/external-attacher](https://github.com/kubernetes-csi/external-attacher).

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/external-attacher:latest
```

## Using external-attacher

The Chainguard external-attacher image contains the `csi-attacher` controller and is a drop-in replacement for the upstream image.

To try it out, follow the [official installation
instructions](https://github.com/kubernetes-csi/external-attacher/blob/master/README.md#usage).

