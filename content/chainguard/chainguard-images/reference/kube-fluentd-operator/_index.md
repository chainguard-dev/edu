---
title: "Image Overview: kube-fluentd-operator"
linktitle: "kube-fluentd-operator"
type: "article"
layout: "single"
description: "Overview: kube-fluentd-operator Chainguard Image"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/kube-fluentd-operator/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/kube-fluentd-operator/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kube-fluentd-operator/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kube-fluentd-operator/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
This image is used for the [Kubernetes Fluentd Operator](https://github.com/vmware/kube-fluentd-operator)
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/kube-fluentd-operator:latest
```
<!--getting:end-->

<!--body:start-->
This image is a drop-in replacement for the Kubernetes Fluentd Operator available upstream at `vmware/kube-fluentd-operator`.

## Use It!

With helm:

```
git clone git@github.com:vmware/kube-fluentd-operator.git
helm install --create-namespace kfo ./kube-fluentd-operator/charts/log-router \
  --set rbac.create=true \
  --set image.tag=latest \
  --set image.repository=cgr.dev/chainguard/kube-fluentd-operator
```
<!--body:end-->

