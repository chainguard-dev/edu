---
title: "Image Overview: kubernetes-csi-external-resizer"
type: "article"
description: "Overview: kubernetes-csi-external-resizer Chainguard Image"
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

[cgr.dev/chainguard/kubernetes-csi-external-resizer](https://github.com/chainguard-images/images/tree/main/images/kubernetes-csi-external-resizer)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | August 15th  | `sha256:d65c84d982f14ac82f7325c45a86995726509b79f190b6ab4dba73aa2a826c3b` |
|  `latest-dev` | August 15th  | `sha256:8ce3c0cca0b37e9bcabdc1a39d4ec12a31019d3ef1fb56dc0f1966bdbd1edef4` |



Minimal image with [kubernetes-csi/external-resizer](https://github.com/kubernetes-csi/external-resizer).

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/external-resizer:latest
```

## Using external-resizer

The Chainguard external-resizer image contains the `csi-resizer` controller and is a drop-in replacement for the upstream image.

To try it out, follow the [official installation
instructions](https://github.com/kubernetes-csi/external-resizer/blob/master/README.md#usage).

