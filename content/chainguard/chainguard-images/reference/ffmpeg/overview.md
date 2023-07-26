---
title: "Image Overview: ffmpeg"
type: "article"
description: "Overview: ffmpeg Chainguard Image"
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

| Tag (s)   | Last Changed | Digest                                                                    |
|-----------|--------------|---------------------------------------------------------------------------|
|  `latest` | July 24th    | `sha256:2ca11016f0f6d24c1bc7f690110e1f8870e539bdffe8ca696904522ce296907d` |



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

