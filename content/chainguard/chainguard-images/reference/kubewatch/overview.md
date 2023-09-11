---
title: "Image Overview: kubewatch"
type: "article"
description: "Overview: kubewatch Chainguard Image"
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

[cgr.dev/chainguard/kubewatch](https://github.com/chainguard-images/images/tree/main/images/kubewatch)

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest`     | September 8th | `sha256:23c97ed513e8b6c367679145fb7b486fc21eac591e0d654581677790864fc901` |
|  `latest-dev` | September 8th | `sha256:3c12f3760271a0d1a7ecf1bcb9e3a970cdb1d1caa45c4bea555a54706273b085` |



[kubewatch](https://github.com/robusta-dev/kubewatch) is a Kubernetes watcher that publishes notification to available collaboration hubs/notification channels. Run it in your k8s cluster, and you will get event notifications through webhooks.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/kubewatch
```

## Using kubewatch

This image is a drop-in replacement for the upstream image.
You can run it using the official helm chart with:

```shell
$ helm repo add robusta https://robusta-charts.storage.googleapis.com
$ helm repo update
$ helm install kubewatch robusta/kubewatch \
    --set image.repository=cgr.dev/chainguard/kubewatch \
    --set image.tag=latest
    <other configuration parameters here>
```

