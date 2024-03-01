---
title: "Image Overview: prometheus-redis-exporter-fips"
linktitle: "prometheus-redis-exporter-fips"
type: "article"
layout: "single"
description: "Overview: prometheus-redis-exporter-fips Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/prometheus-redis-exporter-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/prometheus-redis-exporter-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/prometheus-redis-exporter-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/prometheus-redis-exporter-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimalist Wolfi-based Prometheus Redis Exporter image for exporting metrics to Redis.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/prometheus-redis-exporter:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

The easiest way to install the Prometheus Redis Exporter is to use the Helm chart.

```bash
$ helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
$ helm repo update
$ helm install prom-redis-exporter prometheus-community/prometheus-redis-exporter \
 --set image.repository=cgr.dev/chainguard/prometheus-redis-exporter --set image.tag=latest
```

For more detail, please refer to the [Redis Exporter documentation](https://github.com/oliver006/redis_exporter).
<!--body:end-->

