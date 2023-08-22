---
title: "Image Overview: kubernetes-dns-node-cache"
type: "article"
description: "Overview: kubernetes-dns-node-cache Chainguard Image"
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

[cgr.dev/chainguard/kubernetes-dns-node-cache](https://github.com/chainguard-images/images/tree/main/images/kubernetes-dns-node-cache)

| Tag (s)   | Last Changed | Digest                                                                    |
|-----------|--------------|---------------------------------------------------------------------------|
|  `latest` | August 15th  | `sha256:93d2737bdd1ef821f77e7978ea46d0ed3af04ce304edb5e4d6303ddbc63cfd34` |



Minimal image that acts as a drop-in replacement for the [NodeLocal DNSCache](https://github.com/kubernetes/dns) image.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/kubernetes-dns-node-cache:latest
```

## Usage

```shell
helm repo add deliveryhero https://charts.deliveryhero.io/
helm repo update
helm install node-local-dns deliveryhero/node-local-dns \
    --set image.repository=cgr.dev/chainguard/kubernetes-dns-node-cache \
    --set image.tag=latest
```

