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
|  `latest-dev` | July 18th    | `sha256:c683b2be3cb42c0abb3d4062729c6b6f8da158a9e726aba7401e802175bb1d5d` |
|  `latest`     | July 14th    | `sha256:da658fe4c12003eb04dba57c7815be98d6aeefb9f3ecb7a798e416d55bfca69c` |
|               | July 12th    | `sha256:6c3729058923030e9d24255aa88e450a5e076b1fe3af06dba17425478a320e4b` |



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

