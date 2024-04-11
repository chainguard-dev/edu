---
title: "Image Overview: ingress-nginx-controller-fips"
linktitle: "ingress-nginx-controller-fips"
type: "article"
layout: "single"
description: "Overview: ingress-nginx-controller-fips Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-04-11 12:38:02
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/ingress-nginx-controller-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/ingress-nginx-controller-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/ingress-nginx-controller-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/ingress-nginx-controller-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
 Ingress-NGINX Controller for Kubernetes
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/ingress-nginx-controller-fips:latest
```


<!--body:start-->
## Using `ingress-nginx-controller`

The Chainguard image is a drop in replacement for the upstream image. For example, to install with the upstream helm chart:

```bash
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx

helm install foo ingress-nginx/ingress-nginx --set image.repository=cgr.dev/chainguard/ingress-nginx-controller
```
<!--body:end-->

