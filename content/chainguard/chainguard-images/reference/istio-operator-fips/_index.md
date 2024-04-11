---
title: "Image Overview: istio-operator-fips"
linktitle: "istio-operator-fips"
type: "article"
layout: "single"
description: "Overview: istio-operator-fips Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/istio-operator-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/istio-operator-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/istio-operator-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/istio-operator-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
[Istio](https://istio.io) is a service mesh that extends Kubernetes to provide traffic management, telemetry, security, and policy for complex deployments.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/istio-operator-fips:latest
```


<!--body:start-->
# Istio images:

## proxy
This is the data plane part of Istio, consisting of:
- A custom-built Envoy that contains Istio plugins (Wasm, telemetry)
- iptables to route inbound/outbound traffic through the Envoy proxy when acting as a sidecar
- pilot-agent to bootstrap the Envoy with some Istio-specific configurations

## pilot
Istio Pilot provides mesh-wide traffic management, security and policy capabilities in the Istio Service Mesh.
<!--body:end-->

