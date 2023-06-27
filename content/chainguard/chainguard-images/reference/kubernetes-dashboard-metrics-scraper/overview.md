---
title: "Image Overview: Kubernetes-dashboard-metrics-scraper"
type: "article"
description: "Overview: Kubernetes-dashboard-metrics-scraper Chainguard Image"
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

[cgr.dev/chainguard/kubernetes-dashboard-metrics-scraper](https://github.com/chainguard-images/images/tree/main/images/kubernetes-dashboard-metrics-scraper)


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
