---
title: "Image Overview: cadvisor"
type: "article"
description: "Overview: cadvisor Chainguard Image"
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

[cgr.dev/chainguard/cadvisor](https://github.com/chainguard-images/images/tree/main/images/cadvisor)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest-dev` | August 16th  | `sha256:ee5e25d6df1fe18d8e17019a5e8dce79e537791f959070ac272154e439d1a32d` |
|  `latest`     | August 16th  | `sha256:eb2301108f572d8172143835309e530bed732e43443e15c939f2ab963143db27` |



[cAdvisor (Container Advisor)](https://github.com/google/cadvisor) provides container users an understanding of the resource usage and performance characteristics of their running containers.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/cadvisor
```

## Usage

See the [RUNNING.md](https://github.com/google/cadvisor/blob/master/docs/running.md) for the instructions. For the [Kubernetes deployment](https://github.com/google/cadvisor/tree/master/deploy/kubernetes), you can use the Kustomize:

```bash
cat <<EOF >> kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - https://github.com/google/cadvisor/deploy/kubernetes/base?ref=master
images:
  - name: gcr.io/cadvisor/cadvisor
    newName: cgr.dev/chainguard/cadvisor
    newTag: latest
namespace: cadvisor
EOF
kubectl apply -k .
```

