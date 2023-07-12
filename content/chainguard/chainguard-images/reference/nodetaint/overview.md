---
title: "Image Overview: Nodetaint"
type: "article"
description: "Overview: Nodetaint Chainguard Image"
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

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest`     | 19 hours ago | `sha256:6a47bf8d0b4d970e4597dd0ba98765e03cfee9a1ebd9bf768e4e38b9d9036981` |
| `latest-dev` | 19 hours ago | `sha256:d81eff434b9bb277469281c29b253f67ba029dc5466548d55676b852b810af15` |



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
