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

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest-dev` | September 6th | `sha256:f6e37ed60df7261786d66dd776a1c4c348a30247bd1fc368e2b5b0f0384165ad` |
|  `latest`     | September 6th | `sha256:3512cf514ada35b9f4783d39eed4b77f683cf224854d2eed9bd88ec38d0c85b6` |



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

