---
title: "Image Overview: pgbouncer-fips"
linktitle: "pgbouncer-fips"
type: "article"
layout: "single"
description: "Overview: pgbouncer-fips Chainguard Image"
date: 2024-03-08 00:56:03
lastmod: 2024-03-08 00:56:03
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/pgbouncer-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/pgbouncer-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/pgbouncer-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/pgbouncer-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
This image contains the CLI for the [pgbouncer](https://www.pgbouncer.org/) connection pooler for PostgreSQL. This image contains the `pgbouncer` binary and can be used directly.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/pgbouncer:latest
```
<!--getting:end-->

<!--body:start-->
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
<!--body:end-->

