---
title: "Image Overview: configmap-reload"
type: "article"
description: "Overview: configmap-reload Chainguard Image"
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

[cgr.dev/chainguard/configmap-reload](https://github.com/chainguard-images/images/tree/main/images/configmap-reload)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 27th    | `sha256:eea92823310011e7c8d1e95cc2a774c305d6f56f003fe7f23698628d23a14186` |
|  `latest`     | July 26th    | `sha256:52ef9b9bfddc008fdaf93e6365aed4031dce915d5e3b3cf59826caccb9bd5912` |



Kubernetes ConfigMap Reload

`configmap-reload` is a simple binary to trigger a reload when Kubernetes ConfigMaps or Secrets, mounted into pods, are updated.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/configmap-reload:latest
```

## Usage

This image is a drop-in replacement for the upstream image.
You can run it using the helm chart with:

```shell
$ helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
$ helm install my-release prometheus-community/alertmanager \
    --set configmapReload.enabled=true \
    --set configmapReload.image=cgr.dev/chainguard/configmap-reload \
    --set image.tag=latest
    <other configuration parameters here>
```

