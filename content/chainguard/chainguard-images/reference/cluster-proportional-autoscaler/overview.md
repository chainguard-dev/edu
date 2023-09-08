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

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest-dev` | September 7th | `sha256:4f059e54b671e9683d50323bddbc52cb04b07e013b832e3708bd78ac2510f604` |
|  `latest`     | September 4th | `sha256:6c874df6cdf70ec48dd1ae5d5c4fafb2682d7c9b05d67dde9701d527168953c6` |



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

