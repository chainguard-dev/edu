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

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest`     | September 4th | `sha256:1a76cbf99af19b597516ff04dd213a3b602fba05a85b9bb27b9ba9f0da071820` |
|  `latest-dev` | September 4th | `sha256:920498adfc87337e0a59bb835f50cc064bf2b1b742bc932a4f8875d933142729` |



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

