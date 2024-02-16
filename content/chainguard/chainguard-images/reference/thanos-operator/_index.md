---
title: "Image Overview: thanos-operator"
linktitle: "thanos-operator"
type: "article"
layout: "single"
description: "Overview: thanos-operator Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-02-16 00:30:51
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/thanos-operator/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/thanos-operator/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/thanos-operator/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/thanos-operator/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image with the [thanos-operator](https://github.com/banzaicloud/thanos-operator).
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/thanos-operator:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

```shell
helm repo add banzaicloud-stable https://kubernetes-charts.banzaicloud.com
helm repo update
helm install thanos-operator banzaicloud-stable/thanos-operator \
    --set image.repository=cgr.dev/chainguard/thanos-operator \
    --set image.tag=latest
```
<!--body:end-->

