---
title: "Image Overview: Nri-prometheus"
type: "article"
description: "Overview: Nri-prometheus Chainguard Image"
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

[cgr.dev/chainguard/nri-prometheus](https://github.com/chainguard-images/images/tree/main/images/nri-prometheus)


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
