---
title: "Image Overview: istio-pilot"
linktitle: "istio-pilot"
type: "article"
layout: "single"
description: "Overview: istio-pilot Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/istio-pilot/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/istio-pilot/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/istio-pilot/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/istio-pilot/provenance_info/" >}}
{{</ tabs >}}



# Istio images:

## proxy
This is the data plane part of Istio, consisting of:
- A custom-built Envoy that contains Istio plugins (Wasm, telemetry)
- iptables to route inbound/outbound traffic through the Envoy proxy when acting as a sidecar
- pilot-agent to bootstrap the Envoy with some Istio-specific configurations

## pilot 
Istio Pilot provides mesh-wide traffic management, security and policy capabilities in the Istio Service Mesh.

