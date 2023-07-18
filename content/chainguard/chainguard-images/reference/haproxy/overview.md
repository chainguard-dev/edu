---
title: "Image Overview: haproxy"
type: "article"
description: "Overview: haproxy Chainguard Image"
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

[cgr.dev/chainguard/haproxy](https://github.com/chainguard-images/images/tree/main/images/haproxy)

| Tag (s)   | Last Changed | Digest                                                                    |
|-----------|--------------|---------------------------------------------------------------------------|
|  `latest` | July 18th    | `sha256:4f1d8dcd871d501f27d233e6fb403209c55c7cace19c3ac97c280e9c752d74e8` |









A minimal haproxy base image rebuilt every night from source.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/haproxy:latest
```

## Usage

Similar to the `docker-library/haproxy` image, this image does not come with any default configuration.

Please refer to [upstream's excellent (and comprehensive) documentation](https://docs.haproxy.org/) on the subject of configuring HAProxy for your needs.

Let say you have a `haproxy.cfg` config file is current working directory. To test that configuration file, you can run the following command

```
docker run -it --rm -v "$(pwd):/etc/haproxy" --name haproxy-syntax-check cgr.dev/chainguard/haproxy haproxy -c -f /etc/haproxy/haproxy.cfg
```

In order for the container to work, you need to mount your custom `haproxy.cfg` file in the container. The following example runs HAProxy with a custom configuration file:

```
docker run -it --rm -v "$(pwd):/etc/haproxy" cgr.dev/chainguard/haproxy haproxy -f /etc/haproxy/haproxy.cfg
```

