---
title: "Image Overview: Kubernetes-csi-external-attacher"
type: "article"
description: "Overview: Kubernetes-csi-external-attacher Chainguard Image"
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

[cgr.dev/chainguard/kubernetes-csi-external-attacher](https://github.com/chainguard-images/images/tree/main/images/kubernetes-csi-external-attacher)

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest`     | 20 hours ago | `sha256:fa13036a968125fd4de35e5067980cc4b48c6431232d54b0542563394f5f161a` |
| `latest-dev` | 20 hours ago | `sha256:d2d883693862955a767801137ab010920c0e153959d9c5e5d5d246d39726469f` |



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
