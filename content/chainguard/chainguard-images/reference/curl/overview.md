---
title: "Image Overview: curl"
type: "article"
description: "Overview: curl Chainguard Image"
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

[cgr.dev/chainguard/curl](https://github.com/chainguard-images/images/tree/main/images/curl)

| Tag (s)   | Last Changed  | Digest                                                                    |
|-----------|---------------|---------------------------------------------------------------------------|
|  `latest` | September 7th | `sha256:0dbf1a0dce2306f27f6be79cef206487f2e95371841d96961a7283c0041c7127` |



This is a minimal curl image base.

It contains curl and ca-certificates.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/curl:latest
```

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

