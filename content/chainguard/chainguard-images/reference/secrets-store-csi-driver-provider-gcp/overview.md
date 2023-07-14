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

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest-dev` | July 12th    | `sha256:965caffcda10f6994b63dfcab797150512b1f7f4f17e8f4bbd6adbc17da695b2` |
| `latest`     | July 11th    | `sha256:7778750d5a8091b82420241a9b9821e800ab2391a4d982b6301b3652cf72cb0c` |



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
