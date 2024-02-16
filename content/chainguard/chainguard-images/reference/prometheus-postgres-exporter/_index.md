---
title: "Image Overview: prometheus-postgres-exporter"
linktitle: "prometheus-postgres-exporter"
type: "article"
layout: "single"
description: "Overview: prometheus-postgres-exporter Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-02-16 00:30:51
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/prometheus-postgres-exporter/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/prometheus-postgres-exporter/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/prometheus-postgres-exporter/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/prometheus-postgres-exporter/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
A PostgreSQL metric exporter for Prometheus
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/prometheus-postgres-exporter:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

The easiest way to install the Prometheus Prometheus Exporter is to use the Helm chart.

```bash
$ helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
$ helm repo update
$ helm install prom-postgres-exporter prometheus-community/prometheus-postgres-exporter \
 --set image.repository=cgr.dev/chainguard/prometheus-postgres-exporter --set image.tag=latest
```

For more detail, please refer to the [Postgres Exporter documentation](https://github.com/prometheus-community/postgres_exporter).
<!--body:end-->

