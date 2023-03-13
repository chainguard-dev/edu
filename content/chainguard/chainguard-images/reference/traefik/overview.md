---
title: "Image Overview: traefik"
type: "article"
description: "Overview: traefik Chainguard Images"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "images-reference"
weight: 600
toc: true
---

`experimental` [cgr.dev/chainguard/traefik](https://github.com/chainguard-images/images/tree/main/images/traefik)
| Tags     | Aliases                         |
|----------|---------------------------------|
| `latest` | `2`, `2.9`, `2.9.8`, `2.9.8-r2` |



[RabbitMQ](https://github.com/traefik/traefik) Traefik is a cloud native application proxy.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/traefik
```

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
