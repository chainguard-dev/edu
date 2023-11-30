---
title: "Image Overview: istio-proxy"
linktitle: "istio-proxy"
type: "article"
layout: "single"
description: "Overview: istio-proxy Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/istio-proxy/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/istio-proxy/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/istio-proxy/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/istio-proxy/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
[Istio](https://istio.io) is a service mesh that extends Kubernetes to provide traffic management, telemetry, security, and policy for complex deployments.
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/istio:latest
```
<!--getting:end-->

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

