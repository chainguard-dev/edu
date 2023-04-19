---
title: "Image Overview: minio"
type: "article"
description: "Overview: minio Chainguard Images"
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

`experimental` [cgr.dev/chainguard/minio](https://github.com/chainguard-images/images/tree/main/images/minio)
| Tags         | Aliases                                                                        |
|--------------|--------------------------------------------------------------------------------|
| `latest`     | `0`, `0.20230413`, `0.20230413.030807`, `0.20230413.030807-r0`                 |
| `latest-dev` | `0-dev`, `0.20230413-dev`, `0.20230413.030807-dev`, `0.20230413.030807-r0-dev` |



Minimal image with Minio. **EXPERIMENTAL**

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/minio:latest
```

## Using Minio

The Chainguard Minio image contains the `minio` server binary.
The default entrypoint just runs the `minio` binary without any flags.

```shell
$ docker run cgr.dev/chainguard/minio
NAME:
  minio - High Performance Object Storage

DESCRIPTION:
  Build high performance data infrastructure for machine learning, analytics and application data workloads with MinIO

USAGE:
  minio [FLAGS] COMMAND [ARGS...]

COMMANDS:
  server  start object storage server

FLAGS:
  --certs-dir value, -S value  path to certs directory (default: "/root/.minio/certs")
  --quiet                      disable startup and info messages
  --anonymous                  hide sensitive information from logging
  --json                       output logs in JSON format
  --help, -h                   show help
  --version, -v                print the version

VERSION:
  DEVELOPMENT.2023-03-24T21-41-23Z
```

To start minio in a server configuration, make sure to override the `MINIO_ROOT_USER` and `MINIO_ROOT_PASSWORD` environment variables,
and pass a data volume to the `server` command.

```shell
$ docker run -v $(pwd):/data -e MINIO_ROOT_USER=MYNAME -e MINIO_ROOT_PASSWORD=nothunter2 cgr.dev/chainguard/minio serve /data
MinIO Object Storage Server
Copyright: 2015-2023 MinIO, Inc.
License: GNU AGPLv3 <https://www.gnu.org/licenses/agpl-3.0.html>
Version: DEVELOPMENT.2023-03-24T21-41-23Z (go1.20.2 linux/arm64)

Status:         1 Online, 0 Offline.
API: http://172.17.0.5:9000  http://127.0.0.1:9000
Console: http://172.17.0.5:46387 http://127.0.0.1:46387

Documentation: https://min.io/docs/minio/linux/index.html
Warning: The standard parity is set to 0. This can lead to data loss.
```

