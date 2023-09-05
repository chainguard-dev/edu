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

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest`     | September 4th | `sha256:6a9b064c3523996cd75a9a16103a7a9dcf28b7f7e9b454a85823788d19f89aeb` |
|  `latest-dev` | September 4th | `sha256:8e3cf7b2ed45a8495fe84884bb6e839816e5f6aa23013811de5d3876519f4b8e` |



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

