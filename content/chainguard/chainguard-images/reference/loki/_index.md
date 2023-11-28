---
title: "Image Overview: loki"
linktitle: "loki"
type: "article"
layout: "single"
description: "Overview: loki Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2023-11-28 00:31:13
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu: 
  docs: 
    parent: "images-reference"
weight: 500
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/loki/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/loki/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/loki/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/loki/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
This image contains the `loki` application for log aggregation. `loki` can be used to stream, aggregate, and query logs from apps and infrastructure.
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/loki:latest
```
<!--getting:end-->

<!--body:start-->
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
<!--body:end-->

