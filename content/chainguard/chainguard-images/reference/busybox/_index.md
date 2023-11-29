---
title: "Image Overview: busybox"
linktitle: "busybox"
type: "article"
layout: "single"
description: "Overview: busybox Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2023-11-29 00:31:44
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

- [Documentation](https://edu.chainguard.dev/chainguard/chainguard-images/reference/busybox)
- [Usage](https://github.com/chainguard-images/images/blob/main/images/busybox/README.md#usage)
- [Provenance Information](https://edu.chainguard.dev/chainguard/chainguard-images/reference/busybox/provenance_info/)

## Image Variants

There are two variants, one for musl and one for gclib.

- `latest`: This is a image that has busybox and is for musl based variants.
- `latest-glibc`: This is a image that has busybox and is for glibc based variants.

## Usage

We are going to run a simple hello world to make sure things are working either on the musl or glibc one:

`musl`:
```shell
docker run -it cgr.dev/chainguard/busybox:latest echo hello world!
```

`glibc`:
```shell
docker run -it cgr.dev/chainguard/busybox:latest-glibc echo hello world!
```

and you should see `hello world!` printed.

You can get a running shell on the image like this:

```shell
docker run -it cgr.dev/chainguard/busybox:latest sh
```
<!--body:end-->

