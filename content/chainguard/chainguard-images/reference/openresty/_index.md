---
title: "Image Overview: openresty"
linktitle: "openresty"
type: "article"
layout: "single"
description: "Overview: openresty Chainguard Image"
date: 2024-06-23 00:43:06
lastmod: 2024-06-23 00:43:06
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/openresty/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/openresty/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/openresty/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/openresty/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
OpenResty is a high Performance Web Platform Based on Nginx and LuaJIT.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/openresty:latest
```


<!--body:start-->
## Usage

To start an OpenResty container with this image, you can use the following command:

```sh
docker run --name openresty -p 80:80 cgr.dev/chainguard/openresty
```

This will start OpenResty in non-daemon mode with the openresty's default Nginx [configuration file](https://github.com/openresty/docker-openresty/blob/master/nginx.conf).

To adhere to stricter security guidelines, in Chainguard's OpenResty image, the default locations for writable files are moved as follows:
- logs: `/var/log/openresty/`
- `nginx.conf`: `/etc/nginx/nginx.conf`
- `default.conf`: `/etc/nginx/conf.d/default.conf`
- `*_temp` directories: `/var/run/openresty/`

### Configuration

You can mount your custom configuration files to the container.

```sh
docker run --name openresty -p 80:80 -v /path/to/your/nginx.conf:/etc/nginx/nginx.conf cgr.dev/chainguard/openresty
```

For more information, refer to the official [OpenResty documentation](https://openresty.org/en/docs.html) and the [OpenResty image documentation](https://github.com/openresty/docker-openresty/tree/master).
<!--body:end-->
