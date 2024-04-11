---
title: "Image Overview: velero-plugin-for-aws"
linktitle: "velero-plugin-for-aws"
type: "article"
layout: "single"
description: "Overview: velero-plugin-for-aws Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2024-04-11 12:38:02
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/velero-plugin-for-aws/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/velero-plugin-for-aws/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/velero-plugin-for-aws/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/velero-plugin-for-aws/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Plugins to support Velero on AWS
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/velero-plugin-for-aws:latest
```


<!--body:start-->

##  Usage

The [Velero plugin for AWS documentation](https://velero.io/plugins/) can be found on Velero's official website. Velero have a guide on [getting started with Velero plugin for AWS](https://github.com/vmware-tanzu/velero-plugin-for-aws#setup), which demonstrates how to the plugin to backup and restore your Kubernetes cluster resources to AWS S3.  

To use the Chainguard Image version of the plugin, follow the Velero instructions and replace the `velero/velero-plugin-for-aws` image with `cgr.dev/chainguard/velero-plugin-for-aws` in the Velero's install command.  

```bash
$ velero install \
    --provider aws \
    --plugins cgr.dev/chainguard/velero-plugin-for-aws:latest \
   ...
```
<!--body:end-->

