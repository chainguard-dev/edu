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
|  `latest-dev` | July 18th    | `sha256:3f7556ba31746b11a99e7134f80363fdc55ae1452157e6753fb48e9ec42b93a4` |
|  `latest`     | July 14th    | `sha256:38b32ee47873545a111054159659085cfe159757da3da3816e763d03055c8e43` |
|               | July 12th    | `sha256:245c57b1c7ff2c75fbd8b742299179dd71660d931659324ebb6f7b084ff93a9d` |
|               | July 4th     | `sha256:c3185d735f3376e178286a0c0a121602b029acde614a8663577ba0dd92cc8889` |



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

