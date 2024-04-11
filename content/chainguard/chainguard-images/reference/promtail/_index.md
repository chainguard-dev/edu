---
title: "Image Overview: promtail"
linktitle: "promtail"
type: "article"
layout: "single"
description: "Overview: promtail Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-04-11 12:38:02
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/promtail/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/promtail/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/promtail/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/promtail/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
This image contains the `promtail` application for log aggregation. `promtail` is the log aggregator that ships logs to Loki and/or Prometheus. It runs as an agent and scrapes logs from files, containers, and hosts and ships them to a logging backend.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/promtail:latest
```


<!--body:start-->
## Use It!

The image can be run directly and sets the promtail binary as the entrypoint with a default configuration:

```
docker run cgr.dev/chainguard/promtail:latest
level=info ts=2023-09-02T14:01:20.497084554Z caller=promtail.go:133 msg="Reloading configuration file" md5sum=64f8f10a58e874375abaf4e9f7632b07
level=info ts=2023-09-02T14:01:20.497604554Z caller=server.go:323 http=[::]:9080 grpc=[::]:41909 msg="server listening on addresses"
level=info ts=2023-09-02T14:01:20.497705346Z caller=main.go:174 msg="Starting Promtail" version="(version=2.8.4, branch=HEAD, revision=89d282c)"
level=warn ts=2023-09-02T14:01:20.497754387Z caller=promtail.go:265 msg="enable watchConfig"
```

This image is a drop-in replacement for official image at grafana/promtail.
See documentation [there](https://github.com/grafana/loki/blob/main/cmd/promtail/Dockerfile#L9) for how to configure it.
<!--body:end-->

