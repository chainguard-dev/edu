---
title: "Image Overview: metacontroller"
type: "article"
description: "Overview: metacontroller Chainguard Image"
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

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | August 28th  | `sha256:ffd4d7b360d76aa8e14ccf101e52531cb1930384affc9dd7d8d760d8c1e898c0` |
|  `latest-dev` | August 28th  | `sha256:c89b9ddd2e9faf0dd421f95c90e4db896d0f164aa53307016a66ba063994ed00` |



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

