---
title: "Image Overview: prometheus-mongodb-exporter-fips"
linktitle: "prometheus-mongodb-exporter-fips"
type: "article"
layout: "single"
description: "Overview: prometheus-mongodb-exporter-fips Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/prometheus-mongodb-exporter-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/prometheus-mongodb-exporter-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/prometheus-mongodb-exporter-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/prometheus-mongodb-exporter-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimalist Wolfi-based Prometheus MongoDB Exporter image for exporting various metrics about MongoDB.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/prometheus-mongodb-exporter:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

The easiest way to install the Prometheus MongoDB Exporter is to use the Helm chart.

```bash
$ helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
$ helm repo update
$ helm install prom-mongodb-exporter prometheus-community/prometheus-mongodb-exporter \
 --set image.repository=cgr.dev/chainguard/prometheus-mongodb-exporter --set image.tag=latest
```

For more detail, please refer to the [MongoDB Exporter documentation](https://github.com/percona/mongodb_exporter).
<!--body:end-->

