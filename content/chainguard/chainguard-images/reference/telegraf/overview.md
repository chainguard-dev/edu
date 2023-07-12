---
title: "Image Overview: Telegraf"
type: "article"
description: "Overview: Telegraf Chainguard Image"
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

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest`     | 19 hours ago | `sha256:8a37469195442ca1cca10c25505f9255db18ea596b46d36e706c76f0204054f1` |
| `latest-dev` | 19 hours ago | `sha256:d5fbbe30c031a00e78e5fb3ff9e84f7d7cda039086c4b23b620e07947c3c4ac7` |



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
