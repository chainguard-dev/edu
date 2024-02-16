---
title: "Image Overview: cc-dynamic"
linktitle: "cc-dynamic"
type: "article"
layout: "single"
description: "Overview: cc-dynamic Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-02-16 00:30:51
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/cc-dynamic/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/cc-dynamic/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/cc-dynamic/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/cc-dynamic/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Base image with just enough to run arbitrary binaries that may require gcc or cc libraries, typically C++ or Rust binaries.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/cc-dynamic:latest
```
<!--getting:end-->

<!--body:start-->

This image is meant to be used as just a base image only. It does not contain any programs that can be run, other than `/sbin/ldconfig`.

You must bring your own artifacts to use this image, e.g. with a Docker multi-stage build. If you want locale support other than `C.UTF-8`, you must bring your own locale data as well. This may change in the future based on user feedback.

This image is deprecated.  Use the `glibc-dynamic` image instead which is designed to cover the same use cases.
<!--body:end-->

