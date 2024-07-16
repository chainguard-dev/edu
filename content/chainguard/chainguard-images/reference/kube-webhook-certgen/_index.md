---
title: "Image Overview: kube-webhook-certgen"
linktitle: "kube-webhook-certgen"
type: "article"
layout: "single"
description: "Overview: kube-webhook-certgen Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/kube-webhook-certgen/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/kube-webhook-certgen/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kube-webhook-certgen/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kube-webhook-certgen/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Generates certificates and updates Kubernetes webhooks, integrating with Helm to simplify Kubernetes job execution.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/kube-webhook-certgen:latest
```


<!--body:start-->

## Forked version, maintained by ingress-nginx project!
NOTE: this is the ingress-nginx projects fork of `kube-webhook-certgen`. The
[original project](https://github.com/jet/kube-webhook-certgen) is no longer
maintained.

## Prometheus operator
Below is an example of how to deploy the prometheus operator, which utilizes
this image.

First, add the helm operator:

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```

Then, use the following Terraform configuration to deploy the Prometheus
Operator. Note, we're utilizing the[Chainguard prometheus operator image](https://github.com/chainguard-images/images/tree/main/images/prometheus-operator),
as well as the Chainguard kube-webhook-certgen image:

```bash
helm install prometheus-operator prometheus-community/kube-prometheus-stack \
  --set prometheusOperator.image.registry=cgr.dev \
  --set prometheusOperator.image.repository=chainguard/prometheus-operator \
  --set prometheusOperator.image.tag=latest
  --set prometheusOperator.admissionWebhooks.patch.image.registry=cgr.dev \
  --set prometheusOperator.admissionWebhooks.patch.image.repository=chainguard/kube-webhook-certgen \
  --set prometheusOperator.admissionWebhooks.patch.image.tag=latest
```

For more information, refer to the following resources:
- [prometheus operator docs](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack)
- [kube-webhook-certgen docs](https://github.com/kubernetes/ingress-nginx/tree/main/images/kube-webhook-certgen)

<!--body:end-->

