---
title: "Image Overview: secrets-store-csi-driver"
type: "article"
description: "Overview: secrets-store-csi-driver Chainguard Images"
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

`experimental` [cgr.dev/chainguard/secrets-store-csi-driver](https://github.com/chainguard-images/images/tree/main/images/secrets-store-csi-driver)
| Tags         | Aliases                                         |
|--------------|-------------------------------------------------|
| `latest`     | `1`, `1.3`, `1.3.4`, `1.3.4-r0`                 |
| `latest-dev` | `1-dev`, `1.3-dev`, `1.3.4-dev`, `1.3.4-r0-dev` |



Minimal image with Kubernetes Secrets Store CSI Driver. **EXPERIMENTAL**

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/secrets-store-csi-driver:latest
```

## Using Kubernetes Secrets Store CSI Driver

The Chainguard Secrets Store CSI DRiver image contains the `secrets-store-csi-driver` binary and required utilities.

The driver typically requires a plugin to be installed and configured separately to run.

