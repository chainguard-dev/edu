---
title: "Image Overview: kubernetes-dns-node-cache-fips"
linktitle: "kubernetes-dns-node-cache-fips"
type: "article"
layout: "single"
description: "Overview: kubernetes-dns-node-cache-fips Chainguard Image"
date: 2024-07-05 00:42:00
lastmod: 2024-07-05 00:42:00
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/kubernetes-dns-node-cache-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/kubernetes-dns-node-cache-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kubernetes-dns-node-cache-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubernetes-dns-node-cache-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image that acts as a drop-in replacement for the [NodeLocal DNSCache](https://github.com/kubernetes/dns) image.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/kubernetes-dns-node-cache-fips:latest
```


<!--body:start-->
## Usage

```shell
helm repo add deliveryhero https://charts.deliveryhero.io/
helm repo update
helm install node-local-dns deliveryhero/node-local-dns \
    --set image.repository=cgr.dev/chainguard/kubernetes-dns-node-cache \
    --set image.tag=latest
```
<!--body:end-->

