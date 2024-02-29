---
title: "Image Overview: kubernetes-csi-external-resizer-fips"
linktitle: "kubernetes-csi-external-resizer-fips"
type: "article"
layout: "single"
description: "Overview: kubernetes-csi-external-resizer-fips Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/kubernetes-csi-external-resizer-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/kubernetes-csi-external-resizer-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kubernetes-csi-external-resizer-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubernetes-csi-external-resizer-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image with [kubernetes-csi/external-resizer](https://github.com/kubernetes-csi/external-resizer).
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/kubernetes-csi-external-resizer:latest
```
<!--getting:end-->

<!--body:start-->
## Using external-resizer

The Chainguard external-resizer image contains the `csi-resizer` controller and is a drop-in replacement for the upstream image.

To try it out, follow the [official installation
instructions](https://github.com/kubernetes-csi/external-resizer/blob/master/README.md#usage).
<!--body:end-->

