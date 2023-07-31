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
|  `latest-dev` | July 28th    | `sha256:0008cce99a026ebe55f2bb23bec15b79c85d36a8bf1933a840aa51ed1da844bd` |
|  `latest`     | July 26th    | `sha256:0c0f3f7f1b61d751b100f56a5612ebea73afd9797e2e11c0e5041e8bc0d20166` |



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

