---
title: "Image Overview: kubeflow-volumes-web-app"
linktitle: "kubeflow-volumes-web-app"
type: "article"
layout: "single"
description: "Overview: kubeflow-volumes-web-app Chainguard Image"
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
{{< tab title="Overview" active=true url="/chainguard/chainguard-images/reference/kubeflow-volumes-web-app/" >}}
{{< tab title="Details" active=false url="/chainguard/chainguard-images/reference/kubeflow-volumes-web-app/image_specs/" >}}
{{< tab title="Tags History" active=false url="/chainguard/chainguard-images/reference/kubeflow-volumes-web-app/tags_history/" >}}
{{< tab title="Provenance" active=false url="/chainguard/chainguard-images/reference/kubeflow-volumes-web-app/provenance_info/" >}}
{{</ tabs >}}



<!--overview:start-->
Minimalist Kubeflow Machine Learning Toolkit for Kubernetes Images
<!--overview:end-->

<!--getting:start-->
## Download this Image
The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/kubeflow:latest
```
<!--getting:end-->

<!--body:start-->

## Usage

There are kustomize files exist for deploying this image to a Kubernetes cluster in kubeflow official GitHub [repository](https://github.com/kubeflow/kubeflow/).

All you need to do is issuing the following commands:

* For [jupyter-web-app](https://github.com/kubeflow/kubeflow/tree/master/components/crud-web-apps/jupyter/manifests)

```shell
$ cat <<EOF > kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - https://github.com/kubeflow/kubeflow/components/crud-web-apps/jupyter/manifests/overlays/istio?ref=master
images:
  - name: docker.io/kubeflownotebookswg/kubeflow-jupyter-web-app
    newName: cgr.dev/chainguard/kubeflow-jupyter-web-app
    newTag: latest
namespace: jupyter-web-app
EOF
```

* For [volumes-web-app](https://github.com/kubeflow/kubeflow/tree/master/components/crud-web-apps/volumes/manifests)

```shell
$ cat <<EOF > kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - https://github.com/kubeflow/kubeflow/components/crud-web-apps/volumes/manifests/overlays/istio?ref=master
images:
  - name: docker.io/kubeflownotebookswg/kubeflow-volumes-web-app
    newName: cgr.dev/chainguard/kubeflow-volumes-web-app
    newTag: latest
namespace: volumes-web-app
EOF
```

Finally, apply the kustomize files:

```shell
$ kubectl apply -k .
```
<!--body:end-->

