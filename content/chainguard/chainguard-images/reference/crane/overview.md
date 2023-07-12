---
title: "Image Overview: Crane"
type: "article"
description: "Overview: Crane Chainguard Image"
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

[cgr.dev/chainguard/crane](https://github.com/chainguard-images/images/tree/main/images/crane)

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest-dev` | 20 hours ago | `sha256:d0bb136de40bc83245a8a1ecd87cf25dfbf2ca0c3466f74debdccbefada78558` |
| `latest`     | 20 hours ago | `sha256:4e077e6e54d5b2b21a27528e4dfda81e9fa3399d7793e3b35454ac229d0980dc` |



Minimalist Wolfi-based crane image for interacting with registries.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/crane:latest
```

## Usage

Inspect the crane image manifest using the crane image:

```
docker run --rm cgr.dev/chainguard/crane:latest manifest cgr.dev/chainguard/crane:latest
```
