---
title: "Image Overview: telegraf"
type: "article"
description: "Overview: telegraf Chainguard Images"
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

`experimental` [cgr.dev/chainguard/telegraf](https://github.com/chainguard-images/images/tree/main/images/telegraf)
| Tags         | Aliases                                            |
|--------------|----------------------------------------------------|
| `latest`     | `1`, `1.26`, `1.26.1`, `1.26.1-r1`                 |
| `latest-dev` | `1-dev`, `1.26-dev`, `1.26.1-dev`, `1.26.1-r1-dev` |



Minimal image with Telegraf. **EXPERIMENTAL**

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

