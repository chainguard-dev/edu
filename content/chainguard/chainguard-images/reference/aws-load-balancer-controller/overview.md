---
title: "Image Overview: aws-load-balancer-controller"
type: "article"
description: "Overview: aws-load-balancer-controller Chainguard Image"
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

[cgr.dev/chainguard/aws-load-balancer-controller](https://github.com/chainguard-images/images/tree/main/images/aws-load-balancer-controller)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 27th    | `sha256:20fb472cd1e322845d09f2e69f6714e4f5c3f00a64abf42194c4d5ffb862dd68` |
|  `latest`     | July 26th    | `sha256:3c06f2182ee1aa1f54b894a1f478ee4f70fb9a22ab06e9b4a31b6a72609dfd39` |



Minimal Image for Kubernetes controller for Elastic Load Balancers

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/aws-load-balancer-controller:latest
```

## Usage

This image is a drop-in replacement for the upstream image.
You can run it using the helm chart with:

```shell
$ helm repo add eks https://aws.github.io/eks-charts
$ helm install aws-load-balancer-controller eks/aws-load-balancer-controller \
    --set image.repository=cgr.dev/chainguard/aws-load-balancer-controller \
    --set image.tag=latest
    <other configuration parameters here>
```

Note that the `aws-load-balancer-controller` does need cloud provider configuration to work correctly, so it won't run locally.
See the [configuration](https://github.com/aws/eks-charts/tree/master/stable/aws-load-balancer-controller) docs for more examples.

