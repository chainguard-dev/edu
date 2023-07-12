---
title: "Image Overview: Secrets-store-csi-driver"
type: "article"
description: "Overview: Secrets-store-csi-driver Chainguard Image"
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

[cgr.dev/chainguard/secrets-store-csi-driver](https://github.com/chainguard-images/images/tree/main/images/secrets-store-csi-driver)

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest`     | 19 hours ago | `sha256:e833fa20f464257f3a2f102d421977c3e92d66d4a447407870ee684ae5855a3f` |
| `latest-dev` | 19 hours ago | `sha256:b6357b71f4f92f33b710fa39e38ec0c54c744f98024fae85630c5ab6bf1b4dde` |



Minimal image with Kubernetes Secrets Store CSI Driver. **EXPERIMENTAL**

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/secrets-store-csi-driver:latest
```

## Using Kubernetes Secrets Store CSI Driver

The Chainguard Secrets Store CSI DRiver image contains the `secrets-store-csi-driver` binary and required utilities.

The driver typically requires a plugin to be installed and configured separately to run.
