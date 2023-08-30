---
title: "Image Overview: thanos"
type: "article"
description: "Overview: thanos Chainguard Image"
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

[cgr.dev/chainguard/thanos](https://github.com/chainguard-images/images/tree/main/images/thanos)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | August 29th  | `sha256:6cfcd7bd7a4510eca40f032e12ebc79031a2bec44e6b0590ca5a98f62c044234` |
|  `latest`     | August 29th  | `sha256:8fc2caec25bc8cf12f9a97c082aa183824a2a51da40b60051294bfcc21bc82ce` |



Minimal Thanos Image

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/thanos:latest
```

## Usage

THe default entrypoint for this image is the `thanos` binary.

To test:

```shell
$ docker run cgr.dev/chainguard/thanos:latest
usage: thanos [<flags>] <command> [<args> ...]

A block storage based long-term storage for Prometheus.

Flags:
  -h, --help               Show context-sensitive help (also try --help-long and
                           --help-man).
      --log.format=logfmt  Log format to use. Possible options: logfmt or json.
      --log.level=info     Log filtering level.
      --tracing.config=<content>
                           Alternative to 'tracing.config-file' flag
                           (mutually exclusive). Content of YAML file
                           with tracing configuration. See format details:
                           https://thanos.io/tip/thanos/tracing.md/#configuration
      --tracing.config-file=<file-path>
                           Path to YAML file with tracing
                           configuration. See format details:
                           https://thanos.io/tip/thanos/tracing.md/#configuration
      --version            Show application version.

Commands:
  help [<command>...]
    Show help.

  sidecar [<flags>]
    Sidecar for Prometheus server.

  store [<flags>]
    Store node giving access to blocks in a bucket provider. Now supported GCS,
    S3, Azure, Swift, Tencent COS and Aliyun OSS.

  query [<flags>]
    Query node exposing PromQL enabled Query API with data retrieved from
    multiple store nodes.
```

