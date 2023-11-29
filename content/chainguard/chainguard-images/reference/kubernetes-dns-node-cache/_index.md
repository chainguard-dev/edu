---
title: "Image Overview: kubernetes-dns-node-cache"
linktitle: "kubernetes-dns-node-cache"
type: "article"
layout: "single"
description: "Overview: kubernetes-dns-node-cache Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2023-11-29 00:31:44
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/kubernetes-dns-node-cache/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/kubernetes-dns-node-cache/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kubernetes-dns-node-cache/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubernetes-dns-node-cache/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image that acts as a drop-in replacement for the [NodeLocal DNSCache](https://github.com/kubernetes/dns) image.
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/kubernetes-dns-node-cache:latest
```
<!--getting:end-->

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

