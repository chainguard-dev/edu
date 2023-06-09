---
title: "Image Overview: http-echo"
type: "article"
description: "Overview: http-echo Chainguard Images"
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

`stable` [cgr.dev/chainguard/http-echo](https://github.com/chainguard-images/images/tree/main/images/http-echo)
| Tags         | Aliases                                         |
|--------------|-------------------------------------------------|
| `latest`     | `0`, `0.2`, `0.2.3`, `0.2.3-r1`                 |
| `latest-dev` | `0-dev`, `0.2-dev`, `0.2.3-dev`, `0.2.3-r1-dev` |



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

