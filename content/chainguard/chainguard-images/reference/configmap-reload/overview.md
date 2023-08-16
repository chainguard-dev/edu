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
|  `latest-dev` | August 15th  | `sha256:a062035553cc01c9f3dfba074c81f46d5c8bd3487f36ea16aee52b7927da3f45` |
|  `latest`     | August 15th  | `sha256:c5612f44fb7a7d3011d05b2f7eec21ce0cee21d74a8d3f7d245033055f68db74` |



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

