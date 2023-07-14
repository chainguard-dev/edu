---
title: "Image Overview: cluster-autoscaler"
type: "article"
description: "Overview: cluster-autoscaler Chainguard Image"
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
| `latest-dev` | July 12th    | `sha256:f026c5a7acf24e2e76f4b89619441485b07301940036197a819a5be19b3f611b` |
| `latest`     | July 11th    | `sha256:03b9c0794865fec49035a955f73be35d2fd42db09f6a8e5714899ae59c81c027` |



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
