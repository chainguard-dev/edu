---
title: "Image Overview: nri-prometheus"
type: "article"
description: "Overview: nri-prometheus Chainguard Images"
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

`stable` [cgr.dev/chainguard/nri-prometheus](https://github.com/chainguard-images/images/tree/main/images/nri-prometheus)
| Tags         | Aliases                                            |
|--------------|----------------------------------------------------|
| `latest`     | `2`, `2.18`, `2.18.1`, `2.18.1-r0`                 |
| `latest-dev` | `2-dev`, `2.18-dev`, `2.18.1-dev`, `2.18.1-r0-dev` |



Minimal image with the New Relic Prometheus Integration binary.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/nri-prometheus:latest
```

This image is a drop-in replacement for the `nri-prometheus` image available upstream at `newrelic/nri-prometheus`.

You can run this in helm with:

```shell
helm upgrade \
    --install \
    newrelic-prometheus nri-prometheus/newrelic-prometheus \
    --set image.repository=cgr.dev/chainguard/nri-prometheus \
    --set image.integration.tag="latest" \
    --set cluster=$CLUSTER --set licenseKey=$LICENSE_KEY
```

NOTE: This image requires a license key to run properly, which you can obtain from New Relic.

## Testing

The tests for this image also require a license key, which is configured in a secret in Github Actions.

