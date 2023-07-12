---
title: "Image Overview: Netcat"
type: "article"
description: "Overview: Netcat Chainguard Image"
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

| Tag      | Last Updated | Digest                                                                    |
|----------|--------------|---------------------------------------------------------------------------|
| `latest` | 19 hours ago | `sha256:df5593af7c09ae0398838b4fbcf9505f287c3373d8556106c104c9a8a18e5d7e` |



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
