---
title: "Image Overview: falcosidekick"
linktitle: "falcosidekick"
type: "article"
layout: "single"
description: "Overview: falcosidekick Chainguard Image"
date: 2024-02-18 00:27:40
lastmod: 2024-02-18 00:27:40
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/falcosidekick/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/falcosidekick/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/falcosidekick/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/falcosidekick/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimalist Wolfi-based image for `falcosidekick`.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/falcosidekick:latest
```
<!--getting:end-->

<!--body:start-->
`falcosidekick` is a simple daemon for connecting Falco to your ecosystem. It takes a Falco events and forward them to different outputs in a fan-out way.

## Usage

`falcosidekick` is the entrypoint for the container image. Run with `help` to view
list of supported commands and options:

```bash
docker run cgr.dev/chainguard/falcosidekick:latest help
```

For more information, refer to the falco documentation:
- [Install and operate falco](https://falco.org/docs/install-operate/running/)
- [Falco GitHub](https://github.com/falcosecurity/falco)
<!--body:end-->

