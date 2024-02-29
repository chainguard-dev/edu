---
title: "Image Overview: eks-distro-kubernetes-csi-external-snapshotter"
linktitle: "eks-distro-kubernetes-csi-external-snapshotter"
type: "article"
layout: "single"
description: "Overview: eks-distro-kubernetes-csi-external-snapshotter Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/eks-distro-kubernetes-csi-external-snapshotter/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/eks-distro-kubernetes-csi-external-snapshotter/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/eks-distro-kubernetes-csi-external-snapshotter/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/eks-distro-kubernetes-csi-external-snapshotter/provenance_info/" >}}
{{</ tabs >}}

Kubernetes CSI External Snapshotter is a sidecar container that watches Kubernetes Snapshot CRD objects and triggers CreateSnapshot/DeleteSnapshot against a CSI endpoint.

## Get It

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/eks-distro-kubernetes-csi-external-snapshotter:1.23
```
