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

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | August 26th  | `sha256:eb3c297e5b02c8502d13d9a6c67ec6fc30d25a351b48b0e30caca7c2dc076439` |
|  `latest`     | August 15th  | `sha256:0b7dccc4a7d2105f1a0f4c3510d80ae95d70b105032469db5d12b0595fcb81f0` |



Minimal image with the Virus Total CLI - `vt-cli`.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/vt:latest
```

This image contains the `vt-cli` tool.
Note that you will need an api key for most operations.
This can be configured with `vt init`, with the `--apikey` flag, or with the `VTCLI_APIKEY` environment variable.

