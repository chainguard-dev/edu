---
title: "Image Overview: loki"
type: "article"
description: "Overview: loki Chainguard Image"
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

[cgr.dev/chainguard/loki](https://github.com/chainguard-images/images/tree/main/images/loki)

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest-dev` | September 3rd | `sha256:9f22d79fbb1a84216f99f94d6f2fe9e00b4a63d8cdb6b3c4d87d8c7286547fa8` |
|  `latest`     | September 3rd | `sha256:20bce8d2b9a8f1bac063bd955d93ee668aa54a74b72cd352d95d7fff46a362ce` |



This image contains the `loki` application for log aggregation.
`loki` can be used to stream, aggregate, and query logs from apps and infrastructure.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/loki:latest
```

## Use It!

The image can be run directly and sets the loki binary as the entrypoint with a default configuration:

```
docker run cgr.dev/chainguard/loki:latest
level=warn ts=2023-09-02T00:50:53.025935792Z caller=loki.go:286 msg="per-tenant timeout not configured, using default engine timeout (\"5m0s\"). This behavior will change in the next major to always use the default per-tenant timeout (\"5m\")."
level=info ts=2023-09-02T00:50:53.026961126Z caller=main.go:108 msg="Starting Loki" version="(version=2.8.4, branch=HEAD, revision=89d282c)"
level=info ts=2023-09-02T00:50:53.027809417Z caller=server.go:323 http=[::]:3100 grpc=[::]:9095 msg="server listening on addresses"
level=warn ts=2023-09-02T00:50:53.029690834Z caller=cache.go:114 msg="fifocache config is deprecated. use embedded-cache instead"
level=warn ts=2023-09-02T00:50:53.029774501Z caller=experimental.go:20 msg="experimental feature in use" feature="In-memory (FIFO) cache - chunksembedded-cache"
level=info ts=2023-09-02T00:50:53.030041376Z caller=table_manager.go:134 msg="uploading tables"
level=info ts=2023-09-02T00:50:53.030075792Z caller=table_manager.go:262 msg="query readiness setup completed" duration=750ns distinct_users_len=0
```

This image is a drop-in replacement for official image at grafana/loki.
See documentation [there](https://github.com/grafana/loki/blob/main/cmd/loki/Dockerfile#L9) for how to configure it.

