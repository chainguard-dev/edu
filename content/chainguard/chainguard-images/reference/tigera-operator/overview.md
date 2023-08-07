---
title: "Image Overview: tigera-operator"
type: "article"
description: "Overview: tigera-operator Chainguard Image"
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

[cgr.dev/chainguard/tigera-operator](https://github.com/chainguard-images/images/tree/main/images/tigera-operator)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | August 5th   | `sha256:96ea403f5fbb315920cc80ecf8484169e0e5da96a4da8d4962b8237cc4d51a40` |
|  `latest`     | August 5th   | `sha256:964c76a487f6aab70d31ed0195aaf7b2a082f24326f5a81a6d3a77c4ccf14c7d` |



Minimal Project Calico Tigera Operator Image

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/tigera-operator:latest
```

## Usage

This image is a drop-in replacement for the upstream image.
You can run it using the helm chart with:

```shell
helm repo add projectcalico https://projectcalico.docs.tigera.io/charts
helm repo update

helm install calico projectcalico/tigera-operator \
    --namespace tigera-operator \
    --create-namespace \
    --set autoDiscovery.clusterName=foo \
    --set tigeraOperator.registry=cgr.dev \
    --set tigeraOperator.image=chainguard/tigera-operator \
    --set tigeraOperator.version=latest

kubectl wait --namespace tigera-operator --for=condition=ready pod --selector name=tigera-operator --timeout=120s
```

