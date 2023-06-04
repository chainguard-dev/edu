---
title: "Image Overview: newrelic-prometheus-configurator"
type: "article"
description: "Overview: newrelic-prometheus-configurator Chainguard Images"
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

`stable` [cgr.dev/chainguard/newrelic-prometheus-configurator](https://github.com/chainguard-images/images/tree/main/images/newrelic-prometheus-configurator)
| Tags         | Aliases                                         |
|--------------|-------------------------------------------------|
| `latest`     | `1`, `1.4`, `1.4.1`, `1.4.1-r0`                 |
| `latest-dev` | `1-dev`, `1.4-dev`, `1.4.1-dev`, `1.4.1-r0-dev` |



Minimal [New Relic Prometheus Configurator](https://github.com/newrelic/newrelic-prometheus-configurator) container image.

## Get It

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/newrelic-prometheus-configurator
```

## Usage

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/newrelic-prometheus-configurator:latest
```

This image is a drop-in replacement for the `newrelic-prometheus-configurator` image available upstream at `newrelic/newrelic-prometheus-configurator`.

You can run this in Helm with:

```bash
helm repo add newrelic-prometheus https://newrelic.github.io/newrelic-prometheus-configurator

helm upgrade --install newrelic newrelic-prometheus/newrelic-prometheus-agent \
    --namespace newrelic \
    --create-namespace \
    --set images.configurator.repository=cgr.dev/chainguard/newrelic-prometheus-configurator \
    --set images.configurator.integration.tag="latest" \
    --set cluster=$CLUSTER \
    --set licenseKey=$LICENSE_KEY
```

NOTE: This image requires a license key to run properly, which you can obtain from New Relic.

## Testing

The tests for this image also require a license key, which is configured in a secret in Github Actions.

