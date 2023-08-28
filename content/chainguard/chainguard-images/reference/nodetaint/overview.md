---
title: "Image Overview: nodetaint"
type: "article"
description: "Overview: nodetaint Chainguard Image"
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

[cgr.dev/chainguard/nodetaint](https://github.com/chainguard-images/images/tree/main/images/nodetaint)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | August 26th  | `sha256:ab09adc3c8126d6fac41ead7161b682a016a00c0352f7ed9665b9da3a2936a78` |
|  `latest`     | August 15th  | `sha256:bf3db24cb559efdbc6e3635a3eab7b9bb28debf18bc4a6253a9d2bacd3615b43` |



Minimal [nodetaint](https://github.com/wish/nodetaint) container image.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/nodetaint
```

## Usage

To install on you Kubernetes, you can use the `Helm`:

```shell
git clone https://github.com/wish/nodetaint && cd nodetaint

helm install nodetaint ./chart \
  --namespace nodetaint \
  --create-namespace \
  --set image.registry=${IMAGE_REGISTRY} \
  --set image.repository=${IMAGE_REPOSITORY} \
  --set image.tag=${IMAGE_TAG}
```

