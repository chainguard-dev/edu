---
title: "Image Overview: tekton-sidecarlogresults-fips"
linktitle: "tekton-sidecarlogresults-fips"
type: "article"
layout: "single"
description: "Overview: tekton-sidecarlogresults-fips Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-06-23 00:43:06
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/tekton-sidecarlogresults-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/tekton-sidecarlogresults-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/tekton-sidecarlogresults-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/tekton-sidecarlogresults-fips/provenance_info/" >}}
{{</ tabs >}}

## tekton-fips

This image is a variant of the Tekton images that is FIPS-compliant.

## Usage

These images a drop-in replacement for the upstream images.

You can use an [upstream release](https://github.com/tektoncd/pipeline/releases) and replace the released images with those from Chainguard.

```shell
curl -sL https://storage.googleapis.com/tekton-releases/pipeline/latest/release.yaml | \
    sed "s|gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/controller[a-z0-9:@.]\{1,\}|cgr.dev/chainguard-private/tekton-controller-fips|g" | \
    sed "s|gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/entrypoint[a-z0-9:@.]\{1,\}|cgr.dev/chainguard-private/tekton-entrypoint-fips|g" | \
    sed "s|gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/events[a-z0-9:@.]\{1,\}|cgr.dev/chainguard-private/tekton-events-fips|g" | \
    sed "s|gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/nop[a-z0-9:@.]\{1,\}|cgr.dev/chainguard-private/tekton-nop-fips|g" | \
    sed "s|gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/resolvers[a-z0-9:@.]\{1,\}|cgr.dev/chainguard-private/tekton-resolvers-fips|g" | \
    sed "s|gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/sidecarlogresults[a-z0-9:@.]\{1,\}|cgr.dev/chainguard-private/tekton-sidecarlogresults-fips|g" | \
    sed "s|gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/webhook[a-z0-9:@.]\{1,\}|cgr.dev/chainguard-private/tekton-webhook-fips|g" | \
    sed "s|gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/workingdirinit[a-z0-9:@.]\{1,\}|cgr.dev/chainguard-private/tekton-workingdirinit-fips|g" | \
    sed "s|cgr.dev/chainguard/busybox[a-z0-9:@.]\{1,\}|cgr.dev/chainguard-private/busybox-fips|g" | \
    kubectl apply -f -
```

Instead of `busybox-fips` one can use any image with a shell and OpenSSL FIPS provider, for example `chainguard-base-fips`. This is needed because of entrypoint support for SPIRE. Currently it is not possible to build up to date entrypoint images without SPIRE, see this [issue](https://github.com/tektoncd/pipeline/issues/8034). If deployment does not use SPIRE support, one can use `cgr.dev/chainguard-private/busybox` and `cgr.dev/chainguard-private/tekton-entrypoint` images combination instead.

For Tekton Chains:

```shell
curl -sL https://storage.googleapis.com/tekton-releases/chains/latest/release.yaml | \
    sed "s|gcr.io/tekton-releases/github.com/tektoncd/chains/cmd/controller[a-z0-9:@.]\{1,\}|cgr.dev/chainguard-private/tekton-chains-fips|g" | \
    kubectl apply -f -
```

For Tekton CLI:

```
docker run cgr.dev/chainguard-private/tekton-cli-fips version
```
<!--body:end-->

