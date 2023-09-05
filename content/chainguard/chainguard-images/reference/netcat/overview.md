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

| Tag (s)   | Last Changed  | Digest                                                                    |
|-----------|---------------|---------------------------------------------------------------------------|
|  `latest` | September 4th | `sha256:1bb0302242c686c184a938efc4db7a0bc9c785b7e875792b66bbeb4a367746b3` |



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

