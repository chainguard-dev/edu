---
title: "Image Overview: mdbook"
linktitle: "mdbook"
type: "article"
layout: "single"
description: "Overview: mdbook Chainguard Image"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/mdbook/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/mdbook/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/mdbook/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/mdbook/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image that contains [mdbook](https://rust-lang.github.io/mdBook/).
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/mdbook:latest
```
<!--getting:end-->

<!--body:start-->
# Usage

Example: build an mdbook project in the `/work` directory

```
docker run --rm \
    -v "${PWD}":/work \
    -w /work \
    cgr.dev/chainguard/mdbook:latest
    init --force --title chainguard-images --ignore git
```
<!--body:end-->

