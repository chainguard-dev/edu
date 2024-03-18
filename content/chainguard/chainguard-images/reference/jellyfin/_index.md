---
title: "Image Overview: jellyfin"
linktitle: "jellyfin"
type: "article"
layout: "single"
description: "Overview: jellyfin Chainguard Image"
date: 2024-03-18 00:56:27
lastmod: 2024-03-18 00:56:27
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/jellyfin/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/jellyfin/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/jellyfin/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/jellyfin/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal [Jellyfin](https://github.com/jellyfin/jellyfin) container image.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/jellyfin:latest
```
<!--getting:end-->

<!--body:start-->
## Running the Image
To get started, open a terminal and run:

```bash
docker run -p 8096:8096 cgr.dev/chainguard/jellyfin
```

The Jellyfin Web UI will start on port 8096. To check availability, run:

```bash
curl -vsL localhost:8096/health
```

If you see `HEALTHCHECK=healthy`, the Web UI is available for use.

For any additional configuration, please see Jellyfin's official [container](https://jellyfin.org/docs/general/installation/container/) documentation.

<!--body:end-->

