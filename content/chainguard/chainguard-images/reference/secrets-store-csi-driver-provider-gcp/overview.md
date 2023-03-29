---
title: "Image Overview: secrets-store-csi-driver-provider-gcp"
type: "article"
description: "Overview: secrets-store-csi-driver-provider-gcp Chainguard Images"
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

`experimental` [cgr.dev/chainguard/secrets-store-csi-driver-provider-gcp](https://github.com/chainguard-images/images/tree/main/images/secrets-store-csi-driver-provider-gcp)
| Tags         | Aliases                                         |
|--------------|-------------------------------------------------|
| `latest`     | `1`, `1.2`, `1.2.0`, `1.2.0-r0`                 |
| `latest-dev` | `1-dev`, `1.2-dev`, `1.2.0-dev`, `1.2.0-r0-dev` |



Minimal image with the Kubernetes Secrets Store CSI Driver GCP Plugin. **EXPERIMENTAL**

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/secrets-store-csi-driver-provider-gcp:latest
```

## Using Secrets Store CSI Driver GCP Plugin

The Chainguard Secrets Store CSI Driver GCP Plugin image contains the `secrets-store-csi-driver-provider-gcp` binary and required utilities.

```shell
$ docker run cgr.dev/chainguard/secrets-store-csi-driver-provider-gcp
```
