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

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest`     | September 2nd | `sha256:0133e87a7249260911137da51a5692511a90576eb94ce0e87dd51011979099c1` |
|  `latest-dev` | September 2nd | `sha256:51aabe175c62a74f5ba6ed2305996b03a98b6f4d26dbaa609e5821594288be58` |



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

