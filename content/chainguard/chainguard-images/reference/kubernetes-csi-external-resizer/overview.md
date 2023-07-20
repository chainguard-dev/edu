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
|  `latest-dev` | July 19th    | `sha256:8216b596b9aded0bf8bda896c59082fca7b0fef677ba837dcf79093d10f59f30` |
|  `latest`     | July 14th    | `sha256:9e8ffd1301b16c279b1481f77f2dd18cc75de3c5b192905d237f74c3cb02a48a` |



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

