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
|  `latest-dev` | August 31st  | `sha256:e21420f50e614819722ac690353064003a3245343ed32339dcf447a8a57e0061` |
|  `latest`     | August 31st  | `sha256:e861eccf3776875e1302fde8b462e7fac4d3d83a77696a98bee2004e3f0e6961` |



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

