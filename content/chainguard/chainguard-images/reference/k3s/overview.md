---
title: "Image Overview: k3s"
type: "article"
description: "Overview: k3s Chainguard Image"
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

[cgr.dev/chainguard/k3s](https://github.com/chainguard-images/images/tree/main/images/k3s)

| Tag (s)       | Last Changed | Digest                                                                    |
|---------------|--------------|---------------------------------------------------------------------------|
|  `latest`     | August 23rd  | `sha256:31cf3b7c0fc8fae9fb8f1bbb1dcadbe77bde74430b43ddf9e36f4a0a69897ff2` |
|  `latest-dev` | August 23rd  | `sha256:c2aa6e668c435891d8869f1cfed6dee74cf028c8a227198848dbdfb67372b30c` |



Minimal image with kubectl binary. **EXPERIMENTAL**

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/k3s:latest
```

This image is a drop in replacement for the upstream `rancher/k3s` image, which means it works everywhere you would expect.

The quickest way to test it is locally with `docker`:

```bash
docker run --rm -v `pwd`:/etc/rancher/k3s --privileged -p 6443:6443 cgr.dev/chainguard/k3s:latest

KUBECONFIG=k3s.yaml kubectl get po -A
```

You can also use it as a drop in replacement in `k3d`:

```bash
k3d cluster create -i cgr.dev/chainguard/k3s:latest
```

