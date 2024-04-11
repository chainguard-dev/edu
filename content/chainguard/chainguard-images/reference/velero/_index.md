---
title: "Image Overview: velero"
linktitle: "velero"
type: "article"
layout: "single"
description: "Overview: velero Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/velero/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/velero/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/velero/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/velero/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Backup and migrate Kubernetes applications and their persistent volumes
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/velero:latest
```


<!--body:start-->
[Velero] (https://velero.io/docs/v1.13/) (formerly Heptio Ark) gives you tools to back up and restore your Kubernetes cluster resources and persistent volumes. You can run Velero with a cloud provider or on-premises. \

Velero lets you:
* Take backups of your cluster and restore in case of loss.
* Migrate cluster resources to other clusters.
* Replicate your production cluster to development and testing clusters.

## Installation and Usage

```bash
docker run cgr.dev/chainguard/velero:latest help
```

For more information, refer to the velero documentation:
- [Velero GitHub](https://github.com/vmware-tanzu/velero)
<!--body:end-->

