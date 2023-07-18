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
|  `latest-dev` | July 18th    | `sha256:96a1ee2eea48c7d758113b99be52c7c181df138100ef43b5a5c7698b62f33041` |
|  `latest`     | July 11th    | `sha256:2007c187eff4fa07b9114b586a5e6606d9ec919f30835dbbd5e4c4d73f79775b` |
|               | July 8th     | `sha256:0123b33523b214f44a37ed6696b6a1b1f52b76af865cd9b719cc844aca1c090f` |
|               | July 8th     | `sha256:c9075817f35f42d6b12949874bf667b0fda51a94ee619782f5e9755fd6f36707` |



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

