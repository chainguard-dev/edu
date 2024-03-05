---
title: "Image Overview: doppler-kubernetes-operator"
linktitle: "doppler-kubernetes-operator"
type: "article"
layout: "single"
description: "Overview: doppler-kubernetes-operator Chainguard Image"
date: 2024-03-05 17:06:05
lastmod: 2024-03-05 17:06:05
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/doppler-kubernetes-operator/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/doppler-kubernetes-operator/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/doppler-kubernetes-operator/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/doppler-kubernetes-operator/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Automatically sync secrets from Doppler to Kubernetes and auto-reload deployments when secrets change.
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/images/doppler-kubernetes-operator:latest
```
<!--getting:end-->

<!--body:start-->
doppler-kubernetes-operator is a Kubernetes operator, which can be deployed using helm. Refer to the [upstream repositories documentation](https://github.com/DopplerHQ/kubernetes-operator) for how to get started with doppler-kubernetes-operator.

```shell
helm repo add doppler https://helm.doppler.com
helm install doppler-kubernetes-operator doppler/doppler-kubernetes-operator

helm repo update
helm pull doppler/doppler-kubernetes-operator --untar
kubectl apply -f doppler-kubernetes-operator/crds/all.yaml

helm upgrade doppler-kubernetes-operator doppler/doppler-kubernetes-operator \
   --set image.repository=cgr.dev/chainguard/doppler-kubernetes-operator \
   --set image.tag=latest
}
```

As per [project documentation](https://github.com/DopplerHQ/kubernetes-operator/blob/main/README.md).
<!--body:end-->

