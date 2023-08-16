---
title: "Image Overview: secrets-store-csi-driver-provider-gcp"
type: "article"
description: "Overview: secrets-store-csi-driver-provider-gcp Chainguard Image"
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

[cgr.dev/chainguard/secrets-store-csi-driver-provider-gcp](https://github.com/chainguard-images/images/tree/main/images/secrets-store-csi-driver-provider-gcp)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | August 15th  | `sha256:e5facd740b4aca032cb2565eb4d2d2667c96d4b0c97d4fd136b58d8506ffedf1` |
|  `latest-dev` | August 15th  | `sha256:de6352012105bf7c38d60da3e6f8f5b293535e99f7b4131589a638e4463b248e` |



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

