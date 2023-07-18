---
title: "Image Overview: mdbook"
type: "article"
description: "Overview: mdbook Chainguard Image"
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

[cgr.dev/chainguard/mdbook](https://github.com/chainguard-images/images/tree/main/images/mdbook)

| Tag (s)   | Last Changed | Digest                                                                    |
|-----------|--------------|---------------------------------------------------------------------------|
|  `latest` | July 18th    | `sha256:91040a61249724af59e45349e98fd6460c8d3deaea7107451cb097dd920bb2c1` |
|           | July 11th    | `sha256:91bffe9e1ffe5f8a762013c73ea8390f87e0d8b6eff53ee66b855c4118b93df3` |
|           | June 26th    | `sha256:a634e056063a8a423313578dc7cd36c3f57f7bbe5666a0c52bd208781e305038` |



This is an image that contains mdbook.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/mdbook:latest
```

# Usage

Example: build an mdbook project in the `/work` directory

```
docker run --rm \
    -v "${PWD}":/work \
    -w /work \
    cgr.dev/chainguard/mdbook:latest
    init --force --title chainguard-images --ignore git
```

