---
title: "Image Overview: kubernetes-csi-external-attacher"
type: "article"
description: "Overview: kubernetes-csi-external-attacher Chainguard Image"
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
| `latest-dev` | July 12th    | `sha256:835a1c04816ad2d560be69b8d1de98590e2211ae2c626665cac68a63e7b7195a` |
| `latest`     | July 11th    | `sha256:fa13036a968125fd4de35e5067980cc4b48c6431232d54b0542563394f5f161a` |



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
