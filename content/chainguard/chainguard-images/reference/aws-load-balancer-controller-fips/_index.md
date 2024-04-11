---
title: "Image Overview: aws-load-balancer-controller-fips"
linktitle: "aws-load-balancer-controller-fips"
type: "article"
layout: "single"
description: "Overview: aws-load-balancer-controller-fips Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-04-11 12:38:02
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu: 
  docs: 
    parent: "images-reference"
weight: 500
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/aws-load-balancer-controller-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/aws-load-balancer-controller-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/aws-load-balancer-controller-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/aws-load-balancer-controller-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal Image for Kubernetes controller for Elastic Load Balancers
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/aws-load-balancer-controller-fips:latest
```


<!--body:start-->
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
<!--body:end-->

