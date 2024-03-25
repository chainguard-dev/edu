---
title: "Image Overview: prometheus-blackbox-exporter"
linktitle: "prometheus-blackbox-exporter"
type: "article"
layout: "single"
description: "Overview: prometheus-blackbox-exporter Chainguard Image"
date: 2024-03-25 00:49:44
lastmod: 2024-03-25 00:49:44
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/prometheus-blackbox-exporter/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/prometheus-blackbox-exporter/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/prometheus-blackbox-exporter/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/prometheus-blackbox-exporter/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Prometheus blackbox exporter allows blackbox probing of endpoints over HTTP, HTTPS, DNS, TCP, ICMP and gRPC.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/prometheus-blackbox-exporter:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

The easiest way to install the Prometheus Blackbox exporter is to use the Helm chart.

```bash
$ helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
$ helm repo update
$ helm install blackbox-exporter prometheus-community/prometheus-blackbox-exporter \
 --set image.registry=cgr.dev \
 --set image.repository=chainguard/prometheus-blackbox-exporter \
 --set image.tag=latest
```

For more detail, please refer to the [Blackbox exporter documentation](https://github.com/prometheus/blackbox_exporter).
<!--body:end-->

