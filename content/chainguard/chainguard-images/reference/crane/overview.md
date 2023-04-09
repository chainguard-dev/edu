---
title: "Image Overview: crane"
type: "article"
description: "Overview: crane Chainguard Images"
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

`experimental` [cgr.dev/chainguard/crane](https://github.com/chainguard-images/images/tree/main/images/crane)
| Tags         | Aliases                                            |
|--------------|----------------------------------------------------|
| `latest`     | `0`, `0.14`, `0.14.0`, `0.14.0-r1`                 |
| `latest-dev` | `0-dev`, `0.14-dev`, `0.14.0-dev`, `0.14.0-r1-dev` |



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

