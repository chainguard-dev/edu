---
title: "Image Overview: eks-distro-kubernetes-csi-node-driver-registrar"
linktitle: "eks-distro-kubernetes-csi-node-driver-registrar"
type: "article"
layout: "single"
description: "Overview: eks-distro-kubernetes-csi-node-driver-registrar Chainguard Image"
date: 2024-02-29 16:25:55
lastmod: 2024-02-29 16:25:55
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/eks-distro-kubernetes-csi-node-driver-registrar/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/eks-distro-kubernetes-csi-node-driver-registrar/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/eks-distro-kubernetes-csi-node-driver-registrar/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/eks-distro-kubernetes-csi-node-driver-registrar/provenance_info/" >}}
{{</ tabs >}}

## Get It

The image is available on `cgr.dev` and provides older versions of eks-distro-kubernetes-csi-node-driver-registrar: `1.23` and `1.25`.

You can use the following commands to pull images:

For 1.25:

```
docker pull cgr.dev/chainguard/eks-distro-kubernetes-csi-node-driver-registrar:1.25
````
For 1.23:
```
docker pull cgr.dev/chainguard/eks-distro-kubernetes-csi-node-driver-registrar:1.23
```
## Run it
Generally speaking, the `kubernetes-csi-node-driver-registrar` is a low level Kubernetes component used to register drivers, and not meant to be managed directly. However, all the steps outlined in the [upstream repo](https://github.com/kubernetes-csi/node-driver-registrar) apply just as well to the Chainguard Image version.
