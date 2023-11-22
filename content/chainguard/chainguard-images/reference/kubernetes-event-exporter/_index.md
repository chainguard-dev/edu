---
title: "Image Overview: kubernetes-event-exporter"
linktitle: "kubernetes-event-exporter"
type: "article"
layout: "single"
description: "Overview: kubernetes-event-exporter Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/kubernetes-event-exporter/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/kubernetes-event-exporter/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kubernetes-event-exporter/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubernetes-event-exporter/provenance_info/" >}}
{{</ tabs >}}



# Kubernetes-Event-Exporter

Minimalist [wolfi](https://github.com/wolfi-dev)-based image of [Kubernetes Event Exporter]
(https://github.com/resmoio/kubernetes-event-exporter) for exporting Kubernetes 
events to various outputs to be used for observability or alerting purposes.


## Get it!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/kubernetes-event-exporter:latest
```

## Usage

Project documentation suggests usage of Bitnami chart which is comprehensive.

This chart bootstraps a Kubernetes Event Exporter deployment on a Kubernetes cluster using 
the Helm package manager.

To install the chart with the release name my-release:

```
helm install my-release oci://registry-1.docker.io/bitnamicharts/kubernetes-event-exporter

helm upgrade my-release oci://registry-1.docker.io/bitnamicharts/kubernetes-event-exporter \
  --set image.repository=cgr.dev/chainguard/kubernetes-event-exporter \
  --set image.tag=latest

```

To uninstall/delete this deployment:

```
helm delete my-release
```


