---
title: "Image Overview: mlflow-bitnami"
linktitle: "mlflow-bitnami"
type: "article"
layout: "single"
description: "Overview: mlflow-bitnami Chainguard Image"
date: 2024-05-13 00:45:28
lastmod: 2024-05-13 00:45:28
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/mlflow-bitnami/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/mlflow-bitnami/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/mlflow-bitnami/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/mlflow-bitnami/provenance_info/" >}}
{{</ tabs >}}

# MLflow Bitnami

This image provides MLflow with compatibility for Bitnami's Helm chart.

To deploy this image with Bitnami's chart, run:

```bash
helm install my-release oci://registry-1.docker.io/bitnamicharts/mlflow \
  --set image.registry=cgr.dev \
  --set image.repository=<YOUR REGISTRY>/mlflow-bitnami \
  --set image.tag=latest
```

The latest image and usage documentation can be found in [our public repo](https://github.com/chainguard-images/images/tree/main/images/mlflow).

