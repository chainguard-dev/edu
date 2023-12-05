---
title: "Image Overview: vector"
linktitle: "vector"
type: "article"
layout: "single"
description: "Overview: vector Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/vector/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/vector/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/vector/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/vector/provenance_info/" >}}
{{</ tabs >}}



Minimalist [wolfi](https://github.com/wolfi-dev)-based image of [Vector]
(https://github.com/vectordotdev/vector) for high-performance, end-to-end 
(agent & aggregator) observability data pipeline that puts you in 
control of your observability data

## Get It

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/vector:latest
```

## Testing

Fortunately, we have a Helm Chart ready-to-use for testing this image. 

You can find it [here](https://github.com/vectordotdev/helm-charts/blob/develop/charts/vector/README.md).

Basically, all you need to do is running the commands below to test the application:

```shell
helm repo add vector https://helm.vector.dev
helm repo update
helm install --name vector \
  --set image.registry=cgr.dev/ \
  --set image.repository=chainguard/vector \
  --set image.tag=latest
```

Once you run the commands above, you will end up having the application running on your cluster.

