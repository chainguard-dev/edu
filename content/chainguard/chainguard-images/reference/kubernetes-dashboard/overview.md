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
|  `latest-dev` | August 31st  | `sha256:af1775e7fd2fa7b7c709ae781c9c5935d01bd284b3de8fcdbd0fa8d6357e2575` |
|  `latest`     | August 31st  | `sha256:e9dbb40e79e9dc1d9ebf3908b665cca0676944dbb3c758763a0243bf3c94cefa` |



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

