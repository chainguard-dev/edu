---
title: "Image Overview: newrelic-kubernetes"
linktitle: "newrelic-kubernetes"
type: "article"
layout: "single"
description: "Overview: newrelic-kubernetes Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2023-12-04 00:17:31
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/newrelic-kubernetes/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/newrelic-kubernetes/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/newrelic-kubernetes/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/newrelic-kubernetes/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal [newrelic-kubernetes](https://github.com/newrelic/nri-kubernetes) container image.
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/newrelic-kubernetes:latest
```
<!--getting:end-->

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

