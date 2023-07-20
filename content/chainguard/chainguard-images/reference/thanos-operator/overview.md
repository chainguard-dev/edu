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
|  `latest-dev` | July 19th    | `sha256:9842b9b5f99ab717c54cc33c8c7a0066a734fa9d99163a1aac3d360d3289e9d4` |
|  `latest`     | July 14th    | `sha256:294c787ec59cd7b099ae54f547ddcca40eafbeae4fa4e86146cecfd158d61b6a` |



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

