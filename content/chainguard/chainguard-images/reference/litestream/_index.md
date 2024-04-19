---
title: "Image Overview: litestream"
linktitle: "litestream"
type: "article"
layout: "single"
description: "Overview: litestream Chainguard Image"
date: 2024-04-19 00:39:27
lastmod: 2024-04-19 00:39:27
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/litestream/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/litestream/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/litestream/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/litestream/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Container image for [litestream](https://litestream.io), to replicate SQLite databases.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/litestream:latest
```


<!--body:start-->
## Usage

This image is a drop-in replacement for the upstream image. Please refer to the [Docker container guide](https://litestream.io/guides/docker/) or the [Kubernetes guide](https://litestream.io/guides/kubernetes/) for more details.

Instead of specifying `litestream/litestream`, use `cgr.dev/chainguard/litestream:latest`.
<!--body:end-->

