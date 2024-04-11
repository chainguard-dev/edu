---
title: "Image Overview: velero-plugin-for-csi"
linktitle: "velero-plugin-for-csi"
type: "article"
layout: "single"
description: "Overview: velero-plugin-for-csi Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/velero-plugin-for-csi/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/velero-plugin-for-csi/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/velero-plugin-for-csi/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/velero-plugin-for-csi/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Velero plugins for integrating with CSI snapshot API
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/velero-plugin-for-csi:latest
```


<!--body:start-->

# Usage

To get more detail about how to use this plugin, please refer to the [Container Storage Interface Snapshot Support in Velero
](https://velero.io/docs/v1.13/csi/).

To integrate Velero with the CSI volume snapshot APIs, you must enable the EnableCSI feature flag and install the Velero CSI plugins on the Velero server.

Both of these can be added with the velero install command.

```
velero install \
--features=EnableCSI \
--plugins=<object storage plugin>,cgr.dev/chainguard/velero-plugin-for-csi:latest \
...
```

For the object storage plugin, you can use the appropriate object storage plugin for your cloud provider. For example, for AWS, you can use the AWS plugin available in Chainguard image catalog: **cgr.dev/chainguard/velero-plugin-for-aws:latest**


<!--body:end-->

