---
title: "Image Overview: ingress-nginx-controller"
linktitle: "ingress-nginx-controller"
type: "article"
layout: "single"
description: "Overview: ingress-nginx-controller Chainguard Image"
date: 2022-11-01T11:07:52+02:00
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/ingress-nginx-controller/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/ingress-nginx-controller/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/ingress-nginx-controller/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/ingress-nginx-controller/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
 Ingress-NGINX Controller for Kubernetes
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/ingress-nginx-controller:latest
```
<!--getting:end-->

<!--body:start-->
## Using `ingress-nginx-controller`

The Chainguard image is a drop in replacement for the upstream image. For example, to install with the upstream helm chart:

```bash
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx

helm install foo ingress-nginx/ingress-nginx --set image.repository=cgr.dev/chainguard/ingress-nginx-controller
```
<!--body:end-->

