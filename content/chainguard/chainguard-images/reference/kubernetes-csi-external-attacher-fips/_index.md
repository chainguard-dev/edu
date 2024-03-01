---
title: "Image Overview: kubernetes-csi-external-attacher-fips"
linktitle: "kubernetes-csi-external-attacher-fips"
type: "article"
layout: "single"
description: "Overview: kubernetes-csi-external-attacher-fips Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/kubernetes-csi-external-attacher-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/kubernetes-csi-external-attacher-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kubernetes-csi-external-attacher-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubernetes-csi-external-attacher-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image with [kubernetes-csi/external-attacher](https://github.com/kubernetes-csi/external-attacher).
<!--overview:end-->

<!--getting:start-->
## Download this Image
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

