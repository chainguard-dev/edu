---
title: "Image Overview: Http-echo"
type: "article"
description: "Overview: Http-echo Chainguard Image"
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

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest`     | 20 hours ago | `sha256:4b253e3b4e76d298e062f068c11773c04ff71d9fd532de9ff970cee44468f825` |
| `latest-dev` | 20 hours ago | `sha256:e00d2083ad4a3310e6d30c66fb3741e3358d63247133c7f69fe9a920c3cd591e` |



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
