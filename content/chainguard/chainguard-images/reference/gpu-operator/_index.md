---
title: "Image Overview: gpu-operator"
linktitle: "gpu-operator"
type: "article"
layout: "single"
description: "Overview: gpu-operator Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/gpu-operator/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/gpu-operator/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/gpu-operator/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gpu-operator/provenance_info/" >}}
{{</ tabs >}}

This image provides older versions of gpu-operator:

- latest

The ("latest") image and usage documentation can be found in our public repo here:
https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/install-gpu-operator.html

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/gpu-operator:$VERSION
```

## Usage

```sh
helm repo add nvidia https://helm.ngc.nvidia.com/nvidia
helm upgrade --install gpu-operator \
    nvidia/gpu-operator \
    --set operator.repository=cgr.dev/chainguard-private \
    --set operator.image=gpu-operator \
    --set operator.image.tag=$VERSION
```

> **WARNING:** You'll want to make sure the `gpu-operator` chart is up-to-date and use the latest operator tag that's within the compatibility matrix.

> **WARNING:** You need GPU nodes to run the operator as it will schedule Deployments and DaemonSets on nodes with GPUs.

