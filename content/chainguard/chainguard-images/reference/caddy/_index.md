---
title: "Image Overview: caddy"
linktitle: "caddy"
type: "article"
layout: "single"
description: "Overview: caddy Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/caddy/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/caddy/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/caddy/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/caddy/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Open source web server with automatic HTTPS written in Go
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/caddy:latest
```


<!--body:start-->
## Usage

This image comes with a default configuration `Caddyfile` located in `/etc/caddy/Caddyfile`.

Please refer to [upstream's excellent (and comprehensive) documentation](https://caddyserver.com/docs/) on the subject of configuring Caddy for your needs.

The following example runs `caddy` with a custom configuration file:

```
docker run -it --rm -v "$(pwd)/Caddyfile:/etc/caddy/Caddyfile" cgr.dev/chainguard/caddy caddy run --config /etc/caddy/Caddyfile
```
<!--body:end-->

