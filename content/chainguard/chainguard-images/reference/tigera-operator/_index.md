---
title: "Image Overview: tigera-operator"
linktitle: "tigera-operator"
type: "article"
layout: "single"
description: "Overview: tigera-operator Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2023-11-29 00:31:44
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/tigera-operator/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/tigera-operator/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/tigera-operator/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/tigera-operator/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal Project Calico Tigera Operator Image
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/tigera-operator:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

This image is a drop-in replacement for the upstream image.
You can run it using the helm chart with:

```shell
helm repo add projectcalico https://projectcalico.docs.tigera.io/charts
helm repo update

helm install calico projectcalico/tigera-operator \
    --namespace tigera-operator \
    --create-namespace \
    --set autoDiscovery.clusterName=foo \
    --set tigeraOperator.registry=cgr.dev \
    --set tigeraOperator.image=chainguard/tigera-operator \
    --set tigeraOperator.version=latest

kubectl wait --namespace tigera-operator --for=condition=ready pod --selector name=tigera-operator --timeout=120s
```
<!--body:end-->

