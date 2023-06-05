---
title: "Image Overview: spire-agent"
type: "article"
description: "Overview: spire-agent Chainguard Images"
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

`stable` [cgr.dev/chainguard/spire-agent](https://github.com/chainguard-images/images/tree/main/images/spire-agent)
| Tags         | Aliases                                         |
|--------------|-------------------------------------------------|
| `latest`     | `1`, `1.6`, `1.6.4`, `1.6.4-r2`                 |
| `latest-dev` | `1-dev`, `1.6-dev`, `1.6.4-dev`, `1.6.4-r2-dev` |



Minimalist Wolfi-based `spire-agent` image.

**Note**: Unlike most other Chainguard images, the `spire-agent` image must run as root.
This is due to a constraint in the way it is typically deployed into Kubernetes clusters.
See https://github.com/spiffe/spire/issues/1862 for more context.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/spire-agent:latest
```

