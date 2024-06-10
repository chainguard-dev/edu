---
title: "Image Overview: busybox-fips"
linktitle: "busybox-fips"
type: "article"
layout: "single"
description: "Overview: busybox-fips Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-06-10 00:50:47
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
Container image with only busybox and glibc and openssl libraries with a fips provider. Suitable for running any binaries that only need a shell, glibc and an openssl capable of FIPS mode (e.g. for running any GO FIPS binaries with a shell).

Note currently no busybox applets utilise the FIPS provider.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/busybox-fips:latest
```


<!--body:start-->
## Usage

One can execute any busybox applets like so:

```shell
docker run -it cgr.dev/chainguard-private/busybox-fips:latest echo hello world!
```

Also, note that you can open an interactive shell with command like the following:

```shell
docker run -it cgr.dev/chainguard-private/busybox-fips:latest sh
```

This image is particularly useful to execute shell commands together
with GO FIPS binaries, for example as part of Tekton Pipelines
Controller FIPS deployment set shell-image to
cgr.dev/chainguard/busybox-fips.

<!--body:end-->

