---
title: "Image Overview: falcosidekick-fips"
linktitle: "falcosidekick-fips"
type: "article"
layout: "single"
description: "Overview: falcosidekick-fips Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/falcosidekick-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/falcosidekick-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/falcosidekick-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/falcosidekick-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimalist Wolfi-based image for `falcosidekick`.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/falcosidekick-fips:latest
```


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

