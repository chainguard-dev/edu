---
title: "Image Overview: node-problem-detector"
linktitle: "node-problem-detector"
type: "article"
layout: "single"
description: "Overview: node-problem-detector Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/node-problem-detector/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/node-problem-detector/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/node-problem-detector/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/node-problem-detector/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
[node-problem-detector](https://github.com/kubernetes/node-problem-detector) aims to make various node problems visible to the upstream layers in the cluster management stack.
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/node-problem-detector:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

Install via `helm` using the upstream source shown below:

```bash
helm repo add deliveryhero https://charts.deliveryhero.io/
helm upgrade --install npd deliveryhero/node-problem-detector \
  --namespace node-problem-detector \
  --create-namespace \
  --set image.repository=cgr.dev/chainguard/node-problem-detector \
  --set image.tag=latest
```
<!--body:end-->

