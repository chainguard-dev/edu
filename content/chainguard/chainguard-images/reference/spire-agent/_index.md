---
title: "Image Overview: spire-agent"
linktitle: "spire-agent"
type: "article"
layout: "single"
description: "Overview: spire-agent Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/spire-agent/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/spire-agent/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/spire-agent/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/spire-agent/provenance_info/" >}}
{{</ tabs >}}



Minimalist Wolfi-based `spire` images.

**Note**: Unlike most other Chainguard images, the `spire-agent` image must run as root.
This is due to a constraint in the way it is typically deployed into Kubernetes clusters.
See https://github.com/spiffe/spire/issues/1862 for more context.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/spire-agent:latest
docker pull cgr.dev/chainguard/spire-server:latest
```

