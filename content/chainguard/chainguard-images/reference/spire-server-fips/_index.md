---
title: "Image Overview: spire-server-fips"
linktitle: "spire-server-fips"
type: "article"
layout: "single"
description: "Overview: spire-server-fips Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/spire-server-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/spire-server-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/spire-server-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/spire-server-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimalist Wolfi-based `spire` images.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/spire-server-fips:latest
```


<!--compatibility:start-->
## Compatibility Notes

**Note**: Unlike most other Chainguard images, the `spire-agent` image must run as root.
This is due to a constraint in the way it is typically deployed into Kubernetes clusters.
See https://github.com/spiffe/spire/issues/1862 for more context.

<!--compatibility:end-->

<!--body:start-->

**Note**: Unlike most other Chainguard images, the `spire-agent` image must run as root.
This is due to a constraint in the way it is typically deployed into Kubernetes clusters.
See https://github.com/spiffe/spire/issues/1862 for more context.
<!--body:end-->

