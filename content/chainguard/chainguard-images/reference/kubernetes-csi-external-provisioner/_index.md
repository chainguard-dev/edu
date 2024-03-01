---
title: "Image Overview: kubernetes-csi-external-provisioner"
linktitle: "kubernetes-csi-external-provisioner"
type: "article"
layout: "single"
description: "Overview: kubernetes-csi-external-provisioner Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-03-01 12:14:22
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/kubernetes-csi-external-provisioner/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/kubernetes-csi-external-provisioner/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kubernetes-csi-external-provisioner/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubernetes-csi-external-provisioner/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image that acts as a drop-in replacement for the `kubernetes-csi/external-provisioner` image.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/kubernetes-csi-external-provisioner:latest
```
<!--getting:end-->

<!--compatibility:start-->
## Compatibility Notes

The image runs as `root` so that it can mount a `CSI_ENDPOINT` socket.
<!--compatibility:end-->

<!--body:start-->
You can run it with the standard deployment with something like:

```
kubectl apply -f https://raw.githubusercontent.com/kubernetes-csi/external-provisioner/v3.5.0/deploy/kubernetes/rbac.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes-csi/external-provisioner/v3.5.0/deploy/kubernetes/deployment.yaml
kubectl set image deployment/csi-provisioner csi-provisioner="cgr.dev/chainguard/kubernetes-csi-external-provisioner:latest"
```
<!--body:end-->

