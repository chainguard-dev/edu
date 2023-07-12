---
title: "Image Overview: Paranoia"
type: "article"
description: "Overview: Paranoia Chainguard Image"
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

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest-dev` | 19 hours ago | `sha256:d2627839afc95bd763445c91a4b2cebb7a35f2a332909a42be0fe165e72f1b51` |
| `latest`     | 19 hours ago | `sha256:9f3f2e78044349ec4692ceab3bd1d1f2e94be00a6cb58674421fea0b54c35112` |



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
