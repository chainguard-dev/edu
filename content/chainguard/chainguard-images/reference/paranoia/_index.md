---
title: "Image Overview: paranoia"
linktitle: "paranoia"
type: "article"
layout: "single"
description: "Overview: paranoia Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/paranoia/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/paranoia/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/paranoia/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/paranoia/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimalist Wolfi-based paranoia image for inspecting certificate authorities in container images
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/paranoia:latest
```


<!--body:start-->
## Usage

Paranoia can be used to list out the certificates in a container image:

```
docker run --rm cgr.dev/chainguard/paranoia:latest export alpine:latest
```
<!--body:end-->

