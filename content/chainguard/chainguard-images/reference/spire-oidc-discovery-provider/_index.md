---
title: "Image Overview: spire-oidc-discovery-provider"
linktitle: "spire-oidc-discovery-provider"
type: "article"
layout: "single"
description: "Overview: spire-oidc-discovery-provider Chainguard Image"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/spire-oidc-discovery-provider/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/spire-oidc-discovery-provider/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/spire-oidc-discovery-provider/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/spire-oidc-discovery-provider/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimalist Wolfi-based `spire` images.
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/spire:latest
```
<!--getting:end-->

<!--compatibility:start-->
## Compatibility Notes**Note**: Unlike most other Chainguard images, the `spire-agent` image must run as root.
This is due to a constraint in the way it is typically deployed into Kubernetes clusters.
See https://github.com/spiffe/spire/issues/1862 for more context.
<!--compatibility:end-->

<!--body:start-->

**Note**: Unlike most other Chainguard images, the `spire-agent` image must run as root.
This is due to a constraint in the way it is typically deployed into Kubernetes clusters.
See https://github.com/spiffe/spire/issues/1862 for more context.
<!--body:end-->

