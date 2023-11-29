---
title: "Image Overview: helm"
linktitle: "helm"
type: "article"
layout: "single"
description: "Overview: helm Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/helm/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/helm/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/helm/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/helm/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image with [helm](https://helm.sh) binary. **EXPERIMENTAL**
<!--overview:end-->

<!--getting:start-->
## Get It!
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/helm:latest
```
<!--getting:end-->

<!--body:start-->
## Image Variants

Our `latest` tags use the most recent build of the [Wolfi helm](https://github.com/wolfi-dev/os/blob/main/helm.yaml) package. The following tagged variants are available without authentication:

- `latest`: This is a distroless image for running helm to install packages to a kubernetes cluster. It does not include `apk-tools` or `bash`, so no shell will be available.
- `latest-dev`: This is a development / builder image that includes `bash`, `apk-tools`, and `busybox`. This variant allows you to customize your final image with additional Wolfi packages.

### Helm Version
This will automatically pull the image to your local system and execute the command `helm version`:

```shell
docker run --rm  cgr.dev/chainguard/helm version
```

You should see output similar to this:

```
version.BuildInfo{Version:"v3.13.1", GitCommit:"3547a4b5bf5edb5478ce352e18858d8a552a4110", GitTreeState:"dirty", GoVersion:"go1.21.3"}
```
<!--body:end-->

