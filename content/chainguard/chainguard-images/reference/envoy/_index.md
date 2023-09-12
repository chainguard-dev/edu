---
title: "Image Overview: envoy"
linktitle: "envoy"
type: "article"
layout: "single"
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

{{< tabs >}}
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/envoy/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/envoy/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/envoy/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/envoy/provenance_info/" >}}
{{</ tabs >}}



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

