---
title: "Image Overview: kubernetes-csi-external-attacher-fips"
linktitle: "kubernetes-csi-external-attacher-fips"
type: "article"
layout: "single"
description: "Overview: kubernetes-csi-external-attacher-fips Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-04-11 12:38:02
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

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/kubernetes-csi-external-attacher-fips:latest
```


<!--body:start-->
## Using external-attacher

The Chainguard external-attacher image contains the `csi-attacher` controller and is a drop-in replacement for the upstream image.

To try it out, follow the [official installation
instructions](https://github.com/kubernetes-csi/external-attacher/blob/master/README.md#usage).
<!--body:end-->

