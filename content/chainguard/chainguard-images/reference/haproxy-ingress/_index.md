---
title: "Image Overview: haproxy-ingress"
linktitle: "haproxy-ingress"
type: "article"
layout: "single"
description: "Overview: haproxy-ingress Chainguard Image"
date: 2022-11-01T11:07:52+02:00
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/haproxy-ingress/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/haproxy-ingress/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/haproxy-ingress/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/haproxy-ingress/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Kubernetes ingress controller implementation for HAProxy
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/haproxy-ingress:latest
```
<!--getting:end-->

<!--body:start-->
# Use It!

You can use this image with the `haproxy-ingress` project's [Helm chart](https://artifacthub.io/packages/helm/haproxy-ingress/haproxy-ingress). To begin, add the Helm chart's repository.

```shell
helm repo add haproxy-ingress https://haproxy-ingress.github.io/charts
```

Then run the following command to retrieve the latest information about the charts in the repository you just added.

```shell
helm repo update
```

Then install `haproxy-ingress` with the following command. This command directs Helm to install it using Chainguard's `haprox-ingress:latest` image.

```shell
helm install ingress haproxy-ingress/haproxy-ingress \
  --set controller.image.repository="cgr.dev/chainguard/haproxy-ingress" \
  --set controller.image.tag="latest"
```

Run the following command to confirm that the the Pod is running and ready to use.

```shell
kubectl wait --for=condition=ready pod --selector "app.kubernetes.io/name=haproxy-ingress" --timeout=120s
```
<!--body:end-->

