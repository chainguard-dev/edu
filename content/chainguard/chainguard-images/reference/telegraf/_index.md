---
title: "Image Overview: telegraf"
linktitle: "telegraf"
type: "article"
layout: "single"
description: "Overview: telegraf Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-02-16 00:30:51
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu: 
  docs: 
    parent: "images-reference"
weight: 500
toc: true
---

{{< tabs >}}
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/telegraf/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/telegraf/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/telegraf/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/telegraf/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image with Telegraf agent for collecting, processing, aggregating, and writing metrics.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/telegraf:latest
```
<!--getting:end-->

<!--body:start-->
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
<!--body:end-->

