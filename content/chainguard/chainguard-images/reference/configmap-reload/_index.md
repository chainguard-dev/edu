---
title: "Image Overview: configmap-reload"
linktitle: "configmap-reload"
type: "article"
layout: "single"
description: "Overview: configmap-reload Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/configmap-reload/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/configmap-reload/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/configmap-reload/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/configmap-reload/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
`configmap-reload` is a simple binary to trigger a reload when Kubernetes ConfigMaps or Secrets, mounted into pods, are updated.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/configmap-reload:latest
```
<!--getting:end-->

<!--body:start-->
## Usage

This image is a drop-in replacement for the upstream image.
You can run it using the helm chart with:

```shell
$ helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
$ helm install my-release prometheus-community/alertmanager \
    --set configmapReload.enabled=true \
    --set configmapReload.image=cgr.dev/chainguard/configmap-reload \
    --set image.tag=latest
    <other configuration parameters here>
```
<!--body:end-->

