---
title: "Image Overview: multus-cni-fips"
linktitle: "multus-cni-fips"
type: "article"
layout: "single"
description: "Overview: multus-cni-fips Chainguard Image"
date: 2024-04-04 00:51:18
lastmod: 2024-04-04 00:51:18
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/multus-cni-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/multus-cni-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/multus-cni-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/multus-cni-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
A CNI meta-plugin for multi-homed pods in Kubernetes
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/multus-cni:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

Example below on how to install multus-cni in a cluster with helm, replacing with the chainguard image:

```shell
helm repo add startechnica https://startechnica.github.io/apps
helm repo update
helm install my-release startechnica/multus --namespace my-release --create-namespace \
    --set image.repository=cgr.dev/chainguard/multus-cni \
    --set image.tag=latest
```

For more information, refer to the [upstream documentation](https://github.com/k8snetworkplumbingwg/multus-cni), as well as the documentation for the [helm chart](https://artifacthub.io/packages/helm/startechnica/multus)

<!--body:end-->

