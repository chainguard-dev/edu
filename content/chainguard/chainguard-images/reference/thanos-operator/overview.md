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
|  `latest`     | August 15th  | `sha256:c3b285169453a38a380d3bdb66071902b3c1d4048b4fb7fe5bc159dbf1a08bd2` |
|  `latest-dev` | August 15th  | `sha256:8ab5a79e1e51281e5a3a4dfc18c4860ec54944a29a639856a20a8550addf440b` |



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

