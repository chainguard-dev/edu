---
title: "Image Overview: bincapz"
linktitle: "bincapz"
type: "article"
layout: "single"
description: "Overview: bincapz Chainguard Image"
date: 2024-04-01 00:38:36
lastmod: 2024-04-01 00:38:36
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/bincapz/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/bincapz/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/bincapz/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/bincapz/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Enumerate binary capabilities, including malicious behaviors.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/bincapz:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

Inspect the crane image manifest using the crane image:

```
docker run --rm cgr.dev/chainguard/crane:latest manifest cgr.dev/chainguard/crane:latest --platform=linux/amd64
```
<!--body:end-->

