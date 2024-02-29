---
title: "Image Overview: newrelic-infrastructure-k8s"
linktitle: "newrelic-infrastructure-k8s"
type: "article"
layout: "single"
description: "Overview: newrelic-infrastructure-k8s Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/newrelic-infrastructure-k8s/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/newrelic-infrastructure-k8s/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/newrelic-infrastructure-k8s/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/newrelic-infrastructure-k8s/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal [newrelic-infrastructure-k8s](https://github.com/newrelic/nri-kubernetes/tree/v2) container image.
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/newrelic-infrastructure-k8s:latest
```
<!--getting:end-->

<!--body:start-->
## Usage
helm upgrade --install nik \
  --repo https://newrelic.github.io/nri-kubernetes newrelic-infrastructure \
  --version 2.10.3 \
  --set cluster=$CLUSTER_NAME \
  --set privileged=true \
  --set licenseKey=$LICENSE_KEY \
  --set image.repository=cgr.dev/chainguard-private/newrelic-infrastructure-k8s \
  --set image.tag=latest

