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

| Tag (s)       | Last Changed   | Digest                                                                    |
|---------------|----------------|---------------------------------------------------------------------------|
|  `latest`     | September 11th | `sha256:6d7b3a6662e01309aa5f6446d50c6c9066e45d6c2d26b5c31f43bb8c29a3af6f` |
|  `latest-dev` | September 11th | `sha256:351b9f146c5d48fae9013af7a8f53f601fa657e3560ae512801a231372694c1a` |



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

