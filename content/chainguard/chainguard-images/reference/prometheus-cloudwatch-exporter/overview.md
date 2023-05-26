---
title: "Image Overview: prometheus-cloudwatch-exporter"
type: "article"
description: "Overview: prometheus-cloudwatch-exporter Chainguard Images"
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

`stable` [cgr.dev/chainguard/prometheus-cloudwatch-exporter](https://github.com/chainguard-images/images/tree/main/images/prometheus-cloudwatch-exporter)
| Tags         | Aliases                                            |
|--------------|----------------------------------------------------|
| `latest`     | `0`, `0.15`, `0.15.3`, `0.15.3-r1`                 |
| `latest-dev` | `0-dev`, `0.15-dev`, `0.15.3-dev`, `0.15.3-r1-dev` |



Minimal image with the Prometheus Cloudwatch Exporter.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/prometheus-cloudwatch-exporter
```

## Usage

The image is a drop-in replacement for the `prom/cloudwatch-exporter` image.

The image needs a configuration to run.
There is not an example included in the image, but you can find one [here](https://github.com/prometheus/cloudwatch_exporter/blob/master/example.yml).
The default location for the config is `/config/config.yml`, but this can be overridden with the image command.

