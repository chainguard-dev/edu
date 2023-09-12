---
title: "Image Overview: paranoia"
type: "article"
description: "Overview: paranoia Chainguard Image"
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

[cgr.dev/chainguard/paranoia](https://github.com/chainguard-images/images/tree/main/images/paranoia)

| Tag (s)       | Last Changed   | Digest                                                                    |
|---------------|----------------|---------------------------------------------------------------------------|
|  `latest-dev` | September 11th | `sha256:9f98cbcedd156d041479da3abed947b6fae655e9baa5bd2442f697200410f025` |
|  `latest`     | September 11th | `sha256:469ae791b786d64c37e630ead0f0a02eeea1286d1cd1ca9ea719d5ee9535b28a` |



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

