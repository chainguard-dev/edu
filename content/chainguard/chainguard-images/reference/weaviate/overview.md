---
title: "Image Overview: weaviate"
type: "article"
description: "Overview: weaviate Chainguard Image"
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

[cgr.dev/chainguard/weaviate](https://github.com/chainguard-images/images/tree/main/images/weaviate)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | July 18th    | `sha256:9cc38c31beaad722b2fccf7f7c337ffab0dab609ec34d15dae4b84cf8d2ab2af` |
|  `latest-dev` | July 18th    | `sha256:e7072a4f9677772ef067bca78b5f2903f796923b83556ab26d081dec8afece8a` |
|               | July 14th    | `sha256:082ae80875583f45323462aca5244912d648270f93093d86233e632d899b9556` |
|               | July 14th    | `sha256:700a61284d7d19dd6afe43455cfdca50bc50f08a292c87c373e755a11584c3d0` |
|               | July 12th    | `sha256:f57c3fec99e8aa62f0afca4874b6f308084d28a410f5e865e8c185814a1b5f4a` |
|               | July 4th     | `sha256:0f5260ac26e9f6c5c8bcf764045519a3e6a1a3a0e225356f3c6dd5aadf82f102` |
|               | July 1st     | `sha256:13e15a871173be0e3f9c3399668e4f76fb08512c72f716fa69806f7d49e5e46e` |
|               | June 29th    | `sha256:5d6d7350ac9d3afb4a4d0f4804607739e7521204cb2ad72ed0ca36b07c1d6e14` |
|               | June 29th    | `sha256:cffa0dbde3257307aaec65bb6fed13b8bf33ee91a4f72ac8dfc27ee30b03623d` |
|               | June 23rd    | `sha256:bc822c01cc6f23e912490bac3571491ff2779ffbdfc159ddfd1917cbbdc9d4cf` |
|               | June 23rd    | `sha256:a21a9dd827da25a3739e0a4c121c343631eed0f3a82997e1c3c6b3a392843d9b` |



Minimal container image for running the weaviate database.

The image specifies a default non-root `weaviate` user (UID 65532).

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/weaviate:latest
```

## Usage

This image should be a drop-in replacement for the upstream `weaviate` image.

Note that this image does not include a config file by default, and one is required to start the server.
This can be specified using the `--config-file` paramter.

```
% docker run cgr.dev/chainguard/weaviate --help
Usage:
  weaviate [OPTIONS]

Cloud-native, modular vector search engine

Application Options:
      --scheme=            the listeners to enable, this can be repeated and
                           defaults to the schemes in the swagger spec
      --cleanup-timeout=   grace period for which to wait before killing idle
                           connections (default: 10s)
      --graceful-timeout=  grace period for which to wait before shutting down
                           the server (default: 15s)
      --max-header-size=   controls the maximum number of bytes the server will
                           read parsing the request header's keys and values,
                           including the request line. It does not limit the
                           size of the request body. (default: 1MiB)
      --socket-path=       the unix socket to listen on (default:
                           /var/run/weaviate.sock)
      --host=              the IP to listen on (default: localhost) [$HOST]
      --port=              the port to listen on for insecure connections,
                           defaults to a random value [$PORT]
      --listen-limit=      limit the number of outstanding requests
      --keep-alive=        sets the TCP keep-alive timeouts on accepted
                           connections. It prunes dead TCP connections ( e.g.
                           closing laptop mid-download) (default: 3m)
      --read-timeout=      maximum duration before timing out read of the
                           request (default: 30s)
      --write-timeout=     maximum duration before timing out write of the
                           response (default: 60s)
      --tls-host=          the IP to listen on for tls, when not specified it's
                           the same as --host [$TLS_HOST]
      --tls-port=          the port to listen on for secure connections,
                           defaults to a random value [$TLS_PORT]
      --tls-certificate=   the certificate to use for secure connections
                           [$TLS_CERTIFICATE]
      --tls-key=           the private key to use for secure connections
                           [$TLS_PRIVATE_KEY]
      --tls-ca=            the certificate authority file to be used with
                           mutual tls auth [$TLS_CA_CERTIFICATE]
      --tls-listen-limit=  limit the number of outstanding requests
      --tls-keep-alive=    sets the TCP keep-alive timeouts on accepted
                           connections. It prunes dead TCP connections ( e.g.
                           closing laptop mid-download)
      --tls-read-timeout=  maximum duration before timing out read of the
                           request
      --tls-write-timeout= maximum duration before timing out write of the
                           response

Connector config & MQTT config:
      --config-file=       path to config file (default: ./weaviate.conf.json)

Help Options:
  -h, --help               Show this help message
```

