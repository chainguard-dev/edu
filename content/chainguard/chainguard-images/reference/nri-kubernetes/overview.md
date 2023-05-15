---
title: "Image Overview: nri-kubernetes"
type: "article"
description: "Overview: nri-kubernetes Chainguard Images"
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

`stable` [cgr.dev/chainguard/nri-kubernetes](https://github.com/chainguard-images/images/tree/main/images/nri-kubernetes)
| Tags         | Aliases                                            |
|--------------|----------------------------------------------------|
| `latest`     | `3`, `3.11`, `3.11.0`, `3.11.0-r0`                 |
| `latest-dev` | `3-dev`, `3.11-dev`, `3.11.0-dev`, `3.11.0-r0-dev` |



Minimal image with the New Relic Kubernetes Integration binary.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/nri-kubernetes:latest
```

This image is a drop-in replacement for the `nri-kubernetes` image available upstream at `newrelic/nri-kubernetes`.

You can run this in helm with:

```shell
helm upgrade \
    --install \
    newrelic-infrastructure nri-kubernetes/newrelic-infrastructure \
    --set images.integration.registry=cgr.dev \
    --set images.integration.repository=chainguard/nri-kubernetes \
    --set images.integration.tag="latest" \
    --set cluster=$CLUSTER --set licenseKey=$LICENSE_KEY
```

NOTE: This image requires a license key to run properly, which you can obtain from New Relic.

## Testing

The tests for this image also require a license key, which is configured in a secret in Github Actions.

