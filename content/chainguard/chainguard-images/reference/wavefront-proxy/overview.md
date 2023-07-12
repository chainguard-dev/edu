---
title: "Image Overview: Wavefront-proxy"
type: "article"
description: "Overview: Wavefront-proxy Chainguard Image"
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

[cgr.dev/chainguard/wavefront-proxy](https://github.com/chainguard-images/images/tree/main/images/wavefront-proxy)

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest`     | 19 hours ago | `sha256:ad01fd5f1af93fec1db7aee20214170450e1d240abbed6c83d6dd694575a5978` |
| `latest-dev` | 19 hours ago | `sha256:db8a0166d1c97f17d861b426c6a444696c2456110a6e03f65a9e329438b40fe0` |



Minimal wavefront-proxy image

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/wavefront-proxy:latest
```

## Usage

This image is a drop-in replacement for the upstream image.

To test:

```shell
# Need to update WAVEFRONT_URL and WAVEFRONT_TOKEN accordingly

$ docker run -d \
 -e WAVEFRONT_URL=https://<myinstance>.wavefront.com/api \
 -e WAVEFRONT_TOKEN=<YOUR-API-TOKEN> \
 -e JAVA_HEAP_USAGE="1650m"\
 -m 2g \
 -p 2878:2878 \
  cgr.dev/chainguard/wavefront-proxy

```

Note that the `wavefront-proxy` does need the `WAVEFRONT_URL` and `WAVEFRONT_TOKEN`  to work correctly.
See the [configuration](https://docs.wavefront.com/proxies_kube_container.html) docs for more examples.
