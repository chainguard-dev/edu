---
title: "Image Overview: external-resizer"
type: "article"
description: "Overview: external-resizer Chainguard Images"
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

`stable` [cgr.dev/chainguard/external-resizer](https://github.com/chainguard-images/images/tree/main/images/external-resizer)
| Tags         | Aliases                                         |
|--------------|-------------------------------------------------|
| `latest`     | `1`, `1.8`, `1.8.0`, `1.8.0-r0`                 |
| `latest-dev` | `1-dev`, `1.8-dev`, `1.8.0-dev`, `1.8.0-r0-dev` |



Minimal image with [kubernetes-csi/external-resizer](https://github.com/kubernetes-csi/external-resizer).

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/external-resizer:latest
```

## Using external-resizer

The Chainguard external-resizer image contains the `csi-resizer` controller and is a drop-in replacement for the upstream image.

To try it out, follow the [official installation
instructions](https://github.com/kubernetes-csi/external-resizer/blob/master/README.md#usage).

