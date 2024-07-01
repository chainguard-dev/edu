---
title: "Image Overview: multus-cni-fips"
linktitle: "multus-cni-fips"
type: "article"
layout: "single"
description: "Overview: multus-cni-fips Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-07-01 00:36:20
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

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/multus-cni-fips:latest
```


<!--body:start-->
## Usage

Example below on how to install multus-cni in a cluster with helm, replacing with the chainguard image:

```shell
helm repo add startechnica https://startechnica.github.io/apps
helm repo update
helm install my-release startechnica/multus-cni --namespace my-release --create-namespace \
    --set image.registry=cgr.dev \
    --set image.repository=chainguard/multus-cni \
    --set image.tag=latest
```

Note that the `multus-cni` helm chart by default defines architecture to `amd64`. If deploying with `arm64`, add the following flag:
```
    --set nodeSelector."kubernetes\.io/arch"=arm64
```

For more information, refer to the [upstream documentation](https://github.com/k8snetworkplumbingwg/multus-cni), as well as the documentation for the [helm chart](https://artifacthub.io/packages/helm/startechnica/multus)

<!--body:end-->

