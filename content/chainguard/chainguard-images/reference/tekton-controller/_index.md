---
title: "Image Overview: tekton-controller"
linktitle: "tekton-controller"
type: "article"
layout: "single"
description: "Overview: tekton-controller Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/tekton-controller/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/tekton-controller/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/tekton-controller/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/tekton-controller/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
[Tekton](https://tekton.dev) provides a cloud-native Pipeline resource, mainly intended for CI/CD use cases.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/tekton-controller:latest
```


<!--body:start-->
[Tekton](https://tekton.dev) provides a cloud-native Pipeline resource, mainly intended for CI/CD use cases.

[Tekton Chains](https://tekton.dev/docs/chains/) provides additional supply chain security features.

The [Tekton CLI](https://tekton.dev/docs/cli/) is a command-line interface for Tekton.

## Usage

These images a drop-in replacement for the upstream images.

You can use an [upstream release](https://github.com/tektoncd/pipeline/releases) and replace the released images with those from Chainguard.

```shell
curl -sL https://storage.googleapis.com/tekton-releases/pipeline/latest/release.yaml | \
    sed "s|gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/controller[a-z0-9:@.]\{1,\}|cgr.dev/chainguard/tekton-controller|g" | \
    sed "s|gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/entrypoint[a-z0-9:@.]\{1,\}|cgr.dev/chainguard/tekton-entrypoint|g" | \
    sed "s|gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/events[a-z0-9:@.]\{1,\}|cgr.dev/chainguard/tekton-events|g" | \
    sed "s|gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/nop[a-z0-9:@.]\{1,\}|cgr.dev/chainguard/tekton-nop|g" | \
    sed "s|gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/resolvers[a-z0-9:@.]\{1,\}|cgr.dev/chainguard/tekton-resolvers|g" | \
    sed "s|gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/sidecarlogresults[a-z0-9:@.]\{1,\}|cgr.dev/chainguard/tekton-sidecarlogresults|g" | \
    sed "s|gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/webhook[a-z0-9:@.]\{1,\}|cgr.dev/chainguard/tekton-webhook|g" | \
    sed "s|gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/workingdirinit[a-z0-9:@.]\{1,\}|cgr.dev/chainguard/tekton-workingdirinit|g" | \
    kubectl apply -f -
```

For Tekton Chains:

```shell
curl -sL https://storage.googleapis.com/tekton-releases/chains/latest/release.yaml | \
    sed "s|gcr.io/tekton-releases/github.com/tektoncd/chains/cmd/controller[a-z0-9:@.]\{1,\}|cgr.dev/chainguard/tekton-chains|g" | \
    kubectl apply -f -
```

For Tekton CLI:

```
docker run cgr.dev/chainguard/tekton-cli version
```
<!--body:end-->

