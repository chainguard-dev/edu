---
title: "Image Overview: neuvector-prometheus-exporter"
linktitle: "neuvector-prometheus-exporter"
type: "article"
layout: "single"
description: "Overview: neuvector-prometheus-exporter Chainguard Image"
date: 2024-04-08 00:38:35
lastmod: 2024-04-08 00:38:35
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/neuvector-prometheus-exporter/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/neuvector-prometheus-exporter/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/neuvector-prometheus-exporter/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/neuvector-prometheus-exporter/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Prometheus exporter and Grafana template for NeuVector container security platform.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/neuvector-prometheus-exporter:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

Add the NeuVector Helm repository to your repositories list:

```shell
helm repo add neuvector https://neuvector.github.io/neuvector-helm/
helm repo update
```

Next, install the NeuVector Prometheus Exporter with the following command:

```sh
helm install neuvector-prometheus-exporter neuvector/monitor \
    --namespace neuvector \
    --create-namespace \
    --set exporter.apiSvc=neuvector-svc-controller:10443 \
    --set exporter.image.repository=cgr.dev/chainguard/neuvector-prometheus-exporter \
    --set exporter.image.tag=<set to the latest chainguard tag>
```

Jump to the official [Helm Chart](https://github.com/neuvector/neuvector-helm/blob/master/charts/monitor/README.md) for more detailed usage.

P.S: The Exporter will not work without the NeuVector Core Service. Install the [neuvector/core](https://github.com/neuvector/neuvector-helm/tree/master/charts/core) first.

<!--body:end-->

