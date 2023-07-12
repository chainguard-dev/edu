---
title: "Image Overview: Cluster-autoscaler"
type: "article"
description: "Overview: Cluster-autoscaler Chainguard Image"
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

[cgr.dev/chainguard/cluster-autoscaler](https://github.com/chainguard-images/images/tree/main/images/cluster-autoscaler)

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest`     | 20 hours ago | `sha256:03b9c0794865fec49035a955f73be35d2fd42db09f6a8e5714899ae59c81c027` |
| `latest-dev` | 20 hours ago | `sha256:d1a4d9e7df85d5147cfae8518400a854133c7d72626d485e777d44eae51f9384` |



Minimal Kubernetes Cluster Autoscaler Image

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/cluster-autoscaler:latest
```

## Usage

This image is a drop-in replacement for the upstream image.
You can run it using the helm chart with:

```shell
$ helm repo add autoscaler https://kubernetes.github.io/autoscaler
$ helm install my-release autoscaler/cluster-autoscaler \
    --set image.repository=cgr.dev/chainguard/cluster-autoscaler \
    --set image.tag=latest
    <other configuration parameters here>
```

Note that the `cluster-autoscaler` does need cloud provider configuration to work correctly, so it won't run locally.
See the [configuration](https://github.com/kubernetes/autoscaler/tree/master/charts/cluster-autoscaler) docs for more examples.
