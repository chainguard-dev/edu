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
|  `latest-dev` | July 18th    | `sha256:48e1257b5aaaaa4b00d7973850427a3542ee4db74102aa3d3b6fda1d17935004` |
|  `latest`     | July 14th    | `sha256:d77a1f80f91a2e4d199e1c612a65c6f49f1c01d1c6e0099c5055d0efe72494f0` |
|               | July 12th    | `sha256:965caffcda10f6994b63dfcab797150512b1f7f4f17e8f4bbd6adbc17da695b2` |



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

