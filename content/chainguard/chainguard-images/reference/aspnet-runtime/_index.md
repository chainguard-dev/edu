---
title: "Image Overview: aspnet-runtime"
linktitle: "aspnet-runtime"
type: "article"
layout: "single"
description: "Overview: aspnet-runtime Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/aspnet-runtime/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/aspnet-runtime/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/aspnet-runtime/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/aspnet-runtime/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Container image with the latest ASP.NET runtime.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/aspnet-runtime:latest
```


<!--body:start-->
## Usage

The `aspnet-runtime` Chainguard Image contains both the ASP.NET runtime and the .NET core runtime, allowing you to run ASP.NET applications. Note that if your use case depends on running `aspnet-runtime` with a package manager or shell, you can use the `:latest-dev` variant.

For more information, please refer to the official [ASP.NET documentation](https://learn.microsoft.com/en-us/aspnet/core/?view=aspnetcore-8.0).
<!--body:end-->

