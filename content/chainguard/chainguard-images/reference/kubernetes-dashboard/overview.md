---
title: "Image Overview: Kubernetes-dashboard"
type: "article"
description: "Overview: Kubernetes-dashboard Chainguard Image"
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

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest-dev` | 19 hours ago | `sha256:f7bf57e2e15333ad394efd5596fc4b40d2ea50ffaecd633d508787839e6eea94` |
| `latest`     | 19 hours ago | `sha256:9bdbd04a65b0370c1fb346e8daf524b1959b9bd7920425914e14ed9531ab0c1b` |



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
