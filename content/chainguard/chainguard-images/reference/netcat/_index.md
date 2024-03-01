---
title: "Image Overview: netcat"
linktitle: "netcat"
type: "article"
layout: "single"
description: "Overview: netcat Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/netcat/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/netcat/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/netcat/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/netcat/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image for Debian port of OpenBSD's netcat. **EXPERIMENTAL**
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/netcat:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

```
docker run --rm -ti cgr.dev/chainguard/netcat -zv google.com 443
```

See [here](https://manpages.debian.org/unstable/netcat-openbsd/nc.1.en.html) for more invocation details.
<!--body:end-->

