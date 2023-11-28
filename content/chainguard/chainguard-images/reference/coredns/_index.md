---
title: "Image Overview: coredns"
linktitle: "coredns"
type: "article"
layout: "single"
description: "Overview: coredns Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2023-11-28 00:31:13
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/coredns/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/coredns/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/coredns/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/coredns/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
[CoreDNS](https://coredns.io) is a fast and flexible DNS server written in Go
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/coredns:latest
```
<!--getting:end-->

<!--body:start-->
## Using CoreDNS

The Chainguard CoreDNS image is a drop-in replacement for the upstream image.
See the [upstream documentation](https://coredns.io/) for usage information specific to your environment.

Below is a quickstart example using the upstream helm chart:

```bash
helm repo add coredns https://coredns.github.io/helm
helm install coredns coredns/coredns \
	--set image.repository="cgr.dev/chainguard/coredns" \
	--set image.tag="latest" \
	--set isClusterService=false
```
<!--body:end-->

