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

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest`     | September 8th | `sha256:ce3f4f8f40e42caf1c1fedf76ceae93dadd8eef76b0dee780a5c6dc823313ee9` |
|  `latest-dev` | September 8th | `sha256:4e9e77fadec4a3d6870f25245345fb7b733507798ce65ade1aa6009d93dd0d5c` |



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

