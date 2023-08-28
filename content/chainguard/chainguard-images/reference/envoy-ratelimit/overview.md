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
|  `latest-dev` | August 26th  | `sha256:4cdee82b812ee39d7c09870e359621b9e062ea4a8a391fdd1c6c1bf538a1ccda` |
|  `latest`     | August 15th  | `sha256:b58994047aee25e8369e5e20026c50ebee06945f1debaaef539aaebec2406ff6` |



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

