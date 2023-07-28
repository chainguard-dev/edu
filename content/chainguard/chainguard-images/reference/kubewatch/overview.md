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

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 27th    | `sha256:46048493a17a422dff0e85bfdc64768ed709d976994b8287bee6d5a5b13c99f1` |
|  `latest`     | July 26th    | `sha256:bcd9b56b6a99c7ee54c81996a6710dfa0bd1bd7aa6c9be5e3abcb08e83d64ee2` |



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

