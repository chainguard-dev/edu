---
title: "Image Overview: tigera-operator"
type: "article"
description: "Overview: tigera-operator Chainguard Images"
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

`stable` [cgr.dev/chainguard/tigera-operator](https://github.com/chainguard-images/images/tree/main/images/tigera-operator)
| Tags         | Aliases                                            |
|--------------|----------------------------------------------------|
| `latest`     | `1`, `1.30`, `1.30.2`, `1.30.2-r0`                 |
| `latest-dev` | `1-dev`, `1.30-dev`, `1.30.2-dev`, `1.30.2-r0-dev` |



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
    --set tigeraOperator.registry="${IMAGE_REGISTRY}" \
    --set tigeraOperator.image="${IMAGE_REPOSITORY}" \
    --set tigeraOperator.version="${IMAGE_TAG}" \
    --set image.pullPolicy=IfNotPresent

kubectl wait --namespace tigera-operator --for=condition=ready pod --selector name=tigera-operator --timeout=120s
```

