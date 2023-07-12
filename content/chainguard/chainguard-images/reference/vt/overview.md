---
title: "Image Overview: Vt"
type: "article"
description: "Overview: Vt Chainguard Image"
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

[cgr.dev/chainguard/vt](https://github.com/chainguard-images/images/tree/main/images/vt)

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest`     | 19 hours ago | `sha256:e97e875d68d73db197a0bdcbacbff74894ce07a7ff8232d92d268b171ad6c9fd` |
| `latest-dev` | 19 hours ago | `sha256:21509fcb8f7fc3e477e58ed00bfc5b342c37c4f2c2e024a1f59dfec5b72f4596` |



Minimal image with the Virus Total CLI - `vt-cli`.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/vt:latest
```

This image contains the `vt-cli` tool.
Note that you will need an api key for most operations.
This can be configured with `vt init`, with the `--apikey` flag, or with the `VTCLI_APIKEY` environment variable.
