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
|  `latest`     | August 19th  | `sha256:df987e81c179412327aef3f303e38c21b10788e6529eae8be5b97a3cc70c1413` |
|  `latest-dev` | August 19th  | `sha256:4f3c7b5809ef7d1a4908332c104e92a4c477db65a16cd8f8041b3d8818d84b9f` |



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

