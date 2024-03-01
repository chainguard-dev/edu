---
title: "Image Overview: istio-proxy-fips"
linktitle: "istio-proxy-fips"
type: "article"
layout: "single"
description: "Overview: istio-proxy-fips Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/istio-proxy-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/istio-proxy-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/istio-proxy-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/istio-proxy-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
[Istio](https://istio.io) is a service mesh that extends Kubernetes to provide traffic management, telemetry, security, and policy for complex deployments.
<!--overview:end-->

<!--getting:start-->
## Download this Image
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

