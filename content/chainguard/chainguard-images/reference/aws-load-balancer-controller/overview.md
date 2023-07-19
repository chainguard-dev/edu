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
|  `latest-dev` | July 18th    | `sha256:4c74fe7aaf2ff33585bc9d0c7bdcaf2a6515e4aa761f0c4b0f94c2739590c324` |
|  `latest`     | July 14th    | `sha256:8ae66092f5514e35391e3af12d192710ec7b7553d6fa0e8e5f02a86c3ebfa734` |



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

