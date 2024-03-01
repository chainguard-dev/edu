---
title: "Image Overview: eks-distro-kubernetes-csi-external-provisioner"
linktitle: "eks-distro-kubernetes-csi-external-provisioner"
type: "article"
layout: "single"
description: "Overview: eks-distro-kubernetes-csi-external-provisioner Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/eks-distro-kubernetes-csi-external-provisioner/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/eks-distro-kubernetes-csi-external-provisioner/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/eks-distro-kubernetes-csi-external-provisioner/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/eks-distro-kubernetes-csi-external-provisioner/provenance_info/" >}}
{{</ tabs >}}

Minimal image that acts as a drop-in replacement for the `kubernetes-csi/external-provisioner` image.  See https://github.com/kubernetes-csi/external-provisioner.

The image runs as `root` so that it can mount a `CSI_ENDPOINT` socket.

## Get It!

## Get It

The image is available on `cgr.dev` and provides older versions of eks-distro-kubernetes-csi-external-provisioner: `1.23` and `1.25`.

You can use the following commands to pull images:

For 1.25:

```
docker pull cgr.dev/chainguard/eks-distro-kubernetes-csi-external-provisioner:1.25
````
For 1.23:
```
docker pull cgr.dev/chainguard/eks-distro-kubernetes-csi-external-provisioner:1.23
```
You can run it with the standard deployment with something like:
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes-csi/external-provisioner/v3.5.0/deploy/kubernetes/rbac.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes-csi/external-provisioner/v3.5.0/deploy/kubernetes/deployment.yaml
kubectl set image deployment/csi-provisioner csi-provisioner="cgr.dev/chainguard/kubernetes-csi-external-provisioner:latest"
```
