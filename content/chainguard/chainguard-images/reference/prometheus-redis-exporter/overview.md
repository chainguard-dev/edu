---
title: "Image Overview: prometheus-redis-exporter"
type: "article"
description: "Overview: prometheus-redis-exporter Chainguard Images"
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

`experimental` [cgr.dev/chainguard/prometheus-redis-exporter](https://github.com/chainguard-images/images/tree/main/images/prometheus-redis-exporter)
| Tags     | Aliases                            |
|----------|------------------------------------|
| `latest` | `1`, `1.51`, `1.51.0`, `1.51.0-r0` |



A redis exporter for Prometheus.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/prometheus-redis-exporter
```

## Using Redis Exporter

By default the prometheus-redis-exporter serves on port 0.0.0.0:9121 at /metrics:

```sh
docker run -p 9121:9121 cgr.dev/chainguard/prometheus-redis-exporter:latest
```

```sh
$ docker run -p 9121:9121 cgr.dev/chainguard/prometheus-redis-exporter:latest
INFO[0000] Redis Metrics Exporter v1.50.0    build date: 2023-05-24-03:16:53    sha1: b5e02003cea4b73054abe29433c264dec16cc1f0    Go: go1.20.4    GOOS: linux    GOARCH: amd64 
INFO[0000] Providing metrics at :9121/metrics   
```

## Users and Directories

By default this image runs as a non-root user named `nonroot` with a uid of 65532.

