---
title: "Image Overview: telegraf"
type: "article"
description: "Overview: telegraf Chainguard Image"
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

[cgr.dev/chainguard/telegraf](https://github.com/chainguard-images/images/tree/main/images/telegraf)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | July 18th    | `sha256:e9f865fa8a43b7ca2e9dc437b370ffb411aa69c34d6970cbaeaece9b1f17ff8d` |
|  `latest`     | July 14th    | `sha256:dc63911be8051cd2d919bd53e9789ea9e01261b4f26c6935db92b29767f254bf` |



Minimal image with Telegraf.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/telegraf:latest
```

## Using Telegraf

The Chainguard Telegraf image contains the `telegraf` binary.

Telegraf needs a config file to run.
The default location for this config file is at `/etc/telegraf/telegraf.conf`.
One is not provided by default with the image.

This location can be overridden with the `---config` or `--config-directory` flags.

```shell
 % docker run cgr.dev/chainguard/telegraf
2023-03-28T14:07:48Z I! Loading config file: /etc/telegraf/telegraf.conf
2023-03-28T14:07:48Z E! [telegraf] Error running agent: no outputs found, did you provide a valid config file?
```

