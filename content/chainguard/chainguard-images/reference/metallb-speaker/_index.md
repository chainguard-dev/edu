---
title: "Image Overview: metallb-speaker"
linktitle: "metallb-speaker"
type: "article"
layout: "single"
description: "Overview: metallb-speaker Chainguard Image"
date: 2024-03-25 00:49:44
lastmod: 2024-03-25 00:49:44
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/metallb-speaker/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/metallb-speaker/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/metallb-speaker/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/metallb-speaker/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
[MetalLB](https://metallb.org) provides network load balancers for bare-metal Kubernetes clusters
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/metallb:latest
```
<!--getting:end-->

<!--body:start-->
Configuring MetalLB for your Kubernetes environment is beyond the scope of this document. It has multiple configuration options depending on the mode that it is configured to use (Layer 2 or BGP). Refer to the [MetalLB Concepts](https://metallb.universe.tf/concepts/) documentation for details on how each mode works.

Their [installation guide](https://metallb.universe.tf/installation/) is a good reference that has numerous examples using Kubernetes manifests, Kustomize manifests, and Helm charts.

Finally, visit the [configuration reference pages](https://metallb.universe.tf/configuration/) for details on how to use MetalLb in each mode with different CNI providers.
<!--body:end-->

