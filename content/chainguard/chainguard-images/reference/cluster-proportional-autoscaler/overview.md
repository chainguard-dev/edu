---
title: "Image Overview: Cluster-proportional-autoscaler"
type: "article"
description: "Overview: Cluster-proportional-autoscaler Chainguard Image"
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

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest-dev` | 20 hours ago | `sha256:93aa16d779ffcfbadeb9a0f0f6b2b0611de4dbcc00abfd4c3d896a8694a2ea21` |
| `latest`     | 20 hours ago | `sha256:c673d2b952b66afac1375b990ed638ca4b22f7c0322fc6de6f2fe810be82a418` |



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
