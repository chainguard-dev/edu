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
|  `latest-dev` | July 28th    | `sha256:623cc5584cc3ddb0c84bc353e33ce3f89bb36a1583f3e5ba4a0a223d954f1079` |
|  `latest`     | July 26th    | `sha256:a10326bf8b351576c066181168b02a58590fbe7f1e3562f8ddc1d5bb4e8dd91f` |



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

