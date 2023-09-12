---
title: "Image Overview: pgbouncer"
type: "article"
description: "Overview: pgbouncer Chainguard Image"
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

[cgr.dev/chainguard/pgbouncer](https://github.com/chainguard-images/images/tree/main/images/pgbouncer)

| Tag (s)       | Last Changed   | Digest                                                                    |
|---------------|----------------|---------------------------------------------------------------------------|
|  `latest`     | September 11th | `sha256:104b5b1f05bfba45897eb5c06f96df6ed616c5c0d48115bacb4a9f819a91fc7d` |
|  `latest-dev` | September 11th | `sha256:d7cb3c9fd93fc30371c5be0ff0b38b8f8d4714c4786584f32fe4ecd02dc095ed` |



This image contains the CLI for the [pgbouncer](https://www.pgbouncer.org/) connection pooler for PostgreSQL.
This image contains the `pgbouncer` binary and can be used directly.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/pgbouncer:latest
```

## Use It!

The image can be run directly and sets the `pgbouncer` tool as the entrypoint:

```
docker run cgr.dev/chainguard/pgbouncer:latest
/usr/bin/pgbouncer is a connection pooler for PostgreSQL.

Usage:
  /usr/bin/pgbouncer [OPTION]... CONFIG_FILE

Options:
  -d, --daemon         run in background (as a daemon)
  -q, --quiet          run quietly
  -R, --reboot         do an online reboot
  -u, --user=USERNAME  assume identity of USERNAME
  -v, --verbose        increase verbosity
  -V, --version        show version, then exit
  -h, --help           show this help, then exit

Report bugs to <https://github.com/pgbouncer/pgbouncer/issues>.
PgBouncer home page: <https://www.pgbouncer.org/>
```

Note that `pgbouncer` typically needs a configuration file to run.
One is not provided here in the image by default.
You can find documentation on how to configure one in the [upstream documentation](https://www.pgbouncer.org/config.html#authentication-settings)..

