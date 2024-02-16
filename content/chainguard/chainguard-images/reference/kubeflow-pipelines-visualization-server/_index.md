---
title: "Image Overview: kubeflow-pipelines-visualization-server"
linktitle: "kubeflow-pipelines-visualization-server"
type: "article"
layout: "single"
description: "Overview: kubeflow-pipelines-visualization-server Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-02-16 00:30:51
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/kubeflow-pipelines-visualization-server/" >}}
{{< tab title="Variants" active=false url="/chainguard/chainguard-images/reference/kubeflow-pipelines-visualization-server/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kubeflow-pipelines-visualization-server/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubeflow-pipelines-visualization-server/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimal image with [ml-pipeline/visualization-server](https://github.com/kubeflow/pipelines/tree/master/backend/src/apiserver/visualization).
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/kubeflow-pipelines-visualization-server:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

This image is a drop-in replacement for the upstream `ml-pipeline/visualization-server` image.

To try it out, follow the [official installation
instructions](https://github.com/kubeflow/pipelines/tree/master/backend/src/apiserver/visualization#how-to-create-predefined-visualizations).

Please also notice the [known limitations](https://github.com/kubeflow/pipelines/tree/master/backend/src/apiserver/visualization#known-limitations) as described in the upstream documentation.
<!--body:end-->

