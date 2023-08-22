---
title: "Image Overview: http-echo"
type: "article"
description: "Overview: http-echo Chainguard Image"
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

[cgr.dev/chainguard/http-echo](https://github.com/chainguard-images/images/tree/main/images/http-echo)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | August 15th  | `sha256:e2378c1d554b559e5a8e9359d3b0f764a1ba180836429b883726ff69dad727d6` |
|  `latest`     | August 15th  | `sha256:6d5cabbdac213c072feafe42dcaf475d10d0d8fbb0eb5c26b6ebdcd6526ee5b8` |



Minimalist Wolfi-based http-echo image that echos what you start it with.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/http-echo:latest
```

## Usage

```
CONTAINER=$(docker run -d --rm cgr.dev/chainguard/http-echo:latest -listen=:8080 -text="hello world")
curl localhost:8080
docker kill $CONTAINER
```

