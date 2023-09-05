---
title: "Image Overview: envoy"
type: "article"
description: "Overview: envoy Chainguard Image"
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

[cgr.dev/chainguard/envoy](https://github.com/chainguard-images/images/tree/main/images/envoy)

| Tag (s)   | Last Changed  | Digest                                                                    |
|-----------|---------------|---------------------------------------------------------------------------|
|  `latest` | September 4th | `sha256:14cf17f4716593022c395c68ca824267ad143a20a34e2fee36ca93ce49a74faa` |



[Envoy](https://github.com/envoyproxy/envoy) Cloud-native high-performance edge/middle/service proxy

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/envoy
```

## Using Envoy

To run with Docker using default configuration

```sh
docker run --platform=linux/amd64 -p10000:10000 -p 9901:9901 --rm cgr.dev/chainguard/envoy envoy --config-path /etc/envoy/envoy.yaml
```

Or to use a customised envoy configuratiom see https://www.envoyproxy.io/docs/envoy/latest/configuration/overview/overview and mount your file into the envoy container, e.g. `-v $PWD/config:/etc/envoy`

```sh
docker run --platform=linux/amd64 -p10000:10000 -p 9901:9901 --rm -v $PWD/config:/etc/envoy cgr.dev/chainguard/envoy envoy --config-path /etc/envoy/envoy.yaml
```

