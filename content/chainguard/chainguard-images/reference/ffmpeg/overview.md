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
|  `latest` | July 26th    | `sha256:25b89e6b176ec3c922b06e26fe0eb8379a6e581889e7cf55e119e7b3d35b6781` |



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

