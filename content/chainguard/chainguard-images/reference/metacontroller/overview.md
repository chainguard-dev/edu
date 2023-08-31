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
|  `latest-dev` | August 30th  | `sha256:3d19b885bfb1025737037a7598f05099e008fbbc22dd23caddd1eca8b8ed37c4` |
|  `latest`     | August 30th  | `sha256:2523eddf34b8a22400a37c83e6d4fa74896c834cf251718999bdd6f58e5db6aa` |



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

