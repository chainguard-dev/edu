---
title: "Image Overview: k3s-allinone"
linktitle: "k3s-allinone"
type: "article"
layout: "single"
description: "Overview: k3s-allinone Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-02-16 00:30:51
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/k3s-allinone/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/k3s-allinone/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/k3s-allinone/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/k3s-allinone/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image of [K3s](https://k3s.io/), a lightweight Kubernetes distribution
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/k3s:latest
```
<!--getting:end-->

<!--body:start-->
This image is a drop in replacement for the upstream `rancher/k3s` image, which means it works everywhere you would expect.

The quickest way to test it is locally with `docker`:

```bash
docker run --rm -v `pwd`:/etc/rancher/k3s --privileged -p 6443:6443 cgr.dev/chainguard/k3s:latest

KUBECONFIG=k3s.yaml kubectl get po -A
```

You can also use it as a drop in replacement in `k3d`:

```bash
k3d cluster create -i cgr.dev/chainguard/k3s:latest
```
<!--body:end-->

