---
title: "Image Overview: crane"
linktitle: "crane"
type: "article"
layout: "single"
description: "Overview: crane Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/crane/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/crane/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/crane/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/crane/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimalist Wolfi-based crane image for interacting with registries.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/crane:latest
```


<!--body:start-->
## Usage

Inspect the crane image manifest using the crane image:

```
docker run --rm cgr.dev/chainguard/crane:latest manifest cgr.dev/chainguard/crane:latest --platform=linux/amd64
```
<!--body:end-->

