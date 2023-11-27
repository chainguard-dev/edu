---
title: "Image Overview: melange"
linktitle: "melange"
type: "article"
layout: "single"
description: "Overview: melange Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/melange/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/melange/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/melange/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/melange/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Container image for running [melange](https://github.com/chainguard-dev/melange) workflows to build APK packages.
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/melange:latest
```
<!--getting:end-->

<!--body:start-->
To build the melange workflow in [examples](examples/gnu-hello.yaml):

```
docker run --privileged -v "$PWD":/work cgr.dev/chainguard/melange build /work/examples/gnu-hello.yaml
```

Output will be in the `packages` directory.

To build the melange package for the host architecture:

```
docker run --privileged -v "$PWD":/work cgr.dev/chainguard/melange build --empty-workspace --arch $(uname -m) /work/melange.yaml
```

To get a shell, you can change the entrypoint:

```
docker run --privileged -v "$PWD":/work -it --entrypoint /bin/sh cgr.dev/chainguard/melange

/ # melange version
...
```
Note that melange uses bubblewrap internally, which requires various Linux capabilities, hence the
use of `--privileged`. Because of this requirement, we recommend this image is used only for local
development and testing.
<!--body:end-->

