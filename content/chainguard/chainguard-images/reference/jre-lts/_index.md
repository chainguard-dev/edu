---
title: "Image Overview: jre-lts"
linktitle: "jre-lts"
type: "article"
layout: "single"
description: "Overview: jre-lts Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-06-23 00:43:06
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/jre-lts/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jre-lts/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/jre-lts/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jre-lts/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimalist Wolfi-based Java JRE image using [OpenJDK](https://openjdk.org/projects/jdk/). Used for running Java applications.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/jre-lts:latest
```


<!--compatibility:start-->
## Compatibility Notes

### Upcoming Changes

On August 12, 2024 this image will be removed to be consistent with our other images which only make
the latest version available. We recommend you move to use the [jre image](../jdk/README.md). Note
that this image uses a different version of Java, which may require changes to your build system or
application.

Full details are in [this blog post](https://www.chainguard.dev/unchained/updates-to-lts-images-in-chainguard-images-developer-tier).

<!--compatibility:end-->

<!--body:start-->
<!--body:end-->

