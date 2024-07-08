---
title: "Image Overview: grafana-mimir"
linktitle: "grafana-mimir"
type: "article"
layout: "single"
description: "Overview: grafana-mimir Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-07-08 00:34:55
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/grafana-mimir/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/grafana-mimir/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/grafana-mimir/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/grafana-mimir/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
A minimal Wolfi-based image for Grafana Mimir, providing horizontally scalable, highly available, multi-tenant, long-term storage for Prometheus.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/grafana-mimir:latest
```


<!--body:start-->
### Usage

To get started with Grafana Mimir, add Grafana's Helm repository: 

```bash
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
```

Now deploy the Helm chart, substituting Grafana's image with Chainguard's:

```bash
helm install mimir grafana/mimir-distributed \
  --set image.repository=cgr.dev/chainguard/grafana-mimir \
  --set image.tag=latest
```

For additional configuration, please refer to the [upstream documentation](https://grafana.com/docs/helm-charts/mimir-distributed/latest/get-started-helm-charts/).
<!--body:end-->

