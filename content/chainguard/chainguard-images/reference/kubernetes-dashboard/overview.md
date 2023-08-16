---
title: "Image Overview: kubernetes-dashboard"
type: "article"
description: "Overview: kubernetes-dashboard Chainguard Image"
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

[cgr.dev/chainguard/kubernetes-dashboard](https://github.com/chainguard-images/images/tree/main/images/kubernetes-dashboard)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | August 15th  | `sha256:e13e5f1451bc53c1422f00e84e0cde4b74bde874a602e57cb2c50cce0c572bb7` |
|  `latest`     | August 15th  | `sha256:f9042e1d9568b7874733d48e8f68ad95356a48bc6651b56cf412a12aeec062cc` |



Minimal image that acts as a drop-in replacement for the `kubernetesui/dashboard` image.

The dashboard listens on port `8443` by default.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/kubernetes-dashboard:latest
```

You can run it with the standard deployment with something like:

```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml
kubectl set image -n kubernetes-dashboard deployment/kubernetes-dashboard kubernetes-dashboard="cgr.dev/chainguard/kubernetes-dashboard:latest"
```

