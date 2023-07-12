---
title: "Image Overview: Thanos-operator"
type: "article"
description: "Overview: Thanos-operator Chainguard Image"
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

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest`     | 19 hours ago | `sha256:c89b138e3a328b512aa3a1722b359e8a666357997c8c3b46c0eb34d377cbceb4` |
| `latest-dev` | 19 hours ago | `sha256:e31c27ecc37809eedd15a8076fee3240cbc7d57d6d1c4cf3f5d1239daeec986b` |



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
