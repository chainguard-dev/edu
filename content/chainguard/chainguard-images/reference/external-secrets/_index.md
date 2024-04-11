---
title: "Image Overview: external-secrets"
linktitle: "external-secrets"
type: "article"
layout: "single"
description: "Overview: external-secrets Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/external-secrets/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/external-secrets/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/external-secrets/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/external-secrets/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal Kubernetes [External Secrets Operator](https://external-secrets.io/) image
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/external-secrets:latest
```


<!--body:start-->
## Usage

This image is a drop-in replacement for the upstream image.
You can run it using the helm chart with:

```shell

$ helm repo add external-secrets https://charts.external-secrets.io
$ helm install external-secrets \
   external-secrets/external-secrets \
    -n external-secrets \
    --set image.repository=cgr.dev/chainguard/external-secrets  \
    --set image.tag=latest \
    --create-namespace
    <other configuration parameters here>
```

See the [configuration](https://github.com/external-secrets/external-secrets/tree/main/deploy/charts/external-secrets) docs for more examples.
<!--body:end-->

