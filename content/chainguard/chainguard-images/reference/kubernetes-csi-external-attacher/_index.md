---
title: "Image Overview: kubernetes-csi-external-attacher"
linktitle: "kubernetes-csi-external-attacher"
type: "article"
layout: "single"
description: "Overview: kubernetes-csi-external-attacher Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/kubernetes-csi-external-attacher/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/kubernetes-csi-external-attacher/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kubernetes-csi-external-attacher/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubernetes-csi-external-attacher/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image with [kubernetes-csi/external-attacher](https://github.com/kubernetes-csi/external-attacher).
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/kubernetes-csi-external-attacher:latest
```
<!--getting:end-->

<!--body:start-->
## Using external-attacher

The Chainguard external-attacher image contains the `csi-attacher` controller and is a drop-in replacement for the upstream image.

To try it out, follow the [official installation
instructions](https://github.com/kubernetes-csi/external-attacher/blob/master/README.md#usage).
<!--body:end-->

