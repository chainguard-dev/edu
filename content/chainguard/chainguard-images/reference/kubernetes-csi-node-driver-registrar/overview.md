---
title: "Image Overview: Kubernetes-csi-node-driver-registrar"
type: "article"
description: "Overview: Kubernetes-csi-node-driver-registrar Chainguard Image"
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

[cgr.dev/chainguard/kubernetes-csi-node-driver-registrar](https://github.com/chainguard-images/images/tree/main/images/kubernetes-csi-node-driver-registrar)

| Tag      | Last Updated | Digest                                                                    |
|----------|--------------|---------------------------------------------------------------------------|
| `latest` | 16 hours ago | `sha256:122f95fd5199f825276824da0df7a59800319f976a9cd5b3d5965b05eab21567` |



## Get It

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/kubernetes-csi-node-driver-registrar
```

## Run it

Generally speaking, the `kubernetes-csi-node-driver-registrar` is a low level Kubernetes component used to register drivers, and not meant to be managed directly. However, all the steps outlined in the [upstream repo](https://github.com/kubernetes-csi/node-driver-registrar) apply just as well to the Chainguard Image version.
