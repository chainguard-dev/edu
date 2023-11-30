---
title: "Image Overview: memcached-exporter-bitnami"
linktitle: "memcached-exporter-bitnami"
type: "article"
layout: "single"
description: "Overview: memcached-exporter-bitnami Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/memcached-exporter-bitnami/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/memcached-exporter-bitnami/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/memcached-exporter-bitnami/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/memcached-exporter-bitnami/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
A memcached exporter for Prometheus that is compatible with Bitnami Helm charts.
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/memcached-exporter-bitnami:latest
```
<!--getting:end-->

<!--body:start-->
## Using Memcached

By default the memcached-exporter serves on port 0.0.0.0:9150 at /metrics:

```sh
docker run -p 9150:9150 cgr.dev/chainguard/memcached-exporter-bitnami:latest
```

```sh
$ docker run -p 9150:9150 cgr.dev/chainguard/memcached-exporter-bitnami:latest
ts=2023-04-26T17:47:53.477Z caller=main.go:58 level=info msg="Starting memcached_exporter" version="(version=0.11.2, branch=HEAD, revision=48795923bbe6c23eb044c522283e0d865bffbc77)"
ts=2023-04-26T17:47:53.478Z caller=main.go:59 level=info msg="Build context" context="(go=go1.20.3, platform=linux/amd64, user=@fv-az251-622, date=19700101-00:00:00, tags=netgo)"
ts=2023-04-26T17:47:53.478Z caller=tls_config.go:232 level=info msg="Listening on" address=[::]:9150
ts=2023-04-26T17:47:53.478Z caller=tls_config.go:235 level=info msg="TLS is disabled." http2=false address=[::]:9150
```

## Users and Directories

By default this image runs as a non-root user named `nonroot` with a uid of 65532.
<!--body:end-->

