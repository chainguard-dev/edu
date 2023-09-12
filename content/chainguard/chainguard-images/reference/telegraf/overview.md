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

| Tag (s)       | Last Changed   | Digest                                                                    |
|---------------|----------------|---------------------------------------------------------------------------|
|  `latest-dev` | September 11th | `sha256:546bdd3d8798178d024d8de7bdcfecddd4f93cb6d3258a10fea13e380e143199` |
|  `latest`     | September 11th | `sha256:84d68b0fcaca2bb953531521528f9ea9dcf7c21b456289f0917d332959d9a38b` |



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

