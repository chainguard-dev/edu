---
title: "Image Overview: velero-restore-helper"
linktitle: "velero-restore-helper"
type: "article"
layout: "single"
description: "Overview: velero-restore-helper Chainguard Image"
date: 2024-03-27 00:48:55
lastmod: 2024-03-27 00:48:55
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/velero-restore-helper/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/velero-restore-helper/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/velero-restore-helper/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/velero-restore-helper/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Backup and migrate Kubernetes applications and their persistent volumes
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/velero-restore-helper:latest
```
<!--getting:end-->

<!--body:start-->
Velero uses a helper init container when performing a filesystem restore (FSB in Velero's terminology). To use this image as the helper follow the [File System Backup](https://velero.io/docs/main/file-system-backup/#customize-restore-helper-container) documentation, and edit the provided `ConfigMap` to use `cgr.dev/chainguard/velero-restore-helper`.

## Installation and Usage

```bash
docker run cgr.dev/chainguard/velero-restore-helper:latest help
```

For more information, refer to the velero documentation:
- [Velero GitHub](https://github.com/vmware-tanzu/velero)
<!--body:end-->

