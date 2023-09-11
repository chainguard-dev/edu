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

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest-dev` | September 8th | `sha256:b295c82576000b7931d970297f0ad6c2495c08d5eb6d4f9689e565bc03879ccd` |
|  `latest`     | September 8th | `sha256:e0026b66ab451be12b41e488b5a9945a23d9f2e86b505ea34b8aa8ab8eb0267e` |



Minimal image with the Virus Total CLI - `vt-cli`.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/vt:latest
```

This image contains the `vt-cli` tool.
Note that you will need an api key for most operations.
This can be configured with `vt init`, with the `--apikey` flag, or with the `VTCLI_APIKEY` environment variable.

