---
title: "Image Overview: cluster-proportional-autoscaler"
type: "article"
description: "Overview: cluster-proportional-autoscaler Chainguard Image"
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

[cgr.dev/chainguard/cluster-proportional-autoscaler](https://github.com/chainguard-images/images/tree/main/images/cluster-proportional-autoscaler)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | August 26th  | `sha256:8aeb93dd909fb79266c141db0b40907cc30dce127019dbbf39360c74b240cd41` |
|  `latest`     | August 22nd  | `sha256:b9ae6803033b2cd9917ebffa3b25860fbec8da02c9e9b70643578712b3cec7da` |



Minimal Kubernetes Cluster Proportional Autoscaler Container

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/cluster-proportional-autoscaler:latest
```

## Usage

This image is a drop-in replacement for the upstream image.
You can run it using the helm chart with:

```shell
$ helm repo add cluster-proportional-autoscaler https://kubernetes-sigs.github.io/cluster-proportional-autoscaler
$ helm install my-release cluster-proportional-autoscaler/cluster-proportional-autoscaler \
    --set image.repository=cgr.dev/chainguard/cluster-proportional-autoscaler \
    --set image.tag=latest
    <other configuration parameters here>
```

See the [configuration](https://github.com/kubernetes-sigs/cluster-proportional-autoscaler/tree/master/charts/cluster-proportional-autoscaler) docs for more examples.

