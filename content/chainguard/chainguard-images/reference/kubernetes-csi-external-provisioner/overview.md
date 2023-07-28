---
title: "Image Overview: kubernetes-csi-external-provisioner"
type: "article"
description: "Overview: kubernetes-csi-external-provisioner Chainguard Image"
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

[cgr.dev/chainguard/kubernetes-csi-external-provisioner](https://github.com/chainguard-images/images/tree/main/images/kubernetes-csi-external-provisioner)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 27th    | `sha256:b68794ffda975446f64e1979a9bed2c4a70554bf013c853b0ba1e2ebcb069e38` |
|  `latest`     | July 26th    | `sha256:70a92ff633b2cc6deb84feed9257cf4c64233ec15c8891edf4df1cd9ac5ade27` |



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

