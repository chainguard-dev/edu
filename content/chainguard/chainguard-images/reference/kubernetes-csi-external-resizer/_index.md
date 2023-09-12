---
title: "Image Overview: kubernetes-csi-external-resizer"
linktitle: "kubernetes-csi-external-resizer"
type: "article"
layout: "single"
description: "Overview: kubernetes-csi-external-resizer Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/kubernetes-csi-external-resizer/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/kubernetes-csi-external-resizer/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kubernetes-csi-external-resizer/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubernetes-csi-external-resizer/provenance_info/" >}}
{{</ tabs >}}



Minimal image with [kubernetes-csi/external-resizer](https://github.com/kubernetes-csi/external-resizer).

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/external-resizer:latest
```

## Using external-resizer

The Chainguard external-resizer image contains the `csi-resizer` controller and is a drop-in replacement for the upstream image.

To try it out, follow the [official installation
instructions](https://github.com/kubernetes-csi/external-resizer/blob/master/README.md#usage).

