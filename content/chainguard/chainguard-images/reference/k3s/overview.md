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
|  `latest-dev` | August 8th   | `sha256:a3670b0b109a2b728e28a03c8e774a83a4c7942ed357687d0700e4f25a0de685` |
|  `latest`     | August 8th   | `sha256:ffadb48a2aa7bf61e8dbe2bf2290cbb116f069d271581d4dca975212ad8eb939` |



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

