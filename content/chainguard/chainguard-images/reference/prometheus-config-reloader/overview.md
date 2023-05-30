---
title: "Image Overview: prometheus-config-reloader"
type: "article"
description: "Overview: prometheus-config-reloader Chainguard Images"
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

`stable` [cgr.dev/chainguard/prometheus-config-reloader](https://github.com/chainguard-images/images/tree/main/images/prometheus-config-reloader)
| Tags         | Aliases                                            |
|--------------|----------------------------------------------------|
| `latest`     | `0`, `0.65`, `0.65.1`, `0.65.1-r1`                 |
| `latest-dev` | `0-dev`, `0.65-dev`, `0.65.1-dev`, `0.65.1-r1-dev` |



## Try It Out

```sh
helm upgrade --install cg-test \
    prometheus-community/kube-prometheus-stack \
    --set prometheusOperator.prometheusConfigReloader.image.repository=chainguard/prometheus-config-reloader \
    --set prometheusOperator.prometheusConfigReloader.image.registry=cgr.dev \
    --set prometheusOperator.prometheusConfigReloader.image.tag=<set to the latest chainguard tag>
```

You'll want to make sure the `kube-prometheus-stack` chart is up-to-date and use the latest operator tag that's within the compatibility matrix.

