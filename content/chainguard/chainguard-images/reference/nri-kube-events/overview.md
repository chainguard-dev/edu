---
title: "Image Overview: nri-kube-events"
type: "article"
description: "Overview: nri-kube-events Chainguard Images"
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

`stable` [cgr.dev/chainguard/nri-kube-events](https://github.com/chainguard-images/images/tree/main/images/nri-kube-events)
| Tags         | Aliases                                         |
|--------------|-------------------------------------------------|
| `latest`     | `2`, `2.1`, `2.1.0`, `2.1.0-r2`                 |
| `latest-dev` | `2-dev`, `2.1-dev`, `2.1.0-dev`, `2.1.0-r2-dev` |



Minimal image with the [nri-kube-events](https://github.com/newrelic/nri-kube-events) binary.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/nri-kube-events:latest
```

This image is a drop-in replacement for the `nri-kube-events` image available upstream at `newrelic/nnri-kube-events`.

## Usage

```
Usage of /usr/bin/nri-kube-events:
  -config string
        location of the configuration file (default "config.yaml")
  -kubeconfig string
        location of the k8s configuration file. Usually in ~/.kube/config
  -loglevel string
        Log level: [warning, info, debug] (default "info")
  -promaddr string
        Address to serve prometheus metrics on (default "0.0.0.0:8080")
```

You can run this in helm with:

```shell
helm repo add nri-kube-events https://newrelic.github.io/nri-kube-events
helm upgrade \
    --install \
    nri-kube-events nri-kube-events/nri-kube-events \
    --set images.integration.registry=cgr.dev \
    --set images.integration.repository=chainguard/nri-kube-events \
    --set images.integration.tag="latest" \
    --set cluster=$CLUSTER --set licenseKey=$LICENSE_KEY
```

NOTE: This image requires a license key to run properly, which you can obtain from New Relic.

## Testing

The tests for this image also require a license key, which is configured in a secret in Github Actions.

