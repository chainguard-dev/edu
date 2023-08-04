---
title: "Image Overview: kubernetes-csi-external-attacher"
type: "article"
description: "Overview: kubernetes-csi-external-attacher Chainguard Image"
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

[cgr.dev/chainguard/kubernetes-csi-external-attacher](https://github.com/chainguard-images/images/tree/main/images/kubernetes-csi-external-attacher)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | August 3rd   | `sha256:63637946edcf9d36222d8d534ebb3cfaf3c3348af068f79d50d5eb82cb6b4b76` |
|  `latest`     | July 26th    | `sha256:ac271a34e18ff51ed92112be998ee9e077e5c94e3db8958b8e98d21e7de0de4e` |



Minimal image with [kubernetes-csi/external-attacher](https://github.com/kubernetes-csi/external-attacher).

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/external-attacher:latest
```

## Using external-attacher

The Chainguard external-attacher image contains the `csi-attacher` controller and is a drop-in replacement for the upstream image.

To try it out, follow the [official installation
instructions](https://github.com/kubernetes-csi/external-attacher/blob/master/README.md#usage).

