---
title: "Image Overview: busybox"
linktitle: "busybox"
type: "article"
layout: "single"
description: "Overview: busybox Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-01-17 00:18:58
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/busybox/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/busybox/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/busybox/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/busybox/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Container image with only busybox and libc (available in both musl and glibc variants). Suitable for running any binaries that only have a dependency on glibc/musl.
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/busybox:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

Chainguard offers two different variations of the `busybox` Image. Both contain the BusyBox software but are built against different variants of `libc`:

- `latest`, meant for variants based on `musl`
- `latest-glibc`, meant for variants based on `glibc`

You can ensure that either of these Images are working correctly by testing that they can run commands and return output. The following commands will both return `hello world!` in your terminal:

`musl`:
```shell
docker run -it cgr.dev/chainguard/busybox:latest echo hello world!
```

`glibc`:
```shell
docker run -it cgr.dev/chainguard/busybox:latest-glibc echo hello world!
```

Also, note that you can open an interactive shell on either version of the Image with command like the following:

```shell
docker run -it cgr.dev/chainguard/busybox:latest sh
```
<!--body:end-->

