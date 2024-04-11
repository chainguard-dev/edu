---
title: "Image Overview: traefik-fips"
linktitle: "traefik-fips"
type: "article"
layout: "single"
description: "Overview: traefik-fips Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/traefik-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/traefik-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/traefik-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/traefik-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
[Traefik](https://github.com/traefik/traefik) is a cloud native application proxy.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/traefik-fips:latest
```


<!--body:start-->
## Using Traefik

The default Traefik ports are 80 and 8080.

There is no default configuration in the image, but you can use a sample one like this:

```yaml
## traefik.yml


# API and dashboard configuration. DO NOT RUN IN PROD
api:
  insecure: true
```

Save the configuration file from above as `traefik.yml`, then run:

```sh
docker run -v $PWD:/etc  -p 80:80 -p 8080:8080 cgr.dev/chainguard/traefik  --configFile=/etc/traefik.yml
time="2023-01-29T12:37:55Z" level=info msg="Configuration loaded from file: /etc/traefik.yml"
```

## Users and Directories

By default this image runs as a non-root user named `traefik` with a uid of 65532.
<!--body:end-->

