---
title: "Image Overview: kubernetes-csi-node-driver-registrar"
linktitle: "kubernetes-csi-node-driver-registrar"
type: "article"
layout: "single"
description: "Overview: kubernetes-csi-node-driver-registrar Chainguard Image"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/kubernetes-csi-node-driver-registrar/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/kubernetes-csi-node-driver-registrar/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kubernetes-csi-node-driver-registrar/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubernetes-csi-node-driver-registrar/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
 Sidecar container that registers a CSI driver with the kubelet using the kubelet plugin registration mechanism. 
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/kubernetes-csi-node-driver-registrar:latest
```
<!--getting:end-->

<!--body:start-->
## Run it

Generally speaking, the `kubernetes-csi-node-driver-registrar` is a low level Kubernetes component used to register drivers, and not meant to be managed directly. However, all the steps outlined in the [upstream repo](https://github.com/kubernetes-csi/node-driver-registrar) apply just as well to the Chainguard Image version.
<!--body:end-->

