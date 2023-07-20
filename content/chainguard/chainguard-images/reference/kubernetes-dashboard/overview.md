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
|  `latest-dev` | July 19th    | `sha256:5878e267785a7aba04ad96fe248f56d15c17cbf68a0d0325806b9435eb152ce6` |
|  `latest`     | July 14th    | `sha256:7ddfb0959aa54dc35bbaea4b37ad8ef1150726270fbf8f45c813500c2087f14f` |



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

