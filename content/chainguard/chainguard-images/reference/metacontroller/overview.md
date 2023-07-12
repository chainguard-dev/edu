---
title: "Image Overview: Metacontroller"
type: "article"
description: "Overview: Metacontroller Chainguard Image"
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

[cgr.dev/chainguard/metacontroller](https://github.com/chainguard-images/images/tree/main/images/metacontroller)

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest-dev` | 19 hours ago | `sha256:1268faacdf6d35939c309d526aed97d015dc7e07473cd76bfc835d957dcdc07a` |
| `latest`     | 19 hours ago | `sha256:6c31166d0efe91874fb04ab7b3dbaeea484a86c5c85ac01de1ded8f0d8cecfb6` |



Minimal Metacontroller Container

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/:latest
```

## Usage

This image is a drop-in replacement for the upstream image.
You can run it using the helm chart with:

```shell
$ export HELM_EXPERIMENTAL_OCI=1
$ helm install my-metacontroller-helm oci://ghcr.io/metacontroller/metacontroller-helm --version v4.10.3  \
    --set image.repository=cgr.dev/chainguard/metacontroller \
    --set image.tag=latest \
    <other configuration parameters here>
```

See the [configuration](https://metacontroller.github.io/metacontroller/guide/helm-install.html#configuration) docs for more examples.
