---
title: "Image Overview: kubernetes-autoscaler-addon-resizer"
linktitle: "kubernetes-autoscaler-addon-resizer"
type: "article"
layout: "single"
description: "Overview: kubernetes-autoscaler-addon-resizer Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-07-08 00:34:55
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/kubernetes-autoscaler-addon-resizer/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/kubernetes-autoscaler-addon-resizer/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kubernetes-autoscaler-addon-resizer/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubernetes-autoscaler-addon-resizer/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Addon-resizer is a container that vertically scales a Deployment based on the number of nodes in your cluster.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/kubernetes-autoscaler-addon-resizer:latest
```


<!--body:start-->
## Usage

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/autoscaler/master/addon-resizer/deploy/example.yaml
kubectl set image deployment/nanny-v1 pod-nanny=cgr.dev/chainguard/kubernetes-autoscaler-addon-resizer:latest
```

Find more on the [official documentation](https://github.com/kubernetes/autoscaler/blob/master/addon-resizer/README.md)!
<!--body:end-->

