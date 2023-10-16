---
title: "Image Overview: dynamic-localpv-provisioner"
linktitle: "dynamic-localpv-provisioner"
type: "article"
layout: "single"
description: "Overview: dynamic-localpv-provisioner Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/dynamic-localpv-provisioner/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/dynamic-localpv-provisioner/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/dynamic-localpv-provisioner/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/dynamic-localpv-provisioner/provenance_info/" >}}
{{</ tabs >}}



Minimal images for dynamic-localpv-provisioner

## Get It

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/dynamic-localpv-provisioner:latest
```

## Testing

Fortunately, we have a Helm Chart ready-to-use for testing this image. 

You can find it [here](https://github.com/openebs/dynamic-localpv-provisioner/blob/develop/deploy/helm/charts/README.md).

Basically, all you need to do is running the commands below to test the application:

```shell
helm repo add openebs-localpv https://openebs.github.io/dynamic-localpv-provisioner
helm repo update
helm install openebs-localpv openebs-localpv/dynamic-localpv-provisioner \
  --set localpv.image.registry=cgr.dev/ \
  --set localpv.image.repository=chainguard/dynamic-localpv-provisioner \
  --set localpv.image.tag=latest
```

Once you run the commands above, you will end up having the application running on your cluster.
