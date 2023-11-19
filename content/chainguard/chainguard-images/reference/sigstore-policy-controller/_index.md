---
title: "Image Overview: sigstore-policy-controller"
linktitle: "sigstore-policy-controller"
type: "article"
layout: "single"
description: "Overview: sigstore-policy-controller Chainguard Image"
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

{{< tabs >}}
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/sigstore-policy-controller/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/sigstore-policy-controller/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/sigstore-policy-controller/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/sigstore-policy-controller/provenance_info/" >}}
{{</ tabs >}}



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

