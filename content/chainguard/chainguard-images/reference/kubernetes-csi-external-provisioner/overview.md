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

| Tag (s)       | Last Changed   | Digest                                                                    |
|---------------|----------------|---------------------------------------------------------------------------|
|  `latest`     | September 11th | `sha256:e8f63be35d1c1fdf6e5a97eec7b14d7f29667135af43ce0020c294ba0c0edd56` |
|  `latest-dev` | September 11th | `sha256:809d8a2fa1f9a880f2efceb41d43391ad25860d38432d37b257ba922e32523b5` |



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

