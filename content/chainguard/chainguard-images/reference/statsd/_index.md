---
title: "Image Overview: statsd"
linktitle: "statsd"
type: "article"
layout: "single"
description: "Overview: statsd Chainguard Image"
date: 2024-01-19 00:16:42
lastmod: 2024-01-19 00:16:42
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/statsd/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/statsd/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/statsd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/statsd/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Daemon for easy but powerful stats aggregation
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/statsd:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

See the [statsd documentation](https://github.com/statsd/statsd?tab=readme-ov-file#usage) for more information on how to use statsd.

You can also use a Helm chart to install this image on a Kubernetes cluster:

```bash
helm repo add keyporttech https://keyporttech.github.io/helm-charts/
helm install my-release keyporttech/statsd \
  --namespace statsd \
  --create-namespace \
  --set image.repository="cgr.dev/chainguard/statsd" \
  --set image.tag="latest"
```
<!--body:end-->

