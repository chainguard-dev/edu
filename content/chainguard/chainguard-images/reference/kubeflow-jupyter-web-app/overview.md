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
|  `latest`     | August 16th  | `sha256:193b856da601b7aeb8ddb6d24393b37986c14a74bfaf29f3c9cd2ce6ac4d7fe7` |
|  `latest-dev` | August 16th  | `sha256:255d50ea3684a4c14e64c23220d95c7b490ec6b8fb415c87658a9291fc1c3999` |



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
