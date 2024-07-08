---
title: "Image Overview: gitness"
linktitle: "gitness"
type: "article"
layout: "single"
description: "Overview: gitness Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-07-08 00:34:55
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/gitness/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/gitness/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/gitness/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/gitness/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image with the `gitness` [server application](https://github.com/harness/gitness).
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/gitness:latest
```


<!--body:start-->
## Usage

To run `gitness`:

```
$ docker run -d \
  -p 3000:3000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /tmp/gitness:/data \
  --name gitness \
  --restart always \
  cgr.dev/chainguard/gitness

$ docker logs gitness
{"level":"info","time":"2023-09-30T16:31:40.085883346Z","message":"No valid profiler so skipping profiling ['']"}
{"level":"info","time":"2023-09-30T16:31:40.099510346Z","message":"Completed setup of system service 'gitness' (id: 1)."}
{"level":"info","time":"2023-09-30T16:31:40.100499137Z","message":"Completed setup of pipeline service 'pipeline' (id: 2)."}
{"level":"info","port":3000,"revision":"","repository":"","version":"0.0.0","time":"2023-09-30T16:31:40.100514721Z","message":"server started"}
{"level":"info","time":"2023-09-30T16:31:40.100516221Z","message":"gitrpc server started"}
{"level":"info","time":"2023-09-30T16:31:40.100517471Z","message":"gitrpc cron manager subroutine started"}
time="2023-09-30T16:31:40Z" level=debug msg="poller: request stage from remote server" thread=2
time="2023-09-30T16:31:40Z" level=debug msg="poller: request stage from remote server" thread=1
{"level":"info","time":"2023-09-30T16:31:41.560373846Z","message":"added 0 new entries to plugins"}
```

The server should then be available at `localhost:3000`.
<!--body:end-->

