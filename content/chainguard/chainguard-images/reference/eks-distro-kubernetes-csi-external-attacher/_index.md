---
title: "Image Overview: eks-distro-kubernetes-csi-external-attacher"
linktitle: "eks-distro-kubernetes-csi-external-attacher"
type: "article"
layout: "single"
description: "Overview: eks-distro-kubernetes-csi-external-attacher Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/eks-distro-kubernetes-csi-external-attacher/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/eks-distro-kubernetes-csi-external-attacher/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/eks-distro-kubernetes-csi-external-attacher/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/eks-distro-kubernetes-csi-external-attacher/provenance_info/" >}}
{{</ tabs >}}

Minimal image with [aws/eks-distro/kubernetes-csi/external-attacher](https://github.com/aws/eks-distro/tree/v1-23-eks-21/projects/kubernetes-csi/external-attacher).

## Get It!

This image provides older versions of eks-distro-kubernetes-csi-external-attacher:

- `1.23`
- `1.25`

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/eks-distro-kubernetes-csi-external-attacher:$VERSION
```

## Using external-attacher

The Chainguard external-attacher image contains the `csi-attacher` controller and is a drop-in replacement for the upstream image.

To try it out, follow the [official installation
instructions](https://github.com/kubernetes-csi/external-attacher/blob/master/README.md#usage).
