---
title: "Image Overview: qdrant"
linktitle: "qdrant"
type: "article"
layout: "single"
description: "Overview: qdrant Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/qdrant/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/qdrant/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/qdrant/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/qdrant/provenance_info/" >}}
{{</ tabs >}}



[qdrant](https://github.com/qdrant/qdrant) Qdrant is a high-performance, massive-scale Vector Database for the next generation of AI.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/qdrant
```

## Using Qdrant

This image should be a drop-in replacement for the upstream image, and works by default in the helm charts.

To install, follow the steps here: https://qdrant.tech/documentation/guides/installation

But override the image variable in the helm chart:

```shell
$ helm repo add qdrant https://qdrant.to/helm
$ helm upgrade --install qdrant --set image.repository=cgr.dev/chainguard/qdrant --set image.tag=latest qdrant/qdrant
```

The only notable difference is that this image contains both a root and a non-root user, so you can't/don't need to use the `useUnprivileged` [helm variable](https://github.com/qdrant/qdrant-helm/blob/2ddefd61ccd9da092739eaf13f9a76b8b3cfd55e/charts/qdrant/values.yaml#L7C7-L7C7)

Because the helm chart uses the same image for intializing file system permissions and running the final app, we have to run as a root user by default.
The image can still be run as a non-root user (in this case `qdrant`), and the helm chart properly sets that up by default.

