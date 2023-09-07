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

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest-dev` | September 6th | `sha256:a11b2fdfc1f113d1d91efa9ee5c74d9139c3885b0370588f791ad516511ad14a` |
|  `latest`     | September 4th | `sha256:41dc4f507385808370401867e81b9614d15e988e7d9a1b9e71f7bebeae3aefbf` |



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

