---
title: "Image Overview: memcached-exporter"
type: "article"
description: "Overview: memcached-exporter Chainguard Image"
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

[cgr.dev/chainguard/memcached-exporter](https://github.com/chainguard-images/images/tree/main/images/memcached-exporter)

| Tag (s)   | Last Changed | Digest                                                                    |
|-----------|--------------|---------------------------------------------------------------------------|
|  `latest` | July 26th    | `sha256:b7cb3581d78971a5fee8b9f5bf12588a1bc15b6c23dbfceeb0defd7ad32a9e2f` |



A memcached exporter for Prometheus.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/memcached-exporter
```

## Using Memcached

By default the memcached-exporter serves on port 0.0.0.0:9150 at /metrics:

```sh
docker run -p 9150:9150 cgr.dev/chainguard/memcached-exporter:latest
```

```sh
$ docker run -p 9150:9150 ghcr.io/tuananh/memcached-exporter:latest
ts=2023-04-26T17:47:53.477Z caller=main.go:58 level=info msg="Starting memcached_exporter" version="(version=0.11.2, branch=HEAD, revision=48795923bbe6c23eb044c522283e0d865bffbc77)"
ts=2023-04-26T17:47:53.478Z caller=main.go:59 level=info msg="Build context" context="(go=go1.20.3, platform=linux/amd64, user=@fv-az251-622, date=19700101-00:00:00, tags=netgo)"
ts=2023-04-26T17:47:53.478Z caller=tls_config.go:232 level=info msg="Listening on" address=[::]:9150
ts=2023-04-26T17:47:53.478Z caller=tls_config.go:235 level=info msg="TLS is disabled." http2=false address=[::]:9150
```

## Users and Directories

By default this image runs as a non-root user named `nonroot` with a uid of 65532.

