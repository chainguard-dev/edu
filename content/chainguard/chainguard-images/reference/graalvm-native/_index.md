---
title: "Image Overview: graalvm-native"
linktitle: "graalvm-native"
type: "article"
layout: "single"
description: "Overview: graalvm-native Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2023-11-27 16:34:14
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/graalvm-native/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/graalvm-native/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/graalvm-native/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/graalvm-native/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Base image with just enough files to run native [GraalVM](https://www.graalvm.org/) native-image binaries.
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/graalvm-native:latest
```
<!--getting:end-->

<!--body:start-->
## Using


This image includes `glibc` and `libz`, and is designed to contain exactly what's needed to run GraalVM native-image binaries.

This image is meant to be used as a base image only, and is otherwise useless.  It contains the `wolfi-baselayout-data` package from Wolfi, which is just a set of data files needed to support glibc static binaries at runtime.

## Users

The image has a single user `nonroot` with uid `65532`, belonging to gid `65532`.
<!--body:end-->

