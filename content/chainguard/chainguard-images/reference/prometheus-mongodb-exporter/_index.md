---
title: "Image Overview: prometheus-mongodb-exporter"
linktitle: "prometheus-mongodb-exporter"
type: "article"
layout: "single"
description: "Overview: prometheus-mongodb-exporter Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/prometheus-mongodb-exporter/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/prometheus-mongodb-exporter/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/prometheus-mongodb-exporter/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/prometheus-mongodb-exporter/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimalist Wolfi-based Prometheus MongoDB Exporter image for exporting various metrics about MongoDB.
<!--overview:end-->

<!--getting:start-->
## Get It!
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

