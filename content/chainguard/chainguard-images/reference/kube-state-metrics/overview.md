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
|  `latest-dev` | August 15th  | `sha256:86a1c4bc1c375c83cb22d725e9e8ad75903c866aa236565987d20f06091129fe` |
|  `latest`     | August 15th  | `sha256:900ee6a853a0a8f6964fa540bc9030203bc3856c18abdd67018bfb2f47d78b00` |



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

