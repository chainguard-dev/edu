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
|  `latest-dev` | August 3rd   | `sha256:22d8e488fe92c3bd52b99e805be5dbc30f098ce4e6adb6e4b6bd09be40a7c92d` |
|  `latest`     | August 3rd   | `sha256:47c067f9a621c123d67468e9d31ce82f710531b0bf6a825659d2d8f3d33edb73` |



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

