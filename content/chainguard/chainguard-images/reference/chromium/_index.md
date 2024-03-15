---
title: "Image Overview: chromium"
linktitle: "chromium"
type: "article"
layout: "single"
description: "Overview: chromium Chainguard Image"
date: 2024-03-15 00:51:40
lastmod: 2024-03-15 00:51:40
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/chromium/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/chromium/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/chromium/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/chromium/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal [Chromium](https://chromium.googlesource.com/chromium/src/) container image.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/chromium:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

Running Chromium doesn't require passing any additional parameters to Docker:

```bash
docker run cgr.dev/chainguard/chromium:latest
```

Please note that Chromium is ran in a headless state with the sandbox and GPU access disabled with the flags:

```
--headless --no-sandbox --disable-gpu
```

We run Chromium headless with GPU access disabled due to the container not having GPU access.

Chromium's sandbox has been disabled as the container is sandboxed from the host environment.

This can be overriden via the environment variable `CHROMIUM_USER_FLAGS` though this is unsupported.

<!--body:end-->

