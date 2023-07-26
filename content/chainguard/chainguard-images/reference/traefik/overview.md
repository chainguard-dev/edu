---
title: "Image Overview: traefik"
type: "article"
description: "Overview: traefik Chainguard Image"
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

[cgr.dev/chainguard/traefik](https://github.com/chainguard-images/images/tree/main/images/traefik)

| Tag (s)   | Last Changed | Digest                                                                    |
|-----------|--------------|---------------------------------------------------------------------------|
|  `latest` | July 25th    | `sha256:163a9b0cf78c05e7af0d155bcd89f7f2f64de39105a358216ef9c4f31a96cf6e` |



[Traefik](https://github.com/traefik/traefik) is a cloud native application proxy.

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

