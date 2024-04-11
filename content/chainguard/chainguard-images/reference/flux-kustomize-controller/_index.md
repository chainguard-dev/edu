---
title: "Image Overview: flux-kustomize-controller"
linktitle: "flux-kustomize-controller"
type: "article"
layout: "single"
description: "Overview: flux-kustomize-controller Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-04-11 12:38:02
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/flux-kustomize-controller/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/flux-kustomize-controller/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/flux-kustomize-controller/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/flux-kustomize-controller/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
`flux` cli to interact with the [Flux](https://fluxcd.io/) gitops toolkit components in a running cluster.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/flux-kustomize-controller:latest
```


<!--body:start-->
## Using `flux`

> NOTE: Many `flux` commands assume a properly connected `kubectl` context, which isn't usually the case when running through docker.

```bash
# Install the flux gitops toolkit using chainguard images
docker run cgr.dev/chainguard/flux export --registry cgr.dev/chainguard | kubectl apply -f -
```
<!--body:end-->

