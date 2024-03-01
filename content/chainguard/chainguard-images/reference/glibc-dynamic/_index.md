---
title: "Image Overview: glibc-dynamic"
linktitle: "glibc-dynamic"
type: "article"
layout: "single"
description: "Overview: glibc-dynamic Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-03-01 12:14:22
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/glibc-dynamic/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/glibc-dynamic/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/glibc-dynamic/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/glibc-dynamic/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Base image with just enough to run arbitrary glibc binaries.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/glibc-dynamic:latest
```
<!--getting:end-->

<!--body:start-->
This image is meant to be used as just a base image only. It does not contain any programs that can be run, other than `/sbin/ldconfig`.

You must bring your own artifacts to use this image, e.g. with a Docker multi-stage build. If you want locale support other than `C.UTF-8`, you must bring your own locale data as well. This may change in the future based on user feedback.
<!--body:end-->

