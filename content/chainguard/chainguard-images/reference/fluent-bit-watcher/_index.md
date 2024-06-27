---
title: "Image Overview: fluent-bit-watcher"
linktitle: "fluent-bit-watcher"
type: "article"
layout: "single"
description: "Overview: fluent-bit-watcher Chainguard Image"
date: 2024-06-27 00:41:27
lastmod: 2024-06-27 00:41:27
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/fluent-bit-watcher/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/fluent-bit-watcher/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/fluent-bit-watcher/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/fluent-bit-watcher/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->

## Overview

A fluent-bit image, with an additional wrapper (fluent-watcher), which auto-restarts fluent-bit whenever there are config changes.

<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/fluent-bit-watcher:latest
```


<!--body:start-->

## Usage

The `fluent-bit-watcher` image is a wrapper around the `fluent-bit` image. It watches the `watch-path` for changes and restarts `fluent-bit` whenever a change is detected.

You can use Helm to deploy `fluent-bit-watcher` with the following steps:

Add the `fluent` Helm repository:

```shell
helm repo add fluent https://fluent.github.io/helm-charts
```
Add the following to your `values.yaml` file:

```yaml
image:
  repository: cgr.dev/chainguard-private/fluent-bit-watcher
  tag: latest
command: "/fluent-bit/bin/fluent-watcher"
args:
- "-c=/fluent-bit/etc/conf/fluent-bit.conf"
- "-watch-path=/fluent-bit/etc/conf"
```

Then install the chart:

```shell
helm upgrade --install fluent-bit \
    -f values.yaml \
    fluent/fluent-bit
``` 

<!--body:end-->

