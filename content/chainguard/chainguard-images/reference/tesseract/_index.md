---
title: "Image Overview: tesseract"
linktitle: "tesseract"
type: "article"
layout: "single"
description: "Overview: tesseract Chainguard Image"
date: 2024-04-12 00:54:01
lastmod: 2024-04-12 00:54:01
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/tesseract/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/tesseract/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/tesseract/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/tesseract/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image that contains tesseract
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/tesseract:latest
```


<!--body:start-->
# Usage

tessaract sample Example: OCR a eurotext.png file to .txt

```
docker run --rm \
    -v "${PWD}":/work \
    -w /work \
    cgr.dev/chainguard/tesseract:latest
    eurotext.png -
```
<!--body:end-->

