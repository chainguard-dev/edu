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

| Tag (s)       | Last Changed   | Digest                                                                    |
|---------------|----------------|---------------------------------------------------------------------------|
|  `latest-dev` | September 11th | `sha256:3317a12183b68634650545a4bc0e8de1af9d765a9c6297a5f0f767af1b52beb6` |
|  `latest`     | September 11th | `sha256:c39eeb78dd1218a9535a8ddf9e3abb87aaa0f62687ef51d35649ab7c89d130fc` |



Minimal image with Kubernetes Secrets Store CSI Driver. **EXPERIMENTAL**

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/secrets-store-csi-driver:latest
```

## Using Kubernetes Secrets Store CSI Driver

The Chainguard Secrets Store CSI DRiver image contains the `secrets-store-csi-driver` binary and required utilities.

The driver typically requires a plugin to be installed and configured separately to run.

