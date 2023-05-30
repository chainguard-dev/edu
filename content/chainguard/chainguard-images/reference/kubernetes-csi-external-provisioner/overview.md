---
title: "Image Overview: kubernetes-csi-external-provisioner"
type: "article"
description: "Overview: kubernetes-csi-external-provisioner Chainguard Images"
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

`stable` [cgr.dev/chainguard/kubernetes-csi-external-provisioner](https://github.com/chainguard-images/images/tree/main/images/kubernetes-csi-external-provisioner)
| Tags         | Aliases                                         |
|--------------|-------------------------------------------------|
| `latest`     | `3`, `3.5`, `3.5.0`, `3.5.0-r1`                 |
| `latest-dev` | `3-dev`, `3.5-dev`, `3.5.0-dev`, `3.5.0-r1-dev` |



Minimal image that acts as a drop-in replacement for the `kubernetes-csi/external-provisioner` image.  See https://github.com/kubernetes-csi/external-provisioner.

The image runs as `root` so that it can mount a `CSI_ENDPOINT` socket.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/kubernetes-csi-external-provisioner:latest
```

You can run it with the standard deployment with something like:

```
kubectl apply -f https://raw.githubusercontent.com/kubernetes-csi/external-provisioner/v3.5.0/deploy/kubernetes/rbac.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes-csi/external-provisioner/v3.5.0/deploy/kubernetes/deployment.yaml
kubectl set image deployment/csi-provisioner csi-provisioner="cgr.dev/chainguard/kubernetes-csi-external-provisioner:latest"
```

