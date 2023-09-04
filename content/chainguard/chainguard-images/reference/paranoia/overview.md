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

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | August 31st  | `sha256:9cd3469b0e879f7a4da919f7c8f6e60d3dac82dc745d0780fa1a79ca38038b38` |
|  `latest-dev` | August 31st  | `sha256:cf6d150757a42d94d7e2f9e13baa6b4f7ca4f064735c3d7ee0391b9195fb1e2e` |



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

