---
title: "Image Overview: vt"
type: "article"
description: "Overview: vt Chainguard Image"
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

| Tag (s)       | Last Changed   | Digest                                                                    |
|---------------|----------------|---------------------------------------------------------------------------|
|  `latest-dev` | September 11th | `sha256:24f67f31ce25bad9215b738cc043c38b0db9522921e26a04ee2cf0cbd4d71c5f` |
|  `latest`     | September 11th | `sha256:5daf61f50be04940aefcdac54e25e4e9ed371a28a682085df114e96ab93fdd32` |



Minimal image with the Virus Total CLI - `vt-cli`.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/vt:latest
```

This image contains the `vt-cli` tool.
Note that you will need an api key for most operations.
This can be configured with `vt init`, with the `--apikey` flag, or with the `VTCLI_APIKEY` environment variable.

