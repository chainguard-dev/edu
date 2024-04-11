---
title: "Image Overview: nfs-subdir-external-provisioner"
linktitle: "nfs-subdir-external-provisioner"
type: "article"
layout: "single"
description: "Overview: nfs-subdir-external-provisioner Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/nfs-subdir-external-provisioner/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/nfs-subdir-external-provisioner/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/nfs-subdir-external-provisioner/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/nfs-subdir-external-provisioner/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Dynamic sub-dir volume provisioner on a remote NFS server.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/nfs-subdir-external-provisioner:latest
```


<!--body:start-->
## Testing

The NFS subdir external provisioner is an automatic provisioner for Kubernetes that uses your already configured NFS server, automatically creating Persistent Volumes.

To get more information about the nfs-subdir-external-provisioner, visit the [GitHub repository](https://github.com/kubernetes-sigs/nfs-subdir-external-provisioner).

There is a Helm chart available for the nfs-subdir-external-provisioner. To install it, run:

```
$ helm repo add nfs-subdir-external-provisioner https://kubernetes-sigs.github.io/nfs-subdir-external-provisioner/

$ helm install nfs-subdir-external-provisioner nfs-subdir-external-provisioner/nfs-subdir-external-provisioner \
    --set image.repository=cgr.dev/chainguard/nfs-subdir-external-provisioner \
    --set image.tag=latest \
    --set nfs.server=x.x.x.x \
    --set nfs.path=/exported/path
```
<!--body:end-->

