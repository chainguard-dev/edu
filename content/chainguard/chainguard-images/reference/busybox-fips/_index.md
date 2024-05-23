---
title: "Image Overview: busybox-fips"
linktitle: "busybox-fips"
type: "article"
layout: "single"
description: "Overview: busybox-fips Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-05-23 00:45:07
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/busybox-fips/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/busybox-fips/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/busybox-fips/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/busybox-fips/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Container image with only busybox and libc (available in both musl and glibc variants). Suitable for running any binaries that only have a dependency on glibc/musl.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/busybox-fips:latest
```


<!--body:start-->
## Upcoming Changes

On July 15, 2024 the `busybox:latest` image will move from a Alpine base to a Wolfi base,
in-line with all other images in our registry. We do not expect this to cause breakages, but
encourage all users to test and verify the new version.

You can test today by migrating to the `cgr.dev/chainguard/busybox:latest-glibc` image. From July 15, the `:latest` and `:latest-glibc` will point to the same image.

Full details are in [this blog post](https://www.chainguard.dev/unchained/changes-to-static-git-and-busybox-developer-images-2).

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

