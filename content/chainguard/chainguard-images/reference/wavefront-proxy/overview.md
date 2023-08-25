---
title: "Image Overview: wavefront-proxy"
type: "article"
description: "Overview: wavefront-proxy Chainguard Image"
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

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | August 24th  | `sha256:e27acac1d64c41e0f6a5090b76797d35b22bf39e40bd2ad27b4308f61f126015` |
|  `latest`     | August 24th  | `sha256:66cc3d4a76ad8b1194ab2a95a63bf524e36133354f12cfccc1339559ab6678fd` |



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

