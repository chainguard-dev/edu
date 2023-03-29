---
title: "Image Overview: karpenter"
type: "article"
description: "Overview: karpenter Chainguard Images"
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

`experimental` [cgr.dev/chainguard/karpenter](https://github.com/chainguard-images/images/tree/main/images/karpenter)
| Tags         | Aliases                                            |
|--------------|----------------------------------------------------|
| `latest`     | `0`, `0.27`, `0.27.0`, `0.27.0-r0`                 |
| `latest-dev` | `0-dev`, `0.27-dev`, `0.27.0-dev`, `0.27.0-r0-dev` |



Minimal image with Karpenter. **EXPERIMENTAL**

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/karpenter:latest
```

## Using Karpenter

The Chainguard Karpenter image contains the `karpenter` controller and is a drop-in replacement for the upstream image.

To try it out, you should be able to follow the [official installation instructions](https://karpenter.sh/v0.27.0/getting-started/getting-started-with-eksctl/) and pass this to helm to use our image:

```
--set controller.image.repository=cgr.dev/chainguard/karpenter \
--set controller.image.digest=$DIGEST
```
