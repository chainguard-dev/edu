---
title: "Image Overview: curl"
linktitle: "curl"
type: "article"
layout: "single"
description: "Overview: curl Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2023-11-28 00:31:13
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/curl/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/curl/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/curl/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/curl/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal [curl](https://curl.se/) image base containing curl and ca-certificates.
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/curl:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

The curl image allows you to run ordinary curl commands in CI/CD pipelines and also locally via Docker.

### Docker Setup

To make sure you have the latest image version available, start by running a `docker pull` command:

```shell
docker pull cgr.dev/chainguard/curl
```

Then, run the image with the `--version` flag to make sure it is functional:

```shell
docker run -it --rm cgr.dev/chainguard/curl --version
```
You should get output similar to this:

```shell
$ docker run curl --version
curl 7.87.0 (aarch64-unknown-linux-gnu) libcurl/7.87.0 OpenSSL/3.0.7 zlib/1.2.13 brotli/1.0.9 nghttp2/1.49.0
Release-Date: 2022-12-21
Protocols: dict file ftp ftps gopher gophers http https imap imaps mqtt pop3 pop3s rtsp smb smbs smtp smtps telnet tftp
Features: alt-svc AsynchDNS brotli HSTS HTTP2 HTTPS-proxy IPv6 Largefile libz NTLM NTLM_WB SSL threadsafe TLS-SRP UnixSockets
```
<!--body:end-->

