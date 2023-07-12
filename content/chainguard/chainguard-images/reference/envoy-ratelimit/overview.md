---
title: "Image Overview: Envoy-ratelimit"
type: "article"
description: "Overview: Envoy-ratelimit Chainguard Image"
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

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest`     | 20 hours ago | `sha256:2007c187eff4fa07b9114b586a5e6606d9ec919f30835dbbd5e4c4d73f79775b` |
| `latest-dev` | 20 hours ago | `sha256:3302a8c224bf5e1a89e04ca7b5e4051cced83e4018d3047c205e6312c7baadd9` |



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
