---
title: "Image Overview: argocd"
type: "article"
description: "Overview: argocd Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "images-reference"
weight: 500
toc: true
---

[cgr.dev/chainguard/argocd](https://github.com/chainguard-images/images/tree/main/images/argocd)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | August 3rd   | `sha256:10aac97e333aa65737427408d2bd773445f095921dfb23580475785e88390c34` |
|  `latest-dev` | August 3rd   | `sha256:73f7868bd949c47511acb2f9fbffd6e56af600c82a8c2e9a30eb000f8d2e2769` |



[argocd](https://argo-cd.readthedocs.io/en/stable/) Declarative continuous deployment for Kubernetes.

## Get It!

The images available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/argocd
docker pull cgr.dev/chainguard/argocd-repo-server
```

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
    tag: 7.0

dex:
  image:
    repository: cgr.dev/chainguard/dev
    tag: latest
```

### ArgoCD Components

ArgoCD is comprised of multiple [components](https://argo-cd.readthedocs.io/en/stable/operator-manual/architecture/#components) that all share the same image.

Keeping in line with the philosophy of minimal components in Chainguard images, we chose to split this up to keep the number of packages in the components to a minimum. This means the overall number of images increases, but the size and complexity of each image is reduced to (almost) the bare minimum needed to function.

