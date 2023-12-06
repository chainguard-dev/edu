---
title: "Image Overview: metacontroller"
linktitle: "metacontroller"
type: "article"
layout: "single"
description: "Overview: metacontroller Chainguard Image"
date: 2023-12-06 17:47:48
lastmod: 2023-12-06 17:47:48
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/metacontroller/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/metacontroller/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/metacontroller/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/metacontroller/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal Metacontroller Image
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/metacontroller:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

This image is a drop-in replacement for the upstream image.
You can run it using the helm chart with:

```shell
$ export HELM_EXPERIMENTAL_OCI=1
$ helm install my-metacontroller-helm oci://ghcr.io/metacontroller/metacontroller-helm --version v4.10.3  \
    --set image.repository=cgr.dev/chainguard/metacontroller \
    --set image.tag=latest \
    <other configuration parameters here>
```

See the [configuration](https://metacontroller.github.io/metacontroller/guide/helm-install.html#configuration) docs for more examples.
<!--body:end-->

