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
|  `latest-dev` | July 18th    | `sha256:1b58b27e591bc9447d55209383655afab922cee31f51a3f1e24ed9039c3b78b5` |
|  `latest`     | July 12th    | `sha256:20fb09a96739c1e56f499b51b926f96b1b620536120416c2adbce2f8ad7467c3` |
|               | July 11th    | `sha256:727b3f4aceae4fdcbd8fb8c9665714f5f65459342b8ad8ab6e73189bc33a1a9a` |
|               | July 4th     | `sha256:72316daf8b23b8eafe73e2731e862732d52ed6c45f866d6b3314dba9c02f6a42` |
|               | July 4th     | `sha256:d3dfd61887c758dca865bfec0eec994c7fd940bd6a8c6c7ee29c671892a6c24d` |
|               | June 21st    | `sha256:98e77f869dc45801dedd9728208926e3987a6fac4cbd7a81df1c00ddef587ffc` |



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

