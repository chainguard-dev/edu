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
|  `latest-dev` | August 3rd   | `sha256:78d11b3e96ddf344b7baac481270c3f613cd977cbaa9b3d0dbe4811a7ad2b11c` |
|  `latest`     | July 26th    | `sha256:f99fb013a8afaf4b3edfd0ca830b7fb48729333eb323abb8229102c5e1403147` |



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

