---
title: "Image Overview: nvidia-container-toolkit"
linktitle: "nvidia-container-toolkit"
type: "article"
layout: "single"
description: "Overview: nvidia-container-toolkit Chainguard Image"
date: 2024-05-06 00:43:57
lastmod: 2024-05-06 00:43:57
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/nvidia-container-toolkit/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/nvidia-container-toolkit/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/nvidia-container-toolkit/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/nvidia-container-toolkit/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
The NVIDIA Container Toolkit allows users to build and run GPU accelerated containers.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/nvidia-container-toolkit:latest
```


<!--body:start-->

## Usage

```sh
helm repo add nvidia https://helm.ngc.nvidia.com/nvidia
helm upgrade --install gpu-operator nvidia/gpu-operator \
    -n gpu-operator \
    --create-namespace \
    --set toolkit.repository=cgr.dev/chainguard \
    --set toolkit.image=nvidia-container-toolkit \
    --set toolkit.version=latest
```

* Refer to [values.yaml](https://github.com/NVIDIA/gpu-operator/blob/master/deployments/gpu-operator/values.yaml) file for more configuration options.

> [!WARNING]
> You'll want to make sure the `gpu-operator` chart is up-to-date and use the latest operator tag that's within the compatibility matrix.

> [!IMPORTANT]
> You need GPU nodes to run the operator as it will schedule Deployments and DaemonSets on nodes with GPUs.

> [!NOTE]
> If you want to learn more about how we are testing this image, please refer to the [TESTING.md](./TESTING.md) file.

<!--body:end-->

