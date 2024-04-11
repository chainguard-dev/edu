---
title: "Image Overview: prometheus-elasticsearch-exporter-fips"
linktitle: "prometheus-elasticsearch-exporter-fips"
type: "article"
layout: "single"
description: "Overview: prometheus-elasticsearch-exporter-fips Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/prometheus-elasticsearch-exporter-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/prometheus-elasticsearch-exporter-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/prometheus-elasticsearch-exporter-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/prometheus-elasticsearch-exporter-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimalist Wolfi-based Prometheus Elasticsearch Exporter image for exporting various metrics about Elasticsearch.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/prometheus-elasticsearch-exporter-fips:latest
```


<!--body:start-->
## Usage

The easiest way to install the Prometheus Elasticsearch Exporter is to use the Helm chart.

```bash
$ helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
$ helm repo update
$ helm install prom-elasticsearch-exporter prometheus-community/prometheus-elasticsearch-exporter \
 --set image.repository=cgr.dev/chainguard/prometheus-elasticsearch-exporter --set image.tag=latest
```

For more detail, please refer to the [Elasticsearch Exporter documentation](https://github.com/prometheus-community/elasticsearch_exporter).
<!--body:end-->

