---
title: "Image Overview: sigstore-policy-controller-fips"
linktitle: "sigstore-policy-controller-fips"
type: "article"
layout: "single"
description: "Overview: sigstore-policy-controller-fips Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-02-29 16:25:55
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/sigstore-policy-controller-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/sigstore-policy-controller-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/sigstore-policy-controller-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/sigstore-policy-controller-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Policy Controller image that is part of the Sigstore stack
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/sigstore-policy-controller:latest
```
<!--getting:end-->

<!--body:start-->
# Minimal `sigstore/policy-controller` image

This image can be used with the upstream helm chart with the following
overrides:

```bash
IMAGE=cgr.dev/chainguard/sigstore-policy-controller

helm repo add sigstore https://sigstore.github.io/helm-charts

helm install policy-controller sigstore/policy-controller \
	--namespace policy-controller \
	--create-namespace \
	--set webhook.image.repository="${IMAGE}" \
	--set webhook.image.version="$(crane digest ${IMAGE})"
```
<!--body:end-->

