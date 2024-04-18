---
title: "Image Overview: tesseract-fips"
linktitle: "tesseract-fips"
type: "article"
layout: "single"
description: "Overview: tesseract-fips Chainguard Image"
date: 2024-04-18 00:43:55
lastmod: 2024-04-18 00:43:55
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/tesseract-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/tesseract-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/tesseract-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/tesseract-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image that contains tesseract
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/tesseract-fips:latest
```


<!--body:start-->
# Usage

tessaract sample Example: OCR an image from a URL to standard output

```
$ docker run --rm \
    -v "${PWD}":/work \
    -w /work \
    cgr.dev/chainguard/tesseract:latest
    https://tesseract-ocr.github.io/tessdoc/images/eurotext.png -
The (quick) [brown] {fox} jumps!
Over the $43,456.78 <lazy> #90 dog
& duck/goose, as 12.5% of E-mail
from aspammer@website.com is spam.
Der ,schnelle” braune Fuchs springt
iiber den faulen Hund. Le renard brun
«rapide» saute par-dessus le chien
paresseux. La volpe marrone rapida
salta sopra il cane pigro. El zorro
marrén rapido salta sobre el perro
perezoso. A raposa marrom ripida
salta sobre o cdo preguigoso.
```
<!--body:end-->

