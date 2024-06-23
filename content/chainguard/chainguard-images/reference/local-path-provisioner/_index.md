---
title: "Image Overview: local-path-provisioner"
linktitle: "local-path-provisioner"
type: "article"
layout: "single"
description: "Overview: local-path-provisioner Chainguard Image"
date: 2024-06-23 00:43:06
lastmod: 2024-06-23 00:43:06
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/local-path-provisioner/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/local-path-provisioner/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/local-path-provisioner/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/local-path-provisioner/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->

## Overview

Local Path Provisioner provides a way for the Kubernetes users to utilize the local storage in each node. Based on the user configuration, the Local Path Provisioner will create either hostPath or local based persistent volume on the node automatically. It utilizes the features introduced by Kubernetes [Local Persistent Volume](https://kubernetes.io/blog/2018/04/13/local-persistent-volumes-beta/) feature, but makes it a simpler solution than the built-in local volume feature in Kubernetes.

<!--overview:end-->

## Download this Image

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard-private/local-path-provisioner:latest
```


<!--body:start-->
## Usage

You can deploy the `local-path-provisioner` using the Kustomization:

```bash
$ cat <<EOF > kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - https://github.com/rancher/local-path-provisioner/deploy?ref=master
images:
  - name: rancher/local-path-provisioner:master-head
    newName: cgr.dev/chainguard/local-path-provisioner
    newTag: latest
namespace: local-path-provisioner
EOF
$ kubectl apply -k .
```

> [!TIP]
> Please jump to official [USAGE](https://github.com/rancher/local-path-provisioner/tree/master?tab=readme-ov-file#usage) documentation for more details.
<!--body:end-->

