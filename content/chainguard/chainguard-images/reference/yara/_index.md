---
title: "Image Overview: yara"
linktitle: "yara"
type: "article"
layout: "single"
description: "Overview: yara Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/yara/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/yara/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/yara/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/yara/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
The pattern matching swiss knife.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/yara:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

Inspect the crane image manifest using the crane image:

```
docker run --rm cgr.dev/chainguard/crane:latest manifest cgr.dev/chainguard/crane:latest --platform=linux/amd64
```
<!--body:end-->

