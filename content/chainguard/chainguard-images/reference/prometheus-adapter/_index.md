---
title: "Image Overview: prometheus-adapter"
linktitle: "prometheus-adapter"
type: "article"
layout: "single"
description: "Overview: prometheus-adapter Chainguard Image"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/prometheus-adapter/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/prometheus-adapter/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/prometheus-adapter/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/prometheus-adapter/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
[prometheus-adapter](https://github.com/kubernetes-sigs/prometheus-adapter) is a Prometheus project used to collect Prometheus metrics in Kubernetes.
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/prometheus-adapter:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

The easiest way to install the Prometheus Adapter is to use the Helm chart.

```bash
$ helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
$ helm repo update
$ helm install adapter prometheus-community/prometheus-adapter \
 --set image.repository=cgr.dev/chainguard/prometheus-adapter --set image.tag=latest
```

For more detail, please refer to the [Adapter documentation](https://github.com/kubernetes-sigs/prometheus-adapter).
<!--body:end-->

