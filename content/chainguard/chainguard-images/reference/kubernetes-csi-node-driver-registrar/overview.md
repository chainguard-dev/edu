---
title: "Image Overview: kubernetes-csi-node-driver-registrar"
type: "article"
description: "Overview: kubernetes-csi-node-driver-registrar Chainguard Images"
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

`stable` [cgr.dev/chainguard/kubernetes-csi-node-driver-registrar](https://github.com/chainguard-images/images/tree/main/images/kubernetes-csi-node-driver-registrar)
| Tags     | Aliases                         |
|----------|---------------------------------|
| `latest` | `2`, `2.8`, `2.8.0`, `2.8.0-r0` |



## Get It

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/kubernetes-csi-node-driver-registrar
```

## Run it

Generally speaking, the `kubernetes-csi-node-driver-registrar` is a low level Kubernetes component used to register drivers, and not meant to be managed directly. However, all the steps outlined in the [upstream repo](https://github.com/kubernetes-csi/node-driver-registrar) apply just as well to the Chainguard Image version.

