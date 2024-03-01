---
title: "Image Overview: kubernetes-dashboard-metrics-scraper"
linktitle: "kubernetes-dashboard-metrics-scraper"
type: "article"
layout: "single"
description: "Overview: kubernetes-dashboard-metrics-scraper Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/kubernetes-dashboard-metrics-scraper/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/kubernetes-dashboard-metrics-scraper/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kubernetes-dashboard-metrics-scraper/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubernetes-dashboard-metrics-scraper/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image that acts as a drop-in replacement for the `kubernetesui/dashboard` image.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/kubernetes-dashboard:latest
```
<!--getting:end-->

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

