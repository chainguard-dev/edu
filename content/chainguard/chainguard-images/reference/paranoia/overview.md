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

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest-dev` | September 6th | `sha256:9ba3081b2701056938c94393a0c66a2e595bcb06ab57dd7ad951e33908c30d93` |
|  `latest`     | September 4th | `sha256:18587724249a9174a6cb976a58d93f2d777cdc21c94c6afd756e1d896fa34178` |



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

