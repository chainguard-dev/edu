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
|  `latest-dev` | August 15th  | `sha256:b28526d841dab776c4f56be674d27d2c965eb3ce35762cba2e1d6025a5357847` |
|  `latest`     | August 15th  | `sha256:e53412592c39172fc3940ff7d0dfc395da901b3625cdfc7d2a746eea3add682c` |



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

