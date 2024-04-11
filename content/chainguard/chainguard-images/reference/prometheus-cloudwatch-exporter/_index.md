---
title: "Image Overview: prometheus-cloudwatch-exporter"
linktitle: "prometheus-cloudwatch-exporter"
type: "article"
layout: "single"
description: "Overview: prometheus-cloudwatch-exporter Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/prometheus-cloudwatch-exporter/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/prometheus-cloudwatch-exporter/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/prometheus-cloudwatch-exporter/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/prometheus-cloudwatch-exporter/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimalist Wolfi-based Prometheus CloudWatch Exporter image for exporting metrics to Amazon AWS CloudWatch.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/prometheus-cloudwatch-exporter:latest
```


<!--body:start-->
## Usage

The easiest way to install the Prometheus StatsD Exporter is to use the Helm chart.

```bash
$ helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
$ helm repo update
$ helm install prom-cloudwatch-exporter prometheus-community/prometheus-cloudwatch-exporter \
 --set image.repository=cgr.dev/chainguard/prometheus-cloudwatch-exporter --set image.tag=latest
```

For more detail, please refer to the [CloudWatch Exporter documentation](https://github.com/prometheus/cloudwatch_exporter).
<!--body:end-->

