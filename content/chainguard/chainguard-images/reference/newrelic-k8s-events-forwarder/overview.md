---
title: "Image Overview: newrelic-k8s-events-forwarder"
type: "article"
description: "Overview: newrelic-k8s-events-forwarder Chainguard Images"
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

`stable` [cgr.dev/chainguard/newrelic-k8s-events-forwarder](https://github.com/chainguard-images/images/tree/main/images/newrelic-k8s-events-forwarder)
| Tags         | Aliases |
|--------------|---------|
| `latest`     |         |
| `latest-dev` |         |



Minimal [New Relic Infrastructure Agent](https://github.com/newrelic/infrastructure-agent) (newrelic/k8s-events-forwarder) container image.

## Get It

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/newrelic-k8s-events-forwarder
```

## Usage

This image is a drop-in replacement for the `newrelic/infrastructure-agent` project that image known as and available upstream at `newrelic/newrelic-k8s-events-forwarder`.

You can run this in Helm with:

```shell
helm repo add nri-kube-events https://newrelic.github.io/nri-kube-events

helm upgrade --install newrelic-k8s-events-forwarder nri-kube-events/nri-kube-events \
    --set images.agent.registry=cgr.dev \
    --set images.agent.repository=chainguard/newrelic-k8s-events-forwarder \
    --set images.agent.tag=latest \
    --set images.integration.registry=cgr.dev \
    --set images.integration.repository=chainguard/nri-kube-events \
    --set images.integration.tag="latest" \
    --set cluster=$CLUSTER --set licenseKey=$LICENSE_KEY
```

NOTE: This image requires a license key to run properly, which you can obtain from New Relic.

## Testing

The tests for this image also require a license key, which is configured in a secret in Github Actions.

