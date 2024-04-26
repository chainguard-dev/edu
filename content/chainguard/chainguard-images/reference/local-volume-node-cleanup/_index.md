---
title: "Image Overview: local-volume-node-cleanup"
linktitle: "local-volume-node-cleanup"
type: "article"
layout: "single"
description: "Overview: local-volume-node-cleanup Chainguard Image"
date: 2024-04-26 00:36:54
lastmod: 2024-04-26 00:36:54
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/local-volume-node-cleanup/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/local-volume-node-cleanup/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/local-volume-node-cleanup/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/local-volume-node-cleanup/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
The local volume node cleanup controller removes PersistentVolumes and PersistentVolumeClaims that reference deleted Nodes.
<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/local-volume-node-cleanup:latest
```


<!--body:start-->

## Usage

There is an example of how to deploy the local volume node cleanup controller in the [official documentation](https://github.com/kubernetes-sigs/sig-storage-local-static-provisioner/blob/master/docs/node-cleanup-controller.md#usage), but here is a quick guide:

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/sig-storage-local-static-provisioner/master/deployment/kubernetes/example/node-cleanup-controller/rbac.yaml

kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/sig-storage-local-static-provisioner/master/deployment/kubernetes/example/node-cleanup-controller/deployment.yaml
        
kubectl set image deployment/local-volume-node-cleanup-controller local-volume-node-cleanup-controller="cgr.dev/chainguard/local-volume-node-cleanup:latest"
```

Do not forget to change the arguments in the deployment file to match your environment. Because in the documentation, they mentinoded that these are the (optional) important arguments that are highly recommended to be used: https://github.com/kubernetes-sigs/sig-storage-local-static-provisioner/blob/master/docs/node-cleanup-controller.md#important-optional-arguments-that-are-highly-recommended-to-be-used

<!--body:end-->

