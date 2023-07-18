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
|  `latest-dev` `latest` | July 14th    | `sha256:83a9d92c2dce42a5a09f885c51456e20aae027eaf88af2801771f4fc334e0e2a` |
|                        | July 11th    | `sha256:b2dda8bb4631f9c8ea9151b47f8f272f7224a28faaa88973727b6a4d2335c7d7` |



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

