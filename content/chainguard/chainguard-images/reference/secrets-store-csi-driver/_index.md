---
title: "Image Overview: secrets-store-csi-driver"
linktitle: "secrets-store-csi-driver"
type: "article"
layout: "single"
description: "Overview: secrets-store-csi-driver Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/secrets-store-csi-driver/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/secrets-store-csi-driver/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/secrets-store-csi-driver/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/secrets-store-csi-driver/provenance_info/" >}}
{{</ tabs >}}



Minimal image with Kubernetes Secrets Store CSI Driver. **EXPERIMENTAL**

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/secrets-store-csi-driver:latest
```

## Using Kubernetes Secrets Store CSI Driver

The Chainguard Secrets Store CSI DRiver image contains the `secrets-store-csi-driver` binary and required utilities.

The driver typically requires a plugin to be installed and configured separately to run.

