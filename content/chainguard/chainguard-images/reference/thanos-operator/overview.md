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
|  `latest-dev` | August 15th  | `sha256:f75293e9e4e90e94709a62ab1e949e6d76898147cfcd1186472c66d774da770e` |
|  `latest`     | August 15th  | `sha256:3a608f1ed99eb779c2849a3b2d9edeeb15358d9e1f5cfebfb43cdd400aa6aa28` |



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

