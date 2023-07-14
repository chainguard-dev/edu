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

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest-dev` | July 12th    | `sha256:9af4af9df80ac1978c16f8f4192788fde92b3328a24fddea2ca016e08b130a9d` |
| `latest`     | July 12th    | `sha256:20fb09a96739c1e56f499b51b926f96b1b620536120416c2adbce2f8ad7467c3` |



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
