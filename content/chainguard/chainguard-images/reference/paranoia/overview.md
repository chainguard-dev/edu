---
title: "Image Overview: paranoia"
type: "article"
description: "Overview: paranoia Chainguard Images"
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

`stable` [cgr.dev/chainguard/paranoia](https://github.com/chainguard-images/images/tree/main/images/paranoia)
| Tags         | Aliases                                         |
|--------------|-------------------------------------------------|
| `latest`     | `0`, `0.2`, `0.2.1`, `0.2.1-r0`                 |
| `latest-dev` | `0-dev`, `0.2-dev`, `0.2.1-dev`, `0.2.1-r0-dev` |



Minimalist Wolfi-based paranoia image for inspecting certificate authorities in container images

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/paranoia:latest
```

## Usage

Paranoia can be used to list out the certificates in a container image:

```
docker run --rm cgr.dev/chainguard/paranoia:latest export alpine:latest
```

