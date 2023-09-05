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

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest`     | September 4th | `sha256:269e5497703158539b14d0a21cc314ade1190445f5640b23ecb06680494cfbd5` |
|  `latest-dev` | September 4th | `sha256:500d780192718049f2c5de7b19ff80f3dd0fc41549605def4e2503e0700c0b6f` |



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

