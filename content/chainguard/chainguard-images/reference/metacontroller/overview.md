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
|  `latest-dev` | August 15th  | `sha256:106a4599de679d6dc0f5d8e17ddb861e923fb80e9b524ba76b542075a9a7df9d` |
|  `latest`     | August 15th  | `sha256:e57a2edad97b3103864aac9f0e00cc07710d68d5a0cd6721641bd2b94c40d6b8` |



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

