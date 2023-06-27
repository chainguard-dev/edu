---
title: "Image Overview: Newrelic-infrastructure-bundle"
type: "article"
description: "Overview: Newrelic-infrastructure-bundle Chainguard Image"
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

[cgr.dev/chainguard/newrelic-infrastructure-bundle](https://github.com/chainguard-images/images/tree/main/images/newrelic-infrastructure-bundle)


Minimal [newrelic-infrastructure-bundle](https://github.com/newrelic/infrastructure-bundle) container image.

## Get It

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/newrelic-infrastructure-bundle
```

## Usage

This image is a drop-in replacement for the `newrelic-infrastructure-bundle` project that image known as and available upstream at `newrelic/infrastructure-bundle`.

You can run this in Helm with:

```shell
helm repo add nri-kubernetes https://newrelic.github.io/nri-kubernetes

helm upgrade --install newrelic-infrastructure-bundle nri-kubernetes/newrelic-infrastructure \
    --set images.agent.registry=cgr.dev \
    --set images.agent.repository=chainguard/newrelic-infrastructure-bundle \
    --set images.agent.tag=latest \
    --set images.integration.registry=cgr.dev \
    --set images.integration.repository=chainguard/nri-kube-events \
    --set images.integration.tag="latest" \
    --set cluster=$CLUSTER --set licenseKey=$LICENSE_KEY
```

NOTE: This image requires a license key to run properly, which you can obtain from New Relic.

## Testing

The tests for this image also require a license key, which is configured in a secret in Github Actions.
