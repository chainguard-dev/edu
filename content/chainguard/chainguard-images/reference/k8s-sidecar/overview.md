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

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | July 18th    | `sha256:d7b3965a43e6bb993c59fb8d0a1c0ce100f674f84bb790503e15248a8e7ec0fe` |
|  `latest-dev` | July 18th    | `sha256:e14a2616d1d53c89c38145e762526ec2a1850736c9d2fe29235864d4c1807032` |
|               | July 12th    | `sha256:6c0fa5716f05a6ae8b31b5f1dea9606a6bed1f1ebb6dff35f9bf0e4498d487c0` |
|               | July 11th    | `sha256:966b5a91cec1b474e8eeae424f59d3c238ad6c8a94e11ca11ebf404bbc0b5ddf` |
|               | July 7th     | `sha256:5156479e706dc16f34244017f10011309a03abfbf63defdf2cd56c31910fdd9a` |
|               | July 5th     | `sha256:949694d2eaf88e8a965f8400f4501a87df5dd19fdfde03f0e47fbc010c9f20df` |
|               | July 5th     | `sha256:bb6ed06ed4dfb33c16b2f706432b4cb3cbdde9483a98b6afba8e6574c0ce4470` |
|               | July 4th     | `sha256:cf393f9f35cea42e5c4435ac26435dea17fbbb3634b63b009079f91b8de77f96` |
|               | July 4th     | `sha256:4d289a1ce2a5ff293dd7b12efb05fe655cbae1618a436b964ca7914141e747ac` |



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

