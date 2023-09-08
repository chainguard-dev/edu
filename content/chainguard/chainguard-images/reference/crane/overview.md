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

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest`     | September 7th | `sha256:8279a2cf073f663be9be852e9b92c986479eb580962676a71152cd85f90cad70` |
|  `latest-dev` | September 7th | `sha256:516ff92c008337dd131ef2159d08a508231f948a4987e3d6c8a71f3136f8ac19` |



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

