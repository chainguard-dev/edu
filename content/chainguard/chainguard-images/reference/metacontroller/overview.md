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
|  `latest-dev` | August 23rd  | `sha256:905c9109efb69cef59b8812e4344048e4b33d621cbc50a946882fc93ffe08424` |
|  `latest`     | August 23rd  | `sha256:e58b42948d571cc9fafa4926320b5e1a20f8dccd405b9e027384ab7f5d758433` |



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

