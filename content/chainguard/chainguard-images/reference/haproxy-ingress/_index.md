---
title: "Image Overview: haproxy-ingress"
linktitle: "haproxy-ingress"
type: "article"
layout: "single"
description: "Overview: haproxy-ingress Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2023-11-27 16:34:14
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/haproxy-ingress/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/haproxy-ingress/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/haproxy-ingress/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/haproxy-ingress/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Kubernetes ingress controller implementation for HAProxy
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/haproxy-ingress:latest
```
<!--getting:end-->

<!--body:start-->
# Usage

You can use this image with the [Helm Chart](https://artifacthub.io/packages/helm/haproxy-ingress/haproxy-ingress) of the project:

```shell
helm repo add haproxy-ingress https://haproxy-ingress.github.io/charts

helm repo update

helm install ingress haproxy-ingress/haproxy-ingress \
  --set controller.image.repository="cgr.dev/chainguard/haproxy-ingress" \
  --set controller.image.tag="latest"

kubectl wait --for=condition=ready pod --selector "app.kubernetes.io/name=haproxy-ingress" --timeout=120s
```
<!--body:end-->

