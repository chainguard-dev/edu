---
title: "Image Overview: Ffmpeg"
type: "article"
description: "Overview: Ffmpeg Chainguard Image"
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

[cgr.dev/chainguard/ffmpeg](https://github.com/chainguard-images/images/tree/main/images/ffmpeg)

| Tag      | Last Updated | Digest                                                                    |
|----------|--------------|---------------------------------------------------------------------------|
| `latest` | 20 hours ago | `sha256:d2d12532f835bdb7a89c15ef79e74dc92f38b27b95e688c2fa5863d13f626d32` |



This is an image that contains ffmpeg.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/ffmpeg:latest
```

# Usage

Example: convert a .mov file to .mp4

```
docker run --rm \
    -v "${PWD}":/work \
    -w /work \
    cgr.dev/chainguard/ffmpeg:latest
    -i tests/sample.mov \
    tests/sample.mp4
```
