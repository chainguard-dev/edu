---
title: "Image Overview: argocd"
linktitle: "argocd"
type: "article"
layout: "single"
description: "Overview: argocd Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/argocd/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/argocd/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/argocd/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/argocd/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
[argocd](https://argo-cd.readthedocs.io/en/stable/) Declarative continuous deployment for Kubernetes.
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/argocd:latest
```
<!--getting:end-->

<!--body:start-->
## Using argocd

ArgoCD provides two upstream methods for installing, helm, and raw manifests.

The Chainguard Images for ArgoCD are designed to be a drop in replacement for either method. To use them, simply replace the appropriate `image:` path with the Chainguard specific ArgoCD image. Below is an example values file for doing this with helm:

```yaml
global:
  image:
    repository: cgr.dev/chainguard/argocd
```

Using the above values, the helm commands become:

```bash
helm repo add argo https://argoproj.github.io/argo-helm

helm install argocd argo/argo-cd \
	--namespace argocd \
	--create-namespace \
	--set global.image.repository="cgr.dev/chainguard/argocd" \
	--set global.image.tag="latest" \
	--set repoServer.image.repository="cgr.dev/chainguard/argocd-repo-server" \
	--set repoServer.image.tag="latest"
```

Note the multiple images: `argocd` and `argocd-repo-server`. See the [components](#argocd-components) section below for more info.

> NOTE: Setting the tag to "latest" is not recommended, and only shown for illustrative purposes.

Optionally, you can use Chainguard Images to replace the other ArgoCD dependencies:

```yaml
redis:
  image:
    repository: cgr.dev/chainguard/redis
    tag: latest

dex:
  image:
    repository: cgr.dev/chainguard/dex
    tag: latest
```

### ArgoCD Components

ArgoCD is comprised of multiple [components](https://argo-cd.readthedocs.io/en/stable/operator-manual/architecture/#components) that all share the same image.

Keeping in line with the philosophy of minimal components in Chainguard images, we chose to split this up to keep the number of packages in the components to a minimum. This means the overall number of images increases, but the size and complexity of each image is reduced to (almost) the bare minimum needed to function.
<!--body:end-->

