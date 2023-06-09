---
title: "Image Overview: prometheus-operator"
type: "article"
description: "Overview: prometheus-operator Chainguard Images"
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

`stable` [cgr.dev/chainguard/prometheus-operator](https://github.com/chainguard-images/images/tree/main/images/prometheus-operator)
| Tags         | Aliases                                            |
|--------------|----------------------------------------------------|
| `latest`     | `0`, `0.65`, `0.65.2`, `0.65.2-r2`                 |
| `latest-dev` | `0-dev`, `0.65-dev`, `0.65.2-dev`, `0.65.2-r2-dev` |



## Try It Out

```sh
helm upgrade --install cg-test \
    prometheus-community/kube-prometheus-stack \
    --set prometheusOperator.image.repository=chainguard/prometheus-operator \
    --set prometheusOperator.image.registry=cgr.dev \
    --set prometheusOperator.image.tag=<set to the latest chainguard tag>
```

You'll want to make sure the `kube-prometheus-stack` chart is up-to-date and use the latest operator tag that's within the compatibility matrix.

## Known Deviations

The location of the operator binary changes in this image. This image uses

```sh
/usr/bin/operator
```

Upstream image uses

```sh
/bin/operator
```

