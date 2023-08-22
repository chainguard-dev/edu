---
title: "Image Overview: kubeflow-jupyter-web-app"
type: "article"
description: "Overview: kubeflow-jupyter-web-app Chainguard Image"
date: 2022-11-01T11:07:52+02:00
lastmod: 2022-11-01T11:07:52+02:00
draft: false
tags: ["Reference", "Chainguard Images", "Product"]
images: []
menu:
  docs:
    parent: "images-reference"
weight: 500
toc: true
---

[cgr.dev/chainguard/kubeflow-jupyter-web-app](https://github.com/chainguard-images/images/tree/main/images/kubeflow-jupyter-web-app)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | August 17th  | `sha256:50c44ce64bc7148bb55eb68d1149a377e5c1cd5f1d4757c0ca359396c968cb98` |
|  `latest`     | August 17th  | `sha256:54ca0b7ff427655c14d4db64db4c614b0bf8270fbfd55d236a8bea660acbeb46` |



Minimalist Jupyter Web Application.

## Usage

There are kustomize files exist for deploying this image to a kubernetes cluster in kubeflow official GitHub [repository](github.com/kubeflow/kubeflow/). You can find them in [kubeflow/kubeflow/tree/master/components/crud-web-apps/jupyter/manifests](https://github.com/kubeflow/kubeflow/tree/master/components/crud-web-apps/jupyter/manifests).

All you need to do is running the following command in the directory of the kustomize files:

```bash
$ kubectl create ns kubeflow
$ export CURRENT_JWA_IMG=docker.io/kubeflownotebookswg/jupyter-web-app:latest
$ export PR_JWA_IMG=cgr.dev/chainguard/kubeflow-jupyter-web-app:latest
$ kustomize build overlays/istio | sed "s#$CURRENT_JWA_IMG#$PR_JWA_IMG#g" | kubectl apply -f -
$ kubectl wait pods -n kubeflow -l app=jupyter-web-app --for=condition=Ready --timeout=300s
````

then you will be having a Jupyter Web Application running in your kubernetes cluster, voila!

