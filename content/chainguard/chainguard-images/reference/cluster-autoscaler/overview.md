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

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | August 23rd  | `sha256:5b7d7859b4011c2a7ae104ff9aabdcad48504d0c633fda186e45886eada79818` |
|  `latest`     | August 15th  | `sha256:ba3efb7adfb15485719c16bab368fcb9a6073b1014aba1aa6c730da8b5f3ff16` |



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

