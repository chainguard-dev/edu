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
|  `latest-dev` | August 3rd   | `sha256:32b6f439cc0414ec9fdfb1bad73d48220e253c33b8a5f5c80b31be1f8711b8e2` |
|  `latest`     | July 26th    | `sha256:acd514cc8bc93381877f6cf9dedc7506373b30f83dffb9fcf0d512fb19c54dbd` |



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

