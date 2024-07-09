---
title: "Image Overview: grafana-operator"
linktitle: "grafana-operator"
type: "article"
layout: "single"
description: "Overview: grafana-operator Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-07-09 00:39:12
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/grafana-operator/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/grafana-operator/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/grafana-operator/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/grafana-operator/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
A Wolfi-powered operator for Grafana that installs and manages Grafana instances, Dashboards and Datasources.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/grafana-operator:latest
```


<!--body:start-->
# Usage

Use `kubectl` to create a namespace to be used by Grafana Operator:

```bash
kubectl create ns grafana-operator
```

Deploy Grafana Operator within the namespace with the Helm chart:

```bash
  helm upgrade \
    -n grafana-operator \
    -i grafana-operator oci://ghcr.io/grafana/helm-charts/grafana-operator \
    --version v5.8.1 \
    --set image.repository=cgr.dev/chainguard/grafana-operator \
    --set image.tag=latest
```

Note that the upstream chart is not tagged with `latest` so we need to set the version explicitly. Always use the [latest supported version of the chart](https://grafana.github.io/grafana-operator/docs/installation/helm/).

We can verify that the operator is available by checking for the service:

```bash
kubectl get svc -n grafana-operator
```

You've now successfully deployed Grafana Operator! For more documentation, checkout the official docs [here](https://grafana.github.io/grafana-operator/docs/).

<!--body:end-->

