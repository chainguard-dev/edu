---
title: "Image Overview: Kubewatch"
type: "article"
description: "Overview: Kubewatch Chainguard Image"
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

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest`     | 19 hours ago | `sha256:a05833ceac9e0084d2c9dac403ef349c4092ec5643a60a8e482e573724b8769a` |
| `latest-dev` | 19 hours ago | `sha256:321e0a1267ec6cb68df213ec512e5764afebb5b1c11047cca027449c93e10eb4` |



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
