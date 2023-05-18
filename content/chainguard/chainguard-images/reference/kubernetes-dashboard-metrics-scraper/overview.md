---
title: "Image Overview: kubernetes-dashboard-metrics-scraper"
type: "article"
description: "Overview: kubernetes-dashboard-metrics-scraper Chainguard Images"
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

`stable` [cgr.dev/chainguard/kubernetes-dashboard-metrics-scraper](https://github.com/chainguard-images/images/tree/main/images/kubernetes-dashboard-metrics-scraper)
| Tags         | Aliases                                         |
|--------------|-------------------------------------------------|
| `latest`     | `1`, `1.0`, `1.0.9`, `1.0.9-r0`                 |
| `latest-dev` | `1-dev`, `1.0-dev`, `1.0.9-dev`, `1.0.9-r0-dev` |



Minimal image that acts as a drop-in replacement for the `kubernetesui/metrics-scraper` image.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/kubernetes-dashboard-metrics-scraper:latest
```

You can run it with the standard deployment with something like:

```
helm install my-release kubernetes-dashboard/kubernetes-dashboard  \
  --set metricsScraper.image.repository=cgr.dev/chainguard/kubernetes-dashboard-metrics-scraper \
  --set metricsScraper.image.tag=latest \
  --set metricsScraper.enabled=true
```

