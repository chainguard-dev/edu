---
title: "Image Overview: ffmpeg"
linktitle: "ffmpeg"
type: "article"
layout: "single"
description: "Overview: ffmpeg Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/ffmpeg/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/ffmpeg/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/ffmpeg/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/ffmpeg/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image that contains ffmpeg
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/ffmpeg:latest
```


<!--body:start-->
# Usage

Example: convert a .mov file to .mp4

```
docker run --rm \
    -v "${PWD}":/work \
    -w /work \
    cgr.dev/chainguard/ffmpeg:latest
    -i tests/sample.mov \
    tests/sample.mp4
```
<!--body:end-->

