---
title: "Image Overview: Configmap-reload"
type: "article"
description: "Overview: Configmap-reload Chainguard Image"
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

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest-dev` | 20 hours ago | `sha256:f1cbccfdf58f54b1724dceb377d30af82f7bce4369ee4e5015f1555f1dae24f6` |
| `latest`     | 20 hours ago | `sha256:0b15bd64ae9f1ddc21cf9afc518f4f90548caf8a440e7d5280c78f65a4e88e51` |



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
