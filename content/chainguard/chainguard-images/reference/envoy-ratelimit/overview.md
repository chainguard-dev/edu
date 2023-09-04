---
title: "Image Overview: envoy-ratelimit"
type: "article"
description: "Overview: envoy-ratelimit Chainguard Image"
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

[cgr.dev/chainguard/envoy-ratelimit](https://github.com/chainguard-images/images/tree/main/images/envoy-ratelimit)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | August 31st  | `sha256:8b4b823ae6c31fba906933e1f6ba1eab4e0e011e12989ff77fd9de89f0c3838c` |
|  `latest-dev` | August 31st  | `sha256:5e6bb0e10a0c6b5a42df4ce013a87d7bde790cba341f6818b7d21ca4749985b0` |



[etcd](https://github.com/etcd-io/etcd) Distributed reliable key-value store for the most critical data of a distributed system

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/envoy-ratelimit:latest
```

This image includes `ratelimit`.

## Usage

This image should be a drop-in replacement for the upstream `envoyproxy/ratelimit` image.
See the [full documentation](https://gateway.envoyproxy.io/latest/user/rate-limit.html) for installation and usage.

See for the [examples](https://github.com/envoyproxy/ratelimit#examples).

