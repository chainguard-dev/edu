---
title: "Image Overview: curl-fips"
linktitle: "curl-fips"
type: "article"
layout: "single"
description: "Overview: curl-fips Chainguard Image"
date: 2024-07-05 00:42:00
lastmod: 2024-07-05 00:42:00
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/curl-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/curl-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/curl-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/curl-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal [curl](https://curl.se/) image base containing curl and ca-certificates.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/curl-fips:latest
```


<!--body:start-->
## Usage

The curl Chainguard Image allows you to run ordinary `curl` commands in CI/CD pipelines as well as locally with Docker.

To make sure you have the latest version of the Image available, start by running a `docker pull` command:

```shell
docker pull cgr.dev/chainguard/curl
```

Then, run the image with the `--version` flag to make sure the Image is functional:

```shell
docker run -it --rm cgr.dev/chainguard/curl --version
```

This will return output similar to the following:

```shell
curl 8.5.0 (x86_64-pc-linux-gnu) libcurl/8.5.0 rustls-ffi/0.11.0/rustls/0.21.5 zlib/1.3 brotli/1.1.0 nghttp2/1.58.0
Release-Date: 2023-12-06
Protocols: dict file ftp ftps gopher gophers http https imap imaps mqtt pop3 pop3s rtsp smtp smtps telnet tftp
Features: alt-svc AsynchDNS brotli HSTS HTTP2 HTTPS-proxy IPv6 Largefile libz SSL threadsafe UnixSockets
```
<!--body:end-->

