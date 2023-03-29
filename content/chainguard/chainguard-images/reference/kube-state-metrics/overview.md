---
title: "Image Overview: kube-state-metrics"
type: "article"
description: "Overview: kube-state-metrics Chainguard Images"
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

`stable` [cgr.dev/chainguard/kube-state-metrics](https://github.com/chainguard-images/images/tree/main/images/kube-state-metrics)
| Tags         | Aliases                                         |
|--------------|-------------------------------------------------|
| `latest`     | `2`, `2.8`, `2.8.2`, `2.8.2-r0`                 |
| `latest-dev` | `2-dev`, `2.8-dev`, `2.8.2-dev`, `2.8.2-r0-dev` |



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

## Configuration

The image can be configured through flags.
Run it with the `--help` flag to see the full list:

```shell
$ docker run cgr.dev/chainguard/kube-state-metrics --help
kube-state-metrics is a simple service that listens to the Kubernetes API server and generates metrics about the state of the objects.

Usage:
  kube-state-metrics [flags]
  kube-state-metrics [command]

Available Commands:
  completion  Generate completion script for kube-state-metrics.
  help        Help about any command
  version     Print version information.

Flags:
```
