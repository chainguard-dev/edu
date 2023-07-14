---
title: "Image Overview: k8s-sidecar"
type: "article"
description: "Overview: k8s-sidecar Chainguard Image"
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

[cgr.dev/chainguard/k8s-sidecar](https://github.com/chainguard-images/images/tree/main/images/k8s-sidecar)

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest-dev` | July 12th    | `sha256:6c0fa5716f05a6ae8b31b5f1dea9606a6bed1f1ebb6dff35f9bf0e4498d487c0` |
| `latest`     | July 11th    | `sha256:966b5a91cec1b474e8eeae424f59d3c238ad6c8a94e11ca11ebf404bbc0b5ddf` |



Minimal image with the k8s-sidecar app. **EXPERIMENTAL**

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/k8s-sidecar:latest
```

## Using k8s-sidecar

The Chainguard k8s-sidecar image contains the k8s-sidecar python app.
The default entrypoint just runs the `k8s-sidecar` app without any flags.

This image is a drop-in replacement for the upstream image.
For full documentation on how to configure the app, check the [upstream documentation](https://github.com/kiwigrid/k8s-sidecar).

```shell
$ docker run cgr.dev/chainguard/k8s-sidecar
{"time": "2023-03-31T11:50:30.950603+00:00", "msg": "Starting collector", "level": "INFO"}
{"time": "2023-03-31T11:50:30.950708+00:00", "msg": "No folder annotation was provided, defaulting to k8s-sidecar-target-directory", "level": "WARNING"}
{"time": "2023-03-31T11:50:30.950751+00:00", "msg": "Should have added {LABEL} as environment variable! Exit", "level": "CRITICAL"}
```
