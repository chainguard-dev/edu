---
title: "Image Overview: Kubernetes-csi-external-resizer"
type: "article"
description: "Overview: Kubernetes-csi-external-resizer Chainguard Image"
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

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest`     | 19 hours ago | `sha256:05c9e45e10cfd3ab0132bff9c71f196ab8144501a083459c96723ea0d8e392e3` |
| `latest-dev` | 19 hours ago | `sha256:314dcfb9baa9600a53768b7dad5084180c7d9dc1b49fa0cf14ad025b4296c433` |



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
