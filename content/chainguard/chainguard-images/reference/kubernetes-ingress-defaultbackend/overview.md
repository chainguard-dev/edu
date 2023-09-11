---
title: "Image Overview: kubernetes-ingress-defaultbackend"
type: "article"
description: "Overview: kubernetes-ingress-defaultbackend Chainguard Image"
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

| Tag (s)       | Last Changed  | Digest                                                                    |
|---------------|---------------|---------------------------------------------------------------------------|
|  `latest`     | September 8th | `sha256:67f6b829f165bccca5fac1b20a728a3c8bf7f3291f795feffa4eac047a04bc35` |
|  `latest-dev` | September 8th | `sha256:be7f6f0a402caf720bd7043dafe2b4e32eeb84e4a9746ba27da45638b2d6f222` |



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

