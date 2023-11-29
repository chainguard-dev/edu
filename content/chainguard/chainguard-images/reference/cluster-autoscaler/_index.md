---
title: "Image Overview: cluster-autoscaler"
linktitle: "cluster-autoscaler"
type: "article"
layout: "single"
description: "Overview: cluster-autoscaler Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2023-11-29 00:31:44
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/cluster-autoscaler/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/cluster-autoscaler/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/cluster-autoscaler/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cluster-autoscaler/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal Kubernetes Cluster Autoscaler Image
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/cluster-autoscaler:latest
```
<!--getting:end-->

<!--body:start-->
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
<!--body:end-->

