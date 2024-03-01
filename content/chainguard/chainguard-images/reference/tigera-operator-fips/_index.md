---
title: "Image Overview: tigera-operator-fips"
linktitle: "tigera-operator-fips"
type: "article"
layout: "single"
description: "Overview: tigera-operator-fips Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/tigera-operator-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/tigera-operator-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/tigera-operator-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/tigera-operator-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal Project Calico Tigera Operator Image
<!--overview:end-->

<!--getting:start-->
## Download this Image
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

