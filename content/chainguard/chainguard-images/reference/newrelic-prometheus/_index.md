---
title: "Image Overview: newrelic-prometheus"
linktitle: "newrelic-prometheus"
type: "article"
layout: "single"
description: "Overview: newrelic-prometheus Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-04-11 12:38:02
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/newrelic-prometheus/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/newrelic-prometheus/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/newrelic-prometheus/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/newrelic-prometheus/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal [newrelic-prometheus](https://github.com/newrelic/nri-prometheus) container image.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/newrelic-prometheus:latest
```


<!--body:start-->
## Usage

These images are a drop-in replacement for the `newrelic` project. The images are tested against the upstream recommended [`nri-bundle`](https://github.com/newrelic/helm-charts/tree/master/charts/nri-bundle). chart.

A minimum sample of the `values.yaml` required to replace the installation with Chainguard Images is below:

> Note that `latest` is used below for brevity. In long term deployments this is discouraged.

```yaml
# minimal-values.yaml
global:
  cluster: $CLUSTER_NAME
  licenseKey: $LICENSE_KEY

newrelic-infrastructure:
  images:
    agent:
      registry: cgr.dev
      repository: chainguard/newrelic-infrastructure-bundle
      tag: latest
    integration:
      registry: cgr.dev
      repository: chainguard/newrelic-nri-kubernetes
      tag: latest

nri-prometheus:
  enabled: true
  image:
    registry: cgr.dev
    repository: chainguard/newrelic-nri-prometheus
    tag: latest

nri-kube-events:
  enabled: true
  images:
    integration:
      registry: cgr.dev
      repository: chainguard/newrelic-kube-events
      tag: latest
    agent:
      registry: cgr.dev
      repository: chainguard/newrelic-k8s-events-forwarder
      tag: latest

newrelic-logging:
  enabled: true
  image:
    repository: cgr.dev/chainguard/newrelic-fluent-bit-output
    tag: latest

newrelic-prometheus-agent:
  enabled: true
  images:
    configurator:
      registry: cgr.dev
      repository: chainguard/newrelic-prometheus-agent
      tag: latest
    prometheus:
      registry: cgr.dev
      repository: chainguard/prometheus
      tag: latest
```
<!--body:end-->

