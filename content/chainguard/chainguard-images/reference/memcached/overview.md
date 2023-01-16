---
title: "Image Overview: memcached"
type: "article"
description: "Overview: memcached Chainguard Images"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
images: []
menu:
  docs:
    parent: "images-reference"
weight: 600
toc: true
---

<!--monopod:start-->

| | |
| - | - |
| **Status** | experimental |
| **OCI Reference** | `cgr.dev/chainguard/memcached` |
| **Variants/Tags** | ![](https://storage.googleapis.com/chainguard-images-build-outputs/summary/memcached.svg) |
---
<!--monopod:end-->

[Memcached](https://memcached.org/) is an in-memory key-value store for small chunks of arbitrary data (strings, objects) from results of database calls, API calls, or page rendering.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/memcached
```

## Using Memcached

The default memcached port is 11211.
To run with Docker using default configuration:

```sh
docker run -p 11211:11211 --rm cgr.dev/chainguard/memcached
```

Connect to Memcached with telnet

```sh
$ telnet localhost 11211
Trying ::1...
Connected to localhost.
Escape character is '^]'.
set foo 0 100 3  
bar
STORED
get foo 
VALUE foo 0 3
bar
END
quit
Connection closed by foreign host.
```

## Users and Directories

By default this image runs as a non-root user named `memcached` with a uid of 65532.
