---
title: "Image Overview: tekton-events-fips"
linktitle: "tekton-events-fips"
type: "article"
layout: "single"
description: "Overview: tekton-events-fips Chainguard Image"
date: 2024-03-29 00:47:42
lastmod: 2024-03-29 00:47:42
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/tekton-events-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/tekton-events-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/tekton-events-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/tekton-events-fips/provenance_info/" >}}
{{</ tabs >}}

## tekton-fips

This image is a variant of the Tekton images that is FIPS-compliant.

> **Note**:
> Tekton's entrypoint image has requirements that are incompatible with how we normally enable FIPS-validated crypto in Go binaries. In order for it to work with Tekton, the binary must be statically linked. Luckily, this binary does no crypto -- and we ensure that it does no crypto. This means we believe that the regular Tekton entrypoint image can be used in a FIPS environment, alongside the regular FIPS-variant Tekton images.

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
    kubectl apply -f -
```

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

