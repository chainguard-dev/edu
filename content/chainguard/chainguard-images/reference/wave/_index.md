---
title: "Image Overview: wave"
linktitle: "wave"
type: "article"
layout: "single"
description: "Overview: wave Chainguard Image"
date: 2024-04-29 00:53:42
lastmod: 2024-04-29 00:53:42
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/wave/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/wave/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/wave/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/wave/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Wave watches Deployments within a Kubernetes cluster and ensures that each Deployment's Pods always have up to date configuration.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/wave:latest
```


<!--body:start-->
## Compatibility Warning

Starting from versions [v0.6.0](https://github.com/wave-k8s/wave/releases/tag/v0.6.0), [wave](https://github.com/wave-k8s/wave) project add [supports](https://github.com/wave-k8s/wave/pull/145) for `go1.22` with Kubernetes `v1.29`.

If you are using older versions of Kubernetes, please note that the latest version of wave may or may not be compatible with your Kubernetes version.

If you notice any behavioral changes or issues between your version of wave vs the latest Chainguard image, please [file an issue](https://github.com/wave-k8s/wave/issues/new) on the upstream repository.

## Usage

You can deploy the wave with the Helm:

```shell
helm repo add wave-k8s https://wave-k8s.github.io/wave/
helm update
helm install wave wave-k8s/wave \
  --namespace wave \
	--create-namespace \
	--set image.repository="cgr.dev/chainguard/wave" \
	--set image.tag="latest" \
```

Find more on the [Helm Chart values](https://github.com/wave-k8s/wave/tree/master/charts/wave)!

Please follow upstream [documentation](https://wave-k8s.github.io/wave) for usage and configuration.

<!--body:end-->

