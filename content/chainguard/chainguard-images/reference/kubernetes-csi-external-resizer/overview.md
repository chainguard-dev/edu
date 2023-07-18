---
title: "Image Overview: kubernetes-csi-external-resizer"
type: "article"
description: "Overview: kubernetes-csi-external-resizer Chainguard Image"
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

[cgr.dev/chainguard/kubernetes-csi-external-resizer](https://github.com/chainguard-images/images/tree/main/images/kubernetes-csi-external-resizer)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 18th    | `sha256:7f3caac7c2d3ad11bec74bde4e177a2dd550f9b964a32a935a5734d70a43a14e` |
|  `latest`     | July 14th    | `sha256:9e8ffd1301b16c279b1481f77f2dd18cc75de3c5b192905d237f74c3cb02a48a` |
|               | July 12th    | `sha256:0f0d806714870b55e278dfae923ededc9611723d089b03cabb6a8fa4fcebd340` |



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

