---
title: "Image Overview: vt"
linktitle: "vt"
type: "article"
layout: "single"
description: "Overview: vt Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/vt/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/vt/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/vt/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/vt/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image with the Virus Total CLI - `vt-cli`.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/vt:latest
```
<!--getting:end-->

<!--body:start-->
This image contains the `vt-cli` tool.
Note that you will need an api key for most operations.
This can be configured with `vt init`, with the `--apikey` flag, or with the `VTCLI_APIKEY` environment variable.
<!--body:end-->

