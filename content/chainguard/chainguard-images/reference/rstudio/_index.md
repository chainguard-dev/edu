---
title: "Image Overview: rstudio"
linktitle: "rstudio"
type: "article"
layout: "single"
description: "Overview: rstudio Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/rstudio/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/rstudio/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/rstudio/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/rstudio/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal [RStudio](https://github.com/rstudio/rstudio) container image.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/rstudio:latest
```


<!--body:start-->
## Running the Image
In order to run RStudio, execute the following command in a terminal:

```bash
docker run -it -p 8787:8787 cgr.dev/chainguard/rstudio:latest
```

The server will now start and the IDE will be accessible at [localhost:8787](http://localhost:8787) in your browser of choice.

<!--body:end-->

