---
title: "Image Overview: netcat"
type: "article"
description: "Overview: netcat Chainguard Image"
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

[cgr.dev/chainguard/netcat](https://github.com/chainguard-images/images/tree/main/images/netcat)

| Tag (s)   | Last Changed | Digest                                                                    |
|-----------|--------------|---------------------------------------------------------------------------|
|  `latest` | August 31st  | `sha256:d904f75a1cd323140a6955a64168d2aa94093fd4a6f2c1adbb9c76906b469467` |



Minimal image for Debian port of OpenBSD's netcat. **EXPERIMENTAL**

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/netcat:latest
```

## Usage

```
docker run --rm -ti cgr.dev/chainguard/netcat -zv google.com 443
```

See [here](https://manpages.debian.org/unstable/netcat-openbsd/nc.1.en.html) for more invocation details.

