---
title: "Image Overview: Kubernetes-ingress-defaultbackend"
type: "article"
description: "Overview: Kubernetes-ingress-defaultbackend Chainguard Image"
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

[cgr.dev/chainguard/kubernetes-ingress-defaultbackend](https://github.com/chainguard-images/images/tree/main/images/kubernetes-ingress-defaultbackend)

| Tag          | Last Updated | Digest                                                                    |
|--------------|--------------|---------------------------------------------------------------------------|
| `latest-dev` | 20 hours ago | `sha256:6b9e1bf2709747d866b6897be6e9e4a9a82d487640bd7cdab786dbf23e588e72` |
| `latest`     | 20 hours ago | `sha256:f2bb7657174341a7d9df0e574ee598bb5a966b0c43ca30a5c9941ecbdd8695e5` |



Minimal image that acts as a drop-in replacement for the `registry.k8s.io/defaultbackend` image. Used in some ingresses like https://github.com/kubernetes/ingress-gce and https://github.com/kubernetes/ingress-nginx

The image runs as `non-root`.

## Get It!

The image is available on `cgr.dev`:

```
docker pull cgr.dev/chainguard/kubernetes-ingress-defaultbackend:latest
```

You can run it with the standard deployment using nginx-ingress with something like:

```
helm install <RELEASE_NAME> ingress-nginx/ingress-nginx \
  --set defaultBackend.image.registry=cgr.dev/chainguard \
  --set defaultBackend.image.image=kubernetes-ingress-defaultbackend \
  --set defaultBackend.image.tag=latest
```
