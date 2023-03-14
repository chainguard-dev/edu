---
title: "Image Overview: netcat"
type: "article"
description: "Overview: netcat Chainguard Images"
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

`experimental` [cgr.dev/chainguard/netcat](https://github.com/chainguard-images/images/tree/main/images/netcat)
| Tags     | Aliases                  |
|----------|--------------------------|
| `latest` | `1`, `1.219`, `1.219-r0` |



Minimal image for Debian port of OpenBSD's netcat. **EXPERIMENTAL**

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/netcat:latest
```

## Usage

```
docker run --rm -ti ghcr.io/chainguard/netcat -zv google.com 443
```

See [here](https://manpages.debian.org/unstable/netcat-openbsd/nc.1.en.html) for more invocation details.
