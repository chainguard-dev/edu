---
title: "Image Overview: php-fpm_exporter"
linktitle: "php-fpm_exporter"
type: "article"
layout: "single"
description: "Overview: php-fpm_exporter Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-04-11 12:38:02
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/php-fpm_exporter/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/php-fpm_exporter/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/php-fpm_exporter/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/php-fpm_exporter/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal php-fpm_exporter Image
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/php-fpm_exporter:latest
```


<!--body:start-->
## Usage

This image is a drop-in replacement for the upstream image. 

Run docker manually:

```shell
docker pull cgr.dev/chainguard/php-fpm_exporter:latest
docker run -it --rm -e PHP_FPM_SCRAPE_URI="tcp://127.0.0.1:9000/status,tcp://127.0.0.1:9001/status" cgr.dev/chainguard/php-fpm_exporter:latest
``````

If you want to get more details about the php-fpm_exporter, please refer to the [official documentation](https://github.com/hipages/php-fpm_exporter#usage).
<!--body:end-->

