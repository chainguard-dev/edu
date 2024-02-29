---
title: "Image Overview: helm"
linktitle: "helm"
type: "article"
layout: "single"
description: "Overview: helm Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-02-29 16:25:55
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/helm/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/helm/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/helm/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/helm/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image with [helm](https://helm.sh) binary. **EXPERIMENTAL**
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/helm:latest
```
<!--getting:end-->

<!--body:start-->

## Testing the Helm Image

The following command will pull the image to your local system and automatically execute the `helm version` command:

```shell
docker run --rm  cgr.dev/chainguard/helm version
```

This will return output similar to this.

```
version.BuildInfo{Version:"v3.13.2", GitCommit:"2a2fb3b98829f1e0be6fb18af2f6599e0f4e8243", GitTreeState:"clean", GoVersion:"go1.21.4"}
```
<!--body:end-->

