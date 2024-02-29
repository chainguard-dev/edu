---
title: "Image Overview: configurable-http-proxy-fips"
linktitle: "configurable-http-proxy-fips"
type: "article"
layout: "single"
description: "Overview: configurable-http-proxy-fips Chainguard Image"
date: 2024-02-29 16:25:55
lastmod: 2024-02-29 16:25:55
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/configurable-http-proxy-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/configurable-http-proxy-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/configurable-http-proxy-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/configurable-http-proxy-fips/provenance_info/" >}}
{{</ tabs >}}

#  configurable-http-proxy-fips

[configurable-http-proxy](https://github.com/jupyterhub/configurable-http-proxy) provides you with a way to update and manage a proxy table using a command line interface or REST API. It is a simple wrapper around node-http-proxy. node-http-proxy is an HTTP programmable proxying library that supports websockets and is suitable for implementing components such as reverse proxies and load balancers. By wrapping node-http-proxy, configurable-http-proxy extends this functionality to JupyterHub deployments.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/configurable-http-proxy-fips:latest
```

## Usage

See the [official usage documentation](https://github.com/jupyterhub/configurable-http-proxy?tab=readme-ov-file#usage) on GitHub.

Run:

```sh
docker run --rm cgr.dev/chainguard-private/configurable-http-proxy-fips:latest
```

