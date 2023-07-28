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
|  `latest-dev` | July 27th    | `sha256:5f57f180a7377d051d8a78723323f79e5b4747135da40dc8075704876ab299f9` |
|  `latest`     | July 27th    | `sha256:c459659f7d580e4729c46a3fd1090d5f9959636eb1128cbeacaa1e44a93aae35` |



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

