---
title: "Image Overview: crane"
type: "article"
description: "Overview: crane Chainguard Image"
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

| Tag (s)       | Last Changed   | Digest                                                                    |
|---------------|----------------|---------------------------------------------------------------------------|
|  `latest-dev` | September 11th | `sha256:773cab49a8f9e73705293022b8fbd1312dd452aeb4e960a97c1bbf44e4625795` |
|  `latest`     | September 11th | `sha256:0f70f5faaa35170944f294cb0d0a1cf64d473c8717315aa811690213bd6a36cb` |



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

