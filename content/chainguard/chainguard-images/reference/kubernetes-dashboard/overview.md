---
title: "Image Overview: kubernetes-dashboard"
type: "article"
description: "Overview: kubernetes-dashboard Chainguard Images"
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

`stable` [cgr.dev/chainguard/kubernetes-dashboard](https://github.com/chainguard-images/images/tree/main/images/kubernetes-dashboard)
| Tags         | Aliases                                         |
|--------------|-------------------------------------------------|
| `latest`     | `2`, `2.7`, `2.7.0`, `2.7.0-r3`                 |
| `latest-dev` | `2-dev`, `2.7-dev`, `2.7.0-dev`, `2.7.0-r3-dev` |



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

