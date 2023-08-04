---
title: "Image Overview: secrets-store-csi-driver"
type: "article"
description: "Overview: secrets-store-csi-driver Chainguard Image"
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

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | August 3rd   | `sha256:dd3d9dc98467d406f7238f0b9408fa926025079cffc43d88a24f00d0d4e8b368` |
|  `latest-dev` | August 3rd   | `sha256:7bf8557ada815c195bf0cb124bfecc2939133d8c5a37e557a07eb603ff6a30ec` |



Minimal image with Kubernetes Secrets Store CSI Driver. **EXPERIMENTAL**

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/secrets-store-csi-driver:latest
```

## Using Kubernetes Secrets Store CSI Driver

The Chainguard Secrets Store CSI DRiver image contains the `secrets-store-csi-driver` binary and required utilities.

The driver typically requires a plugin to be installed and configured separately to run.

