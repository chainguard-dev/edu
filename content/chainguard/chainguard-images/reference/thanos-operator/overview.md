---
title: "Image Overview: thanos-operator"
type: "article"
description: "Overview: thanos-operator Chainguard Image"
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

[cgr.dev/chainguard/thanos-operator](https://github.com/chainguard-images/images/tree/main/images/thanos-operator)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | August 31st  | `sha256:871e73b55cac2886ab7b33a6cd410d81acb526c14bab1e53608b62627e9f19a7` |
|  `latest-dev` | August 31st  | `sha256:c69d594cf714f0790e29434df00f99d5921315872b7666f2125e21d4a88252a1` |



Minimal image with the [thanos-operator](https://github.com/banzaicloud/thanos-operator).

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/thanos-operator:latest
```

## Usage

```shell
helm repo add banzaicloud-stable https://kubernetes-charts.banzaicloud.com
helm repo update
helm install thanos-operator banzaicloud-stable/thanos-operator \
    --set image.repository=cgr.dev/chainguard/thanos-operator \
    --set image.tag=latest
```

