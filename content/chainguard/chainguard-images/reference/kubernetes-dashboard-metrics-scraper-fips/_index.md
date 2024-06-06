---
title: "Image Overview: kubernetes-dashboard-metrics-scraper-fips"
linktitle: "kubernetes-dashboard-metrics-scraper-fips"
type: "article"
layout: "single"
description: "Overview: kubernetes-dashboard-metrics-scraper-fips Chainguard Image"
date: 2024-06-06 00:48:16
lastmod: 2024-06-06 00:48:16
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/kubernetes-dashboard-metrics-scraper-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/kubernetes-dashboard-metrics-scraper-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kubernetes-dashboard-metrics-scraper-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubernetes-dashboard-metrics-scraper-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image that acts as a drop-in replacement for the `kubernetesui/dashboard` image.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/kubernetes-dashboard-metrics-scraper-fips:latest
```


<!--compatibility:start-->
## Compatibility Notes

The dashboard listens on port `8443` by default.
<!--compatibility:end-->

<!--body:start-->
You can run it with the standard deployment with something like:

```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml
kubectl set image -n kubernetes-dashboard deployment/kubernetes-dashboard kubernetes-dashboard="cgr.dev/chainguard/kubernetes-dashboard:latest"
```
<!--body:end-->

