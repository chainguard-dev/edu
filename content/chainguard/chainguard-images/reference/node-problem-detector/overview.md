---
title: "Image Overview: node-problem-detector"
type: "article"
description: "Overview: node-problem-detector Chainguard Image"
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

[cgr.dev/chainguard/node-problem-detector](https://github.com/chainguard-images/images/tree/main/images/node-problem-detector)

| Tag (s)                | Last Changed | Digest                                                                    |
|------------------------|--------------|---------------------------------------------------------------------------|
|  `latest` `latest-dev` | August 23rd  | `sha256:21a98107997d6f45125aac0afe5d23c06212bd479de01e97ae550f7e4b46f73f` |



[node-problem-detector](https://github.com/kubernetes/node-problem-detector) aims to make various node problems visible to the upstream layers in the cluster management stack.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/node-problem-detector
```

## Usage

Install via `helm` using the upstream source shown below:

```bash
helm repo add deliveryhero https://charts.deliveryhero.io/
helm upgrade --install npd deliveryhero/node-problem-detector \
  --namespace node-problem-detector \
  --create-namespace \
  --set image.repository=cgr.dev/chainguard/node-problem-detector \
  --set image.tag=latest
```

