---
title: "Image Overview: spire-agent-fips"
linktitle: "spire-agent-fips"
type: "article"
layout: "single"
description: "Overview: spire-agent-fips Chainguard Image"
date: 2024-02-29 16:25:55
lastmod: 2024-02-29 16:25:55
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/spire-agent-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/spire-agent-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/spire-agent-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/spire-agent-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimalist Wolfi-based `spire` images.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/spire:latest
```
<!--getting:end-->

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

