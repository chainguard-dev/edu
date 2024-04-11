---
title: "Image Overview: http-echo"
linktitle: "http-echo"
type: "article"
layout: "single"
description: "Overview: http-echo Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/http-echo/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/http-echo/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/http-echo/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/http-echo/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimalist Wolfi-based http-echo image that echos what you start it with.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/http-echo:latest
```


<!--body:start-->
## Usage

```
CONTAINER=$(docker run -d --rm cgr.dev/chainguard/http-echo:latest -listen=:8080 -text="hello world")
curl localhost:8080
docker kill $CONTAINER
```
<!--body:end-->

