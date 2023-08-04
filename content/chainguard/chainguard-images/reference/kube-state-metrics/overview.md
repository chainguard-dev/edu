---
title: "Image Overview: kube-state-metrics"
type: "article"
description: "Overview: kube-state-metrics Chainguard Image"
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

[cgr.dev/chainguard/kube-state-metrics](https://github.com/chainguard-images/images/tree/main/images/kube-state-metrics)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | August 3rd   | `sha256:6ff1ad02d36a624df93c3520737d874a407e6f36049306378e9be45892eee8f0` |
|  `latest`     | July 26th    | `sha256:9d5aedfa84d2d62a49aa1f8b750fa6bfc81dd12bd335c6316157b4cac5a52527` |



Minimal Kube State Metrics Image

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/kube-state-metrics:latest
```

## Usage

To test:

```shell
$ docker run cgr.dev/chainguard/kube-state-metrics
```


There are several methods to deploy the kube-state-metrics, but we will use the `helm` method.

We should add the `prometheus-community` Helm repository to our repositories list:

```shell
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```

Next, we can install the kube-state-metrics with the following command:

```sh
helm upgrade --install cg-test \
    prometheus-community/kube-state-metrics \
    --set image.repository=chainguard/kube-state-metrics \
    --set image.registry=cgr.dev \
    --set image.tag=<set to the latest chainguard tag>
```

Once the kube-state-metrics has been deployed, verify the pods are running:

```shell
kubectl get pods -l app.kubernetes.io/name=kube-state-metrics
```

